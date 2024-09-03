import uvicorn
from fastapi import FastAPI , Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field 
from typing import Optional , List , Union

from sqlalchemy import create_engine , Column , Integer , String, Select
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, Session

class Base(DeclarativeBase):
    """
    Base class for all the models.
    """
    pass

# 根據使用的DB，修改以下的連接字串
engine = create_engine("mysql+mysqldb://root:test@localhost/testdb", echo=True)

# Define the database models 用於定義資料庫結構
class StudentEntity(Base):
    # Define the table name
    __tablename__ = "students"

    # Define the columns
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[int] = mapped_column(String(128), nullable=False)
    age : Mapped[int] = mapped_column(Integer, nullable=False)

    """ 
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    age = Column(Integer, nullable=False)
    """

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)
app = FastAPI()


# define API models 用於API的模型
class StudentBase(BaseModel):
    name: str = Field(..., example="PC Pat")
    age: int

class StudentCreate(StudentBase):
    ...

class StudentOut(StudentBase):
    id: int = Field(..., example=1)


# 前面已經定義好Session()，這裡直接使用
def get_db():
    db = SessionLocal()
    try:
        # 這裡使用yield，而不是return，是為了確保db.close()會被執行
        yield db
    finally:
        db.close()

# router
@app.get("/students", response_model=List[StudentOut])
async def get_students(db : Session = Depends(get_db)):
    students = db.query(StudentEntity).all()
    return students

@app.post("/students", response_model=StudentOut)
async def create_student(student: StudentCreate, db : Session = Depends(get_db)):
    student_entity = StudentEntity(
        name=student.name,
        age=student.age
    )
    db.add(student_entity)
    db.commit()
    db.refresh(student_entity)
    
    return student_entity



if __name__ == "__main__":
    uvicorn.run( "main:app" , reload = True)

