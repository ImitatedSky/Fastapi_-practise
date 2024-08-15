from fastapi import FastAPI , Path , Query
import uvicorn

from typing import Optional
from pydantic import BaseModel
from enum import Enum


app = FastAPI()

'''
title : str
gt : greater than
ge : greater than or equal
lt : less than
le : less than or equal
regex : 正則

Query 與 Path 類似，但是 Query 可以有預設值，而 Path 不行，
Quety 為查詢參數 | Path 為路徑參數
前面...代表必填
Query(1,p1,p2) -> 1 代表預設值
Query(...,p1,p2) -> ... 代表必填
alias='page-index' -> 別名 > 可以用page-index取代page_index > 由於python 不支援- 所以要用_
'''

@app.get('/user')
async def get_user(page_index:int = Query(default=1,  title = 'Page Index' , ge = 1 ,le = 100)):
    return {'page info': f'page_index={page_index}'}



@app.get('/users/{user_id}')
async def get_users(user_id:int = Path(..., title='user id',  ge=1 , le=100)):
    return {'user': f'user id is {user_id}'}

@app.get('/books/{book_name}')
async def get_books(book_name:str = Path(..., title='book name', min_length=3, max_length=10)):
    return {'book': f'book name is {book_name}'}

@app.get('/items/{item_no}')
async def get_items(item_no:str = Path(...,title="item No.",regex = '^[a-f]-[\\d]*$')):
    return {'item': f'item name is {item_no}'}





if __name__ == "__main__":
    uvicorn.run("main:app" , reload=True)

