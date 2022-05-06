from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
import bcrypt

from services.auth import *
from models.auth import *
from dtos.authDto import *

router = APIRouter(tags=['User'])

userService = UserService()

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signUp(newUser: NewUser):
    hashPW = bcrypt.hashpw(newUser.password.encode("utf-8"), bcrypt.gensalt())
    newUser = jsonable_encoder(newUser)
    newUser['password'] = hashPW
    new_user = await userService.addUser(newUser)
    return UsersDto(**new_user)

@router.post("/token" , response_model=Token)
async def login(formData: OAuth2PasswordRequestForm = Depends()):
    username = formData.username
    password = formData.password
    flag = await userService.authenticate(username, password)
    if flag:
        access_token = userService.createAccessToken(
            data={"sub": username}, expires_delta = timedelta(minutes=30)) #추후에 minutes dotenv에 추가하여 사용
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="do not creating token")

@router.get("/detail")
async def user_detail(current_user: NewUser = Depends(userService.getCurrentUser)):
    return {"name": "Danny", "email": "danny@tutorialsbuddy.com"}