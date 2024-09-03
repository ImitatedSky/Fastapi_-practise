from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel, Field

from .base_modle import Base

class StudentEntity(Base):
    __tablename__ = "students"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[int] = mapped_column(String(128), nullable=False)
    age : Mapped[int] = mapped_column(Integer, nullable=False)


class StudentBase(BaseModel):
    name: str = Field(..., example="PC Pat")
    age: int

class StudentCreate(StudentBase):
    ...

class StudentOut(StudentBase):
    id: int = Field(..., example=1)
