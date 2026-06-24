#databse operations happen here
from sqlalchemy.orm import Session
import models,schemas

def create_student(db: Session, student:schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)#stage the record
    db.commit()#saves to disk
    db.refresh(db_student)#reload the object from db after saving
    return db_student#return completed student object


#read one record
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


#read all records
def get_students(db: Session):
    return db.query(models.Student).all()

#update a record
def update_student(db: Session, student_id: int,data: schemas.StudentUpdate):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        return None
    updates = data.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(student, field, value)

    db.commit()
    db.refresh(student)
    return student 

#delete/remove a record
def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        return None
    db.delete(student)
    db.commit()
    return student 