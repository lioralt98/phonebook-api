from datetime import datetime
from typing import List, Optional
from pydantic import AfterValidator, ValidationInfo
from typing_extensions import Annotated
from sqlmodel import Field, SQLModel, Relationship

from enums import PhoneNumberTypesEnum
from config import settings

def inforce_phone_number_validity(v: str):
    if v.startswith("0"):
        return f"+{settings.DEFAULT_AREA_CODE}{v[1:]}"
    elif not v.startswith("+"):
        raise ValueError(f"phone number must start with +[some area code] or 0")
    return v

def check_name_is_alpha(v: str, info: ValidationInfo):
    if not v.isalpha():
        raise ValueError(f"{info.field_name} must contain only alphabetic characters")
    return v

def check_phone_number_type(v: str, info: ValidationInfo):
    v = v.lower()
    if not v.isalpha():
        raise ValueError("phone number type must be alphabetic")
    if not PhoneNumberTypesEnum.contains(v):
        raise ValueError(f"{v} not valid phone number type, select from [mobile, work, home, none]")
    return v
          

class MainModel(SQLModel):
    full_name: str
    phone_number: str
    phone_number_type: str

class ContactBase(SQLModel):
    first_name: Annotated[str, AfterValidator(check_name_is_alpha)]
    last_name: Annotated[str, AfterValidator(check_name_is_alpha)]
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
    first_name: Annotated[Optional[str], AfterValidator(check_name_is_alpha)] = None
    last_name: Annotated[Optional[str], AfterValidator(check_name_is_alpha)] = None

class PhoneNumberBase(SQLModel):
    phone_number: Annotated[str, AfterValidator(inforce_phone_number_validity)]
    phone_number_type: Annotated[str, AfterValidator(check_phone_number_type)] = Field(default=PhoneNumberTypesEnum.NONE)
    contact_id: int = Field(foreign_key="contacts.id")

class PhoneNumber(PhoneNumberBase, table=True):
    __tablename__: str = "phone_numbers"
    id: Optional[int] = Field(default=None, primary_key=True)
    contact: "Contact" = Relationship(back_populates="numbers")

class PhoneNumberCreate(PhoneNumberBase):
    pass

class PhoneNumberPublic(PhoneNumberBase):
    id: int
    phone_number_type: str

class PhoneNumberUpdate(PhoneNumberBase):
    phone_number: Annotated[Optional[str], AfterValidator(inforce_phone_number_validity)] = None
    phone_number_type: Annotated[str, AfterValidator(check_phone_number_type)] = PhoneNumberTypesEnum.NONE
    contact_id: Optional[int] = None