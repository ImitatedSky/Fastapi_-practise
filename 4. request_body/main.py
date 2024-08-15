from fastapi import FastAPI
import uvicorn

from typing import Optional
from pydantic import BaseModel
from enum import Enum


app = FastAPI()

class FruitName(str , Enum):
    apple = 'apple'
    banana = 'banana'
    orange = 'orange'

class Gender(str , Enum):
    male = 'male'
    female = 'female'

class UserModel(BaseModel):
    username:str
    description : Optional[str] = "No description"
    gender : Gender

@app.post("/user/")
async def create_user(user_model : UserModel):

    print(user_model.username)
    user_dict = user_model.model_dump()
    
    return user_dict

@app.post("/user/{user_id}")
async def create_user(user_id : int ,user_model : UserModel):

    print(user_model.username)
    user_dict = user_model.model_dump()
    user_dict['id'] = user_id
    user_dict.update({'uptime': '2024-08-13'})
    
    return user_dict

@app.get("/fruits/{fruit_name}")
async def read_item(fruit_name: FruitName):
    return {"fruit_name": fruit_name}



if __name__ == "__main__":
    uvicorn.run("main:app" , reload=True)

