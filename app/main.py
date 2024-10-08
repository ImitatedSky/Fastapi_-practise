import sys
import os
# 不清楚為何跑的時候有時找不到app module，所以加了這一行
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from app.routers import api
from app.config import settings
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    # return {"message": "Hello World",
    #         "APP_NAME": settings.APP_NAME,
    #         "APP_VERSION": settings.APP_VERSION,}
    return f"""
    Hello World 
    {settings.APP_NAME} 
    {settings.APP_VERSION}
    """
app.include_router(api.api_router)



# 執行uvicorn用
if __name__ == "__main__":
    #bash   uvicorn main:app --reload
    uvicorn.run("main:app" , reload=True) 