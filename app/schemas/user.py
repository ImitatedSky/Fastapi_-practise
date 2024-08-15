from typing import Optional
from pydantic import BaseModel , Field

class User(BaseModel):
    username: str
    phonenumber: Optional[str] = None
