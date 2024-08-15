from fastapi import APIRouter

from app import schemas


router = APIRouter()

@router.post("/items/" , response_model=schemas.Item)
async def create_item(item:schemas.Item):
    return item

@router.post("/items/{item_id}" , response_model=schemas.Item)
async def read_item(item_id:int, Item:schemas.Item):
    result = {  
        'name' : Item.name,
        'description' : Item.description,
        'price' : Item.price,
        'tax' : Item.tax,
        'item_id' : item_id
    }
    return result