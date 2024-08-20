from fastapi import FastAPI , Path , Query , Body , Cookie , Header ,Response
import uvicorn

from typing import Optional , List , Union
from pydantic import BaseModel , Field
from enum import Enum

'''
Swagger UI 裡cookie是無法發送的
Cookie Header 不能使用下劃線
'''
app = FastAPI()


@app.post("/carts")
async def update_cart(*,
                      favorite_schema: Optional[str] = Cookie(default = None, alias="favorite-cookie"),
                      api_token: Union[str, None] = Header(default = None, alias="api-token")
                      ):
    result_dict = {
        "favorite_schema": favorite_schema,
        "api_token": api_token
    }
    return result_dict


# 利用response.set_cookie()來測試設定cookie
@app.post("/carts2")
async def test_response_cookie(
    response: Response,
    favorite_schema: Optional[str] = Cookie(default=None, alias="favorite-cookie"),
    api_token: Union[str, None] = Header(default=None, alias="api-token")
):
    result_dict = {
        "favorite_schema": favorite_schema,
        "api_token": api_token
    }
    response.set_cookie(key="favorite-cookie", value="dark")
    return result_dict





if __name__ == "__main__":
    #bash   uvicorn main:app --reload
    uvicorn.run("main:app" , reload=True) 

