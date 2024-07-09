from pydentic import BaseModel


class Task(BaseModel):
    title: str
    description: str
    project_id: int
    assignee_id: int
    completed: bool
