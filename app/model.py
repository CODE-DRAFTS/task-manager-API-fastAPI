from pydantic import BaseModel
from typing import Optional


class AddTask( BaseModel):
    title: str
    completed: Optional[bool] = False

class UpdateTask( BaseModel):
    title: Optional[str]
    completed: Optional[bool]
