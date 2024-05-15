from fastapi import APIRouter, Depends
from ..models.models import *
from ..utils import get_service
from ..service import Service

contact_router = APIRouter(
    prefix = "/contacts"
)

@contact_router.get("/", response_model=List[ContactPublic])
async def get_contacts(service: Service = Depends(get_service)):
    return await service.get_contacts()

@contact_router.get("/{id}", response_model=ContactPublic)
async def get_contact(id: int, service: Service = Depends(get_service)):
    return await service.get_contact(id)

@contact_router.post("/", response_model=ContactPublic)
async def create_contact(contact: ContactCreate, service: Service = Depends(get_service)):
    return await service.create_contact(contact)

@contact_router.patch("/{id}", response_model=ContactPublic)
async def update_contact(id: int, contact: ContactUpdate, service: Service = Depends(get_service)):
    return await service.update_contact(id, contact)

@contact_router.delete("/{id}")
async def delete_contact(id: int, service: Service = Depends(get_service)):
    return await service.delete_contact(id)

@contact_router.get("/{id}/phone_numbers")
async def get_phone_numbers_by_id(id: int, service: Service = Depends(get_service)):
    return await service.get_phone_numbers_by_id(id)