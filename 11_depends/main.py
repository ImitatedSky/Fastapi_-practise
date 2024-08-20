from fastapi import FastAPI , Path , Query , Body , Cookie ,Header ,Request, Response , HTTPException , status , Depends
from fastapi.responses import JSONResponse
import uvicorn

from typing import Optional , List , Union
from pydantic import BaseModel , Field
from enum import Enum

# 所有api 都要授權於這個
# 全局的依賴
async def all_auth():
    print("all_auth")

app = FastAPI(dependencies=[Depends(all_auth)])


# 
async def verify_auth(api_token:Optional[str] = Header(default = None , alias = "api-token-header")):
    if not api_token:
        raise HTTPException(
            status_code = 400,
            detail = "Unauthorized"
        )

@app.get('/items')
async def get_items(page_index:Optional[int]=1 , page_size:Optional[int] = 10):
    return {"page_index":page_index , "page_limit":page_size}


# ---function---
def pageinfo_params(page_index:Optional[int]=1 , page_size:Optional[int] = 10):
    return {"page_index":page_index , "page_limit":page_size}

@app.get('/items_depends_func')
async def get_items_by_func(page_info:dict = Depends(pageinfo_params)):
    return {"page_index":page_info["page_index"] , "page_limit":page_info["page_limit"]}

@app.get('/users_depends_func',
         dependencies=[Depends(verify_auth)] # 依賴授權
         )
async def get_users_by_func(page_info:dict = Depends(pageinfo_params)):

    return {"page_index":page_info["page_index"] , "page_limit":page_info["page_limit"]}



# ---class---
class PageInfo:
    def __init__(self , page_index:Optional[int]=1 , page_size:Optional[int]=10):
        self.page_index = page_index
        self.page_size = page_size

@app.get('/items_depends_class')
async def get_items_by_class(page_info:PageInfo = Depends(PageInfo)):

    return {"page_index":page_info.page_index , "page_limit":page_info.page_size}

@app.get('/users_depends_class')
async def get_users_by_class(page_info:PageInfo = Depends()):

    return {"page_index":page_info.page_index , "page_limit":page_info.page_size}

# ---function with function---
def total_param(total_page: Optional[int] = 100):
    return total_page
def pageinfo_params2(page_index:Optional[int]=1 , page_size:Optional[int] = 10
                     , total_page: int = Depends(total_param)
                     ):
    return {"page_index":page_index , "page_limit":page_size , "total_page":total_page}

@app.get('/items_depends_func2')
async def get_items_by_func2(page_info:dict = Depends(pageinfo_params2)):
    return {"page_index":page_info["page_index"] , "page_limit":page_info["page_limit"] , "total_page":page_info["total_page"]}

# ---class with class---
class TotalPage:
    def __init__(self , total_page: Optional[int] = 100):
        self.total_page = total_page

class PageInfo2:
    def __init__(self , page_index:Optional[int]=1 , page_size:Optional[int]=10
                     , total_page: int = Depends(TotalPage)
                     ):
        self.page_index = page_index
        self.page_size = page_size
        self.total_page = total_page

@app.get('/items_depends_class2')
async def get_items_by_class2(page_info:PageInfo2 = Depends(PageInfo2)):

    return {"page_index":page_info.page_index , "page_limit":page_info.page_size , "total_page":page_info.total_page}








if __name__ == "__main__":
    #bash   uvicorn main:app --reload
    uvicorn.run("main:app" , reload=True) 

