from typing import Optional
from pydantic import BaseModel


class ManagerSchema(BaseModel):
    name: str
    role: str
    age: int


class UpdateManagerSchema(BaseModel):
    name: Optional[str]
    role: Optional[str]
    age: Optional[int]


def responseModel(data, message):
    return {"data": [data], code: 200, "message": message}
