from fastapi import FastAPI , Path , Query , Body , Cookie ,Header , Response
import uvicorn

from typing import Optional , List , Union
from pydantic import BaseModel , Field
from enum import Enum

'''
response_model 用來檢查回傳的格式
像下面 就不會回傳password. description 其他東西
 
但x 因為少了username ,所以會錯誤訊息,除非加上預設值,例如description

response_model_exclude = ["password","description"]  #輸出不回傳password,description
response_model_include = ["username"]  //輸出只回傳username
response_model_exclude_unset = True  //只回傳有值的
'''

users = {   
    # "x": {"id":0},
    "a": {"id":1 , "username":"a" },
    "b": {"id":2 , "username":"b" ,"password":"bbb" },
    "c": {"id":3 , "username":"c" ,"password":"ccc" ,"description":"ccdec" },
    "d": {"id":4 , "username":"d" ,"password":"ddd" ,"description":"dddec" ,"address":"ddadd" },
    "e": {"id":5 , "username":"e" ,"password":"eee" ,"description":"eedec" ,"address":"eeadd" ,"fullname": "I am Ironman"}
}

class UserOut(BaseModel):
    id : int
    username : str 
    description : Optional[str] = "it's default description"


app = FastAPI()

@app.get("/user/{username}" , response_model=UserOut , response_model_exclude_unset=True)
async def read_user(username:str):
    return users.get(username,{})

@app.get("/user" , response_model = List[UserOut])
async def get_user():
    return users.values()



if __name__ == "__main__":
    #bash   uvicorn main:app --reload
    uvicorn.run("main:app" , reload=True) 
