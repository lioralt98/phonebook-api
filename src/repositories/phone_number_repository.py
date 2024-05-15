from sqlmodel import select, Session
from ..exceptions import is_model_present
from ..models.models import *

class PhoneNumberRepository:

    def __init__(self, session: Session):
        self.session = session

    async def create(self, phone_number: PhoneNumberCreate) -> PhoneNumberPublic:
        db_phone_number = PhoneNumber.model_validate(phone_number)
        self.session.add(db_phone_number)
        self.session.commit()
        self.session.refresh(db_phone_number)
        return db_phone_number
        
    
    async def read(self, id: int) -> PhoneNumberPublic:
        db_phone_number = self.session.get(PhoneNumber, id)
        is_model_present(db_phone_number, PhoneNumber)
        return db_phone_number
    
    async def read_all(self) -> list[PhoneNumberPublic]:
        db_phone_numbers =  self.session.exec(select(PhoneNumber))
        return db_phone_numbers.all()
    
    async def update(self, id: int, phone_number: PhoneNumberUpdate) -> PhoneNumberPublic:
        db_phone_number =  self.session.get(PhoneNumber, id)
        is_model_present(db_phone_number, PhoneNumber)
        data_phone_number = phone_number.model_dump(exclude_unset=True)
        db_phone_number.sqlmodel_update(data_phone_number)
        self.session.add(db_phone_number)
        self.session.commit()
        self.session.refresh(db_phone_number)
        return db_phone_number
    
    async def delete(self, id: int):
        db_phone_number = self.session.get(PhoneNumber, id)
        is_model_present(db_phone_number, PhoneNumber)
        self.session.delete(db_phone_number)
        self.session.commit()
        return {"success": True}