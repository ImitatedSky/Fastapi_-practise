from fastapi import BackgroundTasks, FastAPI
import time
from datetime import datetime
import logging
import uvicorn

import asyncio

# 設置 logging 基本配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

async def print_log(param: str):
    # 0.5秒 在 terminal 輸出一次
    start_time = time.time()
    duration = float(param)  
    end_time = start_time + duration  # 持續param秒

    while time.time() < end_time:
        current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        logging.info(f"current_time: {current_time}")
        await asyncio.sleep(0.5)  # 暫停0.5秒
    print("Task completed")
    
@app.post("/start-task/n")
async def start_task(param: str, background_tasks: BackgroundTasks):
    await print_log(param)
    return {"message": "Task started in the background"}


@app.post("/start-task/")
async def start_task(param: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(print_log, param)
    return {"message": "Task started in the background"}

@app.post("/start-task/2")
async def start_task(param: str, background_tasks: BackgroundTasks):
    async def process( background_tasks: BackgroundTasks):
        background_tasks.add_task(print_log, param)
        print("process")
        return {"message": "in process"}
    
    await process(background_tasks)

    return {"message": "Task started in the background"}







if __name__ == "__main__":
    #bash   uvicorn main:app --reload
    uvicorn.run("main:app" , reload=True) 
