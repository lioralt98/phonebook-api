from sqlmodel import create_engine, select

from .config import settings
from .repositories import phone_number_repository, contact_repository
from .models.models import *
from .exceptions import is_model_present

engine = create_engine(settings.POSTGRES_URL, echo=True)

class Service:

    def __init__(self, session):
        self.session = session
        self.phone_number_repository = phone_number_repository.PhoneNumberRepository(session)
        self.contact_repository = contact_repository.ContactRepository(session)

    async def create_contact(self, contact: ContactCreate) -> ContactPublic:
        return await self.contact_repository.create(contact)
    
    async def get_contacts(self) -> list[ContactPublic]:
        return await self.contact_repository.read_all()
    
    async def get_contact(self, id: int) -> ContactPublic:
        return await self.contact_repository.read(id)
    
    async def delete_contact(self, id: int):
        return await self.contact_repository.delete(id)
    
    async def update_contact(self, id: int, contact: ContactUpdate) -> ContactPublic:
        return await self.contact_repository.update(id, contact)
    
    async def create_phone_number(self, phone_number: PhoneNumberCreate) -> PhoneNumberPublic:
        phone_number.phone_number_type = phone_number.phone_number_type.lower()
        return await self.phone_number_repository.create(phone_number)
    
    async def get_phone_numbers(self) -> list[PhoneNumberPublic]:
        return await self.phone_number_repository.read_all()
    
    async def get_phone_number(self, id: int) -> PhoneNumberPublic:
        return await self.phone_number_repository.read(id)
    
    async def delete_phone_number(self, id: int):
        return await self.phone_number_repository.delete(id)
    
    async def update_phone_number(self, id: int, phone_number: PhoneNumberCreate) -> list[PhoneNumberPublic]:
        return await self.phone_number_repository.update(id, phone_number)
    
    async def get_phone_numbers_by_id(self, id: int) -> list[PhoneNumberPublic]:
        db_contact = self.contact_repository.read(id)
        is_model_present(db_contact, f"no contact with id: {id}")
        
        stmt = select(PhoneNumber).where(PhoneNumber.contact_id == id)
        res = self.session.exec(stmt)
        return res.all()
    
    async def get_phone_numbers_by_type(self, type: str):
        type = type.lower()
        PhoneNumberTypesEnum.contains(type)
        stmt = select(PhoneNumber).where(PhoneNumber.phone_number_type == type)
        res = self.session.exec(stmt)
        return res.all()
    
    async def show_all(self):
        stmt = select(Contact.first_name, Contact.last_name, PhoneNumber.phone_number, PhoneNumber.phone_number_type).\
                join_from(Contact, PhoneNumber)
        
        contacts = self.session.exec(stmt).all()
        
        full_name_contacts = [{
            "full_name": f"{contact.first_name} {contact.last_name}",
            "phone_number": contact.phone_number,
            "phone_number_type": contact.phone_number_type
        } for contact in contacts]
        
        return full_name_contacts
        
        
        
    
    