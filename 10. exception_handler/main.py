from fastapi import FastAPI , Path , Query , Body , Cookie ,Header ,Request, Response , HTTPException , status
from fastapi.responses import JSONResponse
import uvicorn

from typing import Optional , List , Union
from pydantic import BaseModel , Field
from enum import Enum

users = {   
    "x": {"id":0},
    "a": {"id":1 , "username":"a" },
    "b": {"id":2 , "username":"b" ,"password":"bbb" },
    "c": {"id":3 , "username":"c" ,"password":"ccc" ,"description":"ccdec" },
    "d": {"id":4 , "username":"d" ,"password":"ddd" ,"description":"dddec" ,"address":"ddadd" },
    "e": {"id":5 , "username":"e" ,"password":"eee" ,"description":"eedec" ,"address":"eeadd" ,"fullname": "I am Ironman"}
}


app = FastAPI()

class UserBase(BaseModel):
    id:Optional[int] = None
    username:str
    fullname:Optional[str] = None
    description:Optional[str] = None

class UserIn(UserBase):
    password:str

class UserOut(UserBase):
    pass

class UserNotFound(Exception):
    def __init__(self , username:str):
        self.username = username

class ErrorMessage(BaseModel):
    error_code:int
    message:str
    info:str

@app.post("/users", status_code=201 , response_model=UserOut)
async def create_user(user:UserIn):
    user_dict = user.model_dump()
    user_dict.update({"id":100})

    return user_dict

@app.post("/user2" ,status_code = 201, response_model=UserOut , 
          responses = {
                400: {"model": ErrorMessage},
                401 : {"model": ErrorMessage},
          })
async def create_user2(user:UserIn):
    if users.get(user.username, None):
        error_msg = ErrorMessage(error_code = 400 , message = f'{user.username} already exists' , info = "sdfsdofsjdifjos")
        return JSONResponse(status_code=400 , content = error_msg.model_dump())
    
    user_dict = user.model_dump()
    user_dict.update({"id":100})
    return user_dict




@app.get("/user/{username}" , response_model=UserOut)
async def read_user(username:str):
    user = users.get(username,None)

    if user:
        return user
    # raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"{username} not found")
    raise UserNotFound(username)





@app.exception_handler(UserNotFound)
async def user_not_found_exception_handler(request : Request , exc : UserNotFound):
    return JSONResponse(
        status_code = 404,
        content = {
            "error_code":404,
            "message" : f'{exc.username} not found',
            "info" : "sdfsdofsjdifjos",
            }
        )


if __name__ == "__main__":
    #bash   uvicorn main:app --reload
    uvicorn.run("main:app" , reload=True) 

