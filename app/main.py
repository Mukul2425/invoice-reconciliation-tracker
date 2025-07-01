from fastapi import FastAPI
from app.api.routes import user

app = FastAPI(title="Invoice Tracker API")

# Include user router
app.include_router(user.router)

from fastapi import FastAPI
from app.api.routes import user, auth

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router, tags=["Auth"])

