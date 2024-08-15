import sys
import os
# 不清楚為何跑的時候有時找不到app module，所以加了這一行
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi import FastAPI
from simple_template.api import router
import uvicorn

app = FastAPI()

app.include_router(router)




# 執行uvicorn用
if __name__ == "__main__":
    #bash   uvicorn main:app --reload
    uvicorn.run("main:app" , reload=True) 