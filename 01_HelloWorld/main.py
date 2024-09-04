from fastapi import FastAPI , Path , Query , Body , Cookie ,Header ,Request, Response , HTTPException , status , Depends
from fastapi.responses import JSONResponse
import uvicorn

from typing import Optional , List , Union
from pydantic import BaseModel , Field
from enum import Enum

from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from datetime import datetime , timedelta , timezone
from jose import JWTError , jwt

from sqlalchemy import create_engine , Column , Integer , String, Select
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, Session

app = FastAPI()

@app.get("/helloworld")
async def hello_world():
    return {"Hello": "World"}  

if __name__ == "__main__":
    #bash   uvicorn main:app --reload
    uvicorn.run("main:app" , reload=True) 

