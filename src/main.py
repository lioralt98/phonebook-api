from fastapi import FastAPI
import uvicorn

from .routers import contact_router, phone_number_router, main_router

app = FastAPI()

app.include_router(contact_router.contact_router)
app.include_router(phone_number_router.phone_number_router)
app.include_router(main_router.main_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)