from http.client import HTTPException

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from auth import AuthHandler
router = APIRouter()
auth_handler = AuthHandler()

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