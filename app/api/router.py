from fastapi import APIRouter
from app.api.v1 import health
from app.api.v1 import user

router = APIRouter()
router.include_router(health.router, tags=["health"])
router.include_router(user.router, tags=["user"])
