from sqlmodel import Session
from .service import Service, engine

async def get_service():
    with Session(engine) as session:
        yield Service(session)