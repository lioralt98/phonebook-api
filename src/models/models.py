from datetime import datetime
from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from enums import PhoneNumberTypesEnum


class MainModel(SQLModel):
    full_name: str
    phone_number: str
    phone_number_type: str

class ContactBase(SQLModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None

class Contact(ContactBase, table=True):
    __tablename__: str = "contacts"
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = datetime.now()
    numbers: list["PhoneNumber"] = Relationship(back_populates="contact", sa_relationship_kwargs={"cascade": "delete"})

class ContactCreate(ContactBase):
        pass

class ContactPublic(ContactBase):
    id: int
    numbers: List["PhoneNumber"]
    created_at: datetime

class ContactUpdate(ContactBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class PhoneNumberBase(SQLModel):
    phone_number: str
    phone_number_type: str = Field(default=PhoneNumberTypesEnum.NONE)
    contact_id: int = Field(foreign_key="contacts.id")

class PhoneNumber(PhoneNumberBase, table=True):
    __tablename__: str = "phone_numbers"
    id: Optional[int] = Field(default=None, primary_key=True)
    contact: "Contact" = Relationship(back_populates="numbers")

class PhoneNumberCreate(PhoneNumberBase):
    pass

class PhoneNumberPublic(PhoneNumberBase):
    id: int

class PhoneNumberUpdate(PhoneNumberBase):
    phone_number: Optional[str] = None
    phone_number_type: Optional[str] = None
    contact_id: Optional[int] = None