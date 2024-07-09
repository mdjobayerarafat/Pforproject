from pydentic import BaseModel
from typing import List


class User(BaseModel):
    username: str
    email: str
    hashed_password: str
