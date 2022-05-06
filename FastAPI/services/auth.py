from fastapi import Depends, HTTPException, status
from models.auth import TokenData
from repo.baseRepo import *
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from datetime import datetime, timedelta
from jose import JWTError, jwt
import config as config
import bcrypt, os

collection = config.DUHUITEST
load_dotenv(verbose=True)
JWT_SECRET = os.getenv('JWT_SECRET')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class UserService:

    # 회원가입
    async def addUser(self, userData: dict) -> dict:
        user = await insert_one(
            config.DB_SELFLEARNING,
            collection,
            userData
        )
        newUser = await find_one(
            config.DB_SELFLEARNING,
            collection,
            {"_id": user.inserted_id})

        return newUser

    # 전체 user 검색
    async def searchUsers(self):
        users = []
        async for user in find(config.DB_SELFLEARNING, collection):
            users.append(user)
        return users

    # 해당 user 검색
    async def searchUser(self, username: str) -> dict:
        user = await find_one(
            config.DB_SELFLEARNING,
            collection,
            {"username": username})
        if user:
            return user

    # 토큰 생성
    def createAccessToken(self, data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return encoded_jwt

    # 비밀번호 확인
    def verifyPassword(self, plainPassword: str, hashedPassword):
        return bcrypt.checkpw(plainPassword.encode('utf-8'), hashedPassword)

    # 인증
    async def authenticate(self, username, password):
        try:
            user = await self.searchUser(username)
            passwordCheck = self.verifyPassword(password, user['password'])
            return passwordCheck
        except:
            return False

    # 현재 사용자
    async def getCurrentUser(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username = username)
        except JWTError:
            raise credentials_exception
        user = await self.searchUser(username=token_data.username)
        if user is None:
            raise credentials_exception
        return user