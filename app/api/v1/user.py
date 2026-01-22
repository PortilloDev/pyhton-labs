from fastapi import APIRouter
from app.schemas.user import UserListResponse
from app.services.user_service import UserService

router = APIRouter()

@router.get("/user", response_model=UserListResponse)
async def getUser():
    service = UserService()
    result = await service.get_id()
    
    return UserListResponse(status=result.status)