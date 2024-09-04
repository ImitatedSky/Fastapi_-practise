from fastapi import FastAPI , Path , Query , Body , Cookie ,Header ,Request, Response , HTTPException , status , Depends
from fastapi.responses import JSONResponse
import uvicorn

from typing import Optional , List , Union
from pydantic import BaseModel , Field
from enum import Enum

from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from datetime import datetime , timedelta , timezone
from jose import JWTError , jwt


SECURITY_KEY = "abcdef123456"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token") 

class Token(BaseModel):
    # 回傳的資料
    access_token:str
    token_type:str


app = FastAPI()


def validate_user(username:str , password:str):
    if username == "Pat" and password == "1234":
        return username
    return None

def get_current_username(token:str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token , SECURITY_KEY , algorithms=[ALGORITHM])
        username = payload.get("username")
        if username is None:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Invalid authentication credentials",
                headers={"WWW-Authenticate":"Bearer"}
            )
    except JWTError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid authentication credentials",
            headers={"WWW-Authenticate":"Bearer"}
        )
    return username


@app.post('/token' , response_model=Token)
async def login(login_from:OAuth2PasswordRequestForm = Depends()):
    """
    用來取得token
    輸入帳號密碼，如果正確就回傳token
    user: Pat
    password: 1234
    """
    username = validate_user(login_from.username , login_from.password)
    
    if not username:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid user",
            headers={"WWW-Authenticate":"Bearer"}
        )
    
    token_expire = datetime.now(timezone.utc) + timedelta(minutes=300)
    token_data = {
        "username":username,
        "exp":token_expire
    }
    token = jwt.encode(token_data , SECURITY_KEY , algorithm=ALGORITHM)

    return Token(access_token = token,token_type = "bearer")


@app.get('/items')
async def get_items(username:str = Depends(get_current_username)):
    return {"current_user":username}


if __name__ == "__main__":
    #bash   uvicorn main:app --reload
    uvicorn.run("main:app" , reload=True) 

