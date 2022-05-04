from repo.baseRepo import *
import config as config

collection = config.DUHUITEST



class UserService:

    async def is_email_exist(self, email: str) -> dict:
        getEmail = await find_one(
                config.DB_SELFLEARNING,
                collection,
                {"email": email})
        if getEmail:
            return True
        return False

    
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