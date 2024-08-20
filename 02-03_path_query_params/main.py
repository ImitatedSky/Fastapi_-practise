from fastapi import FastAPI
import uvicorn

from typing import Optional
from enum import Enum

app = FastAPI()

class FruitName(str , Enum):
    apple = 'apple'
    banana = 'banana'
    orange = 'orange'

'''
Optional 用來表示參數是可選的
'''

@app.get("/users")
async def get_users(page_index:int, page_size:int):
    return {'page info': f'page_index={page_index}, page_size={page_size}'}

@app.get("/users/{user_id}/friends")
async def get_user_friends(page_index:int , user_id:int, page_size:Optional[int]=10):
    return {'page info': f'page_index={page_index}, user_id={user_id}, page_size={page_size}'}

@app.get("/students")
async def get_students(page_index:Optional[int] = 1, page_size:Optional[int] = 10, sort_by:Optional[str]=None):
    return {'page info': f'page_index={page_index}, page_size={page_size}, sort_by={sort_by}'}


@app.get("/fruits/{fruit_name}")
async def read_item(fruit_name: FruitName):
    return {"fruit_name": fruit_name}


if __name__ == "__main__":
    uvicorn.run("main:app" , reload=True)

