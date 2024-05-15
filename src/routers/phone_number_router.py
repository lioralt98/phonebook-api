from fastapi import APIRouter, Depends
from ..models.models import *
from ..utils import get_service
from ..service import Service

phone_number_router = APIRouter(
    prefix = "/phone_numbers"
)

@phone_number_router.get("/", response_model=list[PhoneNumberPublic])
async def get_phone_numbers(service: Service = Depends(get_service)):
    return await service.get_phone_numbers()

@phone_number_router.get("/{type}")
async def get_phone_numbers_by_type(type: str, service: Service = Depends(get_service)):
    return await service.get_phone_numbers_by_type(type)

@phone_number_router.get("/{id}", response_model=PhoneNumberPublic)
async def get_phone_number(id: int, service: Service = Depends(get_service)):
    return await service.get_phone_number(id)

@phone_number_router.post("/", response_model=PhoneNumberPublic)
async def create_phone_number(contact: PhoneNumberCreate, service: Service = Depends(get_service)):
    return await service.create_phone_number(contact)

@phone_number_router.patch("/{id}", response_model=PhoneNumberPublic)
async def update_phone_number(id: int, contact: PhoneNumberUpdate, service: Service = Depends(get_service)):
    return await service.update_phone_number(id, contact)

@phone_number_router.delete("/{id}")
async def delete_phone_number(id: int, service: Service = Depends(get_service)):
    return await service.delete_phone_number(id)