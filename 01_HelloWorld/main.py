from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import List, Optional, Union

import uvicorn
from fastapi import (
    Body,
    Cookie,
    Depends,
    FastAPI,
    Header,
    HTTPException,
    Path,
    Query,
    Request,
    Response,
    status,
)
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, Select, String, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    sessionmaker,
)

app = FastAPI()


@app.get("/helloworld")
async def hello_world():
    return {"Hello": "World"}


if __name__ == "__main__":
    # bash   uvicorn main:app --reload
    uvicorn.run("main:app", reload=True)
