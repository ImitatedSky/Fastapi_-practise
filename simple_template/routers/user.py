from fastapi import APIRouter
from simple_template.model import User

user_router = APIRouter()

@user_router.post("/")
def helloworld():
    return {"Hello": "World"}


@user_router.post("/user0")
async def get_user(
    user: User
    ):

    result = {  
        user.username : user.phonenumber
    }
    return result