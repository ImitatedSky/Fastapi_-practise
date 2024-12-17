from typing import List

import uvicorn
from db import get_db
from fastapi import Depends, FastAPI
from modle import StudentBase, StudentCreate, StudentEntity, StudentOut
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/students/", response_model=List[StudentOut])
async def get_students(db: Session = Depends(get_db)):
    return db.query(StudentEntity).all()


@app.post("/students/", response_model=StudentOut)
async def create_student(
    student: StudentCreate, db: Session = Depends(get_db)
):

    db_student = StudentEntity(name=student.name, age=student.age)

    db.add(db_student)
    db.commit()

    # db.refresh(db_student)
    return db_student


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
