from fastapi import FastAPI, Depends
import uvicorn


from typing import List
from sqlalchemy.orm import Session
from db import get_db
from modle import StudentEntity, StudentBase, StudentCreate, StudentOut

app = FastAPI()

@app.get("/students/", response_model=List[StudentOut])
async def get_students(db: Session = Depends(get_db)):
    return db.query(StudentEntity).all()

@app.post("/students/", response_model=StudentOut)
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):

    db_student = StudentEntity(
        name=student.name, 
        age=student.age
        )
    
    db.add(db_student)
    db.commit()

    # db.refresh(db_student)
    return db_student


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)