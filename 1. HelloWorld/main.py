from fastapi import FastAPI , Path , Query , Body
import uvicorn

from typing import Optional
from pydantic import BaseModel , Field
from enum import Enum


app = FastAPI()

@app.get("/helloworld")
async def hello_world():
    return {"Hello": "World"}  




if __name__ == "__main__":
    #bash   uvicorn main:app --reload
    uvicorn.run("main:app" , reload=True) 

