from fastapi import APIRouter ,Depends
from simple_template.model import User

user_router = APIRouter()

@user_router.post("/")
def helloworld():
    return {"Hello": "World"}

# 加上response_model=User，會自動檢查是否符合User的格式
@user_router.post("/user0", response_model=User)
async def get_user(user: User):

    result = {  
        user.username : user.phonenumber
    }
    return result

@user_router.get("/user_depends")
async def test_depends(user: User = Depends(User)):
    return user