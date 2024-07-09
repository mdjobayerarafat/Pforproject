from pydentic import BaseModel


class Project(BaseModel):
    name: str
    description: str
    owner_id: int
