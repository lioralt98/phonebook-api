from fastapi import HTTPException
from sqlmodel import SQLModel
from enums import PhoneNumberTypesEnum

def is_model_present(instance: SQLModel, detail: str):
    if not instance:
        raise HTTPException(status_code=404, detail=detail)

def is_type_present(type: str) -> bool:
    return type in set(key for key in PhoneNumberTypesEnum)