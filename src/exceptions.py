from fastapi import HTTPException
from sqlmodel import SQLModel

def is_model_present(instance: SQLModel, detail: str):
    if not instance:
        raise HTTPException(status_code=404, detail=detail)