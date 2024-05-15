from fastapi import APIRouter, Depends
from ..models.models import *
from ..utils import get_service
from ..service import Service

main_router = APIRouter()

@main_router.get("/", response_model=list[MainModel])
async def get_contacts(service: Service = Depends(get_service)):
    return await service.show_all()