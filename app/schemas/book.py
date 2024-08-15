from typing import Optional
from pydantic import BaseModel , Field

class Item(BaseModel):
    name:str
    description:Optional[str] = Field(None , title="description of the item" , max_length=300)
    price: float
    tax: Optional[float] = None