from http.client import HTTPException

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from rich import status
from starlette.responses import JSONResponse

from auth import AuthHandler
from models import fake_users_db

router = APIRouter()
auth_handler = AuthHandler()


@router.post("/register")
async def register(username: str, password: str):
    user = await auth_handler.get_user(username)
    if user:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = await auth_handler.get_password_hash(password)
    fake_users_db.append({"username": username, "hashed_password": hashed_password})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "User created successfully"})

@router.post("/login")
async def login(username: str, password: str):
    user = await auth_handler.authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = await auth_handler.create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
async def logout(token: str = Depends(auth_handler.auth_wrapper)):
    await auth_handler.blocklist_token(token)
    return {"message": "Logged out successfully"}


@router.get("/users/me")
async def read_users_me(token: str = Depends(auth_handler.auth_wrapper)):
    return {"username": token}
