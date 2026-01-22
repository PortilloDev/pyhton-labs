from fastapi import APIRouter

from app.schemas.health import HealthResponse
from app.services.health_service import HealthService

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
async def health_check():
    service = HealthService()
    result = await service.get_status()
    
    return HealthResponse(status=result.status)