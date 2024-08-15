from typing import Optional
from pydantic import BaseModel , Field
from enum import Enum


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


class Address(BaseModel):
    address:str = Field( default=...,examples=["敦化南路一段","敦化南路二段"])
    postcode:Optional[str] = Field(default = ... , examples=["106"])

class User(BaseModel):
    username:str = Field(default=...,min_length=3 )
    description:Optional[str] = Field( default = None , max_length=10 , ) 
    address:Address

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "Pat",
                "description": "who am I",
                "address": {
                    "address": "敦化南路九九九段",
                    "postcode": "1111"
                }
            }
        }
    }