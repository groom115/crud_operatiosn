from typing import Optional
from pydantic import BaseModel

class StudentSchema(BaseModel):
    fullname: str
    email: str
    course: str
    cgpa: float
    year: str

class UpdateStudentSchema(BaseModel):
    fullname: Optional[str]
    email: Optional[str]
    course: Optional[str]
    cgpa: Optional[float]
    year: Optional[str]

def responseModel(data, message):
    return {
        "data": [data],
        code: 200,
        "message": message
    }