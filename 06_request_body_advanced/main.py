from fastapi import FastAPI , Path , Query , Body
import uvicorn

from typing import Optional , List
from pydantic import BaseModel , Field
from enum import Enum


app = FastAPI()

class Item(BaseModel):
    name:str
    length:int

class User(BaseModel):
    username:str
    description:Optional[str] = None

class User2(BaseModel):
    username:str = Field(default = ... , min_length = 3)
    description:Optional[str] = Field(None, max_length = 10)

class Address(BaseModel):
    city:str
    street:str

class User3(BaseModel):
    username:str
    description:Optional[str] = None
    address:Address

class Item2(BaseModel):
    name:str
    features:List[str] 

class Feature(BaseModel):
    name:str
    value:str
    
class Item3(BaseModel):
    name:str
    features:List[Feature]


@app.put("/carts/{cart_id}")
async def update_cart(cart_id:int , item:Item , user:User ):
    print(user.username)
    print(item.name)
    result_dict = {
        'cart_id': cart_id,
        "username" : user.username,
        "item_name": item.name,
    }
    return result_dict

@app.put("/carts_query/{cart_id}")
async def update_cart_query(cart_id:int , item:Item , user:User , count:int ):
    print(user.username)
    print(item.name)
    result_dict = {
        'cart_id': cart_id,
        "username" : user.username,
        "item_name": item.name,
        "count": count
    }
    return result_dict

@app.put("/carts_body/{cart_id}")
async def update_cart_body(cart_id:int , item:Item , user:User , count:int = Body(... , ge = 2) ):
    print(user.username)
    print(item.name)
    result_dict = {
        'cart_id': cart_id,
        "username" : user.username,
        "item_name": item.name,
        "count": count
    }
    return result_dict




@app.put("/carts2")
async def update_cart2( item:Item , user:User2 ):
    print(user.username)
    print(item.name)
    result_dict = {
        "username" : user.username,
        "item_name": item.name,
    }
    return result_dict



@app.put("/carts3")
async def update_cart3( item:Item , user:User3 ):
    print(user)
    result_dict = {
        "username" : user.username,
        "item_name": item.name,
        "city": user.address.city,
        "street": user.address.street
    }
    return result_dict




@app.put("/carts_list")
async def update_cart_list(  item:Item2 , user:User3 ):
    print(user)
    result_dict = {
        "username" : user.username,
        "item_name": item.name,
        "features": item.features
    }
    return result_dict


@app.put("/carts_list2")
async def update_cart_list2(  item:Item3 , user:User3 ):
    print(user)
    result_dict = {
        "username" : user.username,
        "item_name": item.name,
        "features": item.features
    }
    return result_dict


if __name__ == "__main__":
    uvicorn.run("main:app" , reload=True)

