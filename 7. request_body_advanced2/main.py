from fastapi import FastAPI , Path , Query , Body
import uvicorn

from typing import Optional
from pydantic import BaseModel , Field
from enum import Enum


app = FastAPI()


@app.put("/users")
async def update_user(user:User):
    user_dict = user.model_dump()
    return user_dict

@app.put("/users/{user_id}")
async def update_user(*,user_id:int , user:User , count:int = Body(default = ...,gt=0 , examples=[9] )):
    result_dict = {
        "user_id": user_id,
        "username": user.username,
        "description": user.description,
        "address": user.address,
        "count": count
    }
    return result_dict


if __name__ == "__main__":
    uvicorn.run("main:app" , reload=True) 

