from pydantic import BaseModel
from typing import Optional

#what user sends to create ,when someone wants to add a new student
#(name,course,grade,email-->fields they must send in their request)
class StudentCreate(BaseModel):
    name: str
    course: str
    grade: float = 0.0
    email:str

#what user sends to update
#When someone wants to change a student's details
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    course: Optional[str] = None
    grade: Optional[float] = None
    #optional --should be able to send just one field

#what comes back if someone makes a request
#notice the student response includes id,after creating a student we want the user to know the id they were assigned to
class StudentResponse(BaseModel):
    id: int
    name: str
    course: str
    grade: float
    email: str

    class Config:#special class in pydantic,holds a configuration setting 
        from_attributes = True #without this pydantic cannot read SQLAlchemy
        
