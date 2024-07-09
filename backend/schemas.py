from pydentic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    username: str
    email: str


class Tocken(BaseModel):
    access_tocken: str
    tocken_type: str
