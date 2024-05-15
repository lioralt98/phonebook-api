from sqlmodel import select, Session
from ..models.models import *
from ..exceptions import is_model_present

class ContactRepository:

    def __init__(self, session: Session):
        self.session = session

    async def create(self, contact: ContactCreate) -> ContactPublic:
        db_contact = Contact.model_validate(contact)
        self.session.add(db_contact)
        self.session.commit()
        self.session.refresh(db_contact)
        return db_contact
    
    async def read(self, id: int) -> ContactPublic:
        db_contact = self.session.get(Contact, id)
        is_model_present(db_contact, Contact.__name__)
        return db_contact
    
    async def read_all(self) -> list[ContactPublic]:
        db_contacts = self.session.exec(select(Contact))
        return db_contacts.all()
    
    async def update(self, id: int, contact: ContactUpdate) -> ContactPublic:
        db_contact =  self.session.get(Contact, id)
        is_model_present(db_contact, Contact)
        data_contact = contact.model_dump(exclude_unset=True)
        db_contact.sqlmodel_update(data_contact)
        self.session.add(db_contact)
        self.session.commit()
        self.session.refresh(db_contact)
        return db_contact
    
    async def delete(self, id: int):
        db_contact = self.session.get(Contact, id)
        is_model_present(db_contact, Contact)
        self.session.delete(db_contact)
        self.session.commit()
        return {"success": True}
        


    
