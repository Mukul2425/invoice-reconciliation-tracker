from fastapi import FastAPI
from app.api.routes import user

app = FastAPI(title="Invoice Tracker API")

# Include user router
app.include_router(user.router)

