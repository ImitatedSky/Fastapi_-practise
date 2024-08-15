from fastapi import APIRouter
from routers.user import user_router


router = APIRouter()  # 修改变量名为 api
router.include_router(user_router, prefix='/prefix_user', tags=['Tag_user'])