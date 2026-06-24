# the entry point- where it all connects 
#creates fastAPI app ,database tables,defines all end points

from fastapi import FastAPI ,Depends,HTTPException
from sqlalchemy.orm import Session
from typing import List
import models,schemas, crud
from database import get_db, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Grade Tracker",description="Track student grades with FastAPI",version ="1.0.0")

#create
@app.post("/students/",response_model= schemas.StudentResponse)
def create_student(student:schemas.StudentCreate,db:Session = Depends(get_db)):
    return crud.create_student(db,student)

#read all
@app.get("/students/",response_model = List[schemas.StudentResponse] )
def get_students(db:Session = Depends(get_db)):
    return crud.get_students(db)

@app.get("/students/{student_id}",response_model=schemas.StudentResponse)
def get_student(student_id:int, db:Session = Depends(get_db)):
    student =  crud.get_student(db,student_id)
    if not student:
        raise HTTPException(404,"Student not found")
    return student 

#update
@app.put("/students/{student_id}",response_model=schemas.StudentResponse)
def update_student(student_id:int, data: schemas.StudentUpdate, db:Session= Depends(get_db)):
    student_updated = crud.update_student(db,student_id,data)
    if not student_updated:
        raise HTTPException(404,"Student already exists")
    return student_updated

#delete
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db:Session= Depends(get_db)):
    student = crud.delete_student(db, student_id)
    if not student:
        raise HTTPException(404,"Student not found")
    return {"message":"Student deleted successfully"}