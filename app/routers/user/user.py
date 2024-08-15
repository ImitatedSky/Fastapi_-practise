from fastapi import APIRouter

from app import schemas

router = APIRouter()

@router.post("/user")
async def get_user(
    user: schemas.User
    ):

    result = {  
        user.username : user.phonenumber
    }
    return result