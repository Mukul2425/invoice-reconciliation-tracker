from fastapi import FastAPI
from app.api.routes import user
from app.api.routes import user, auth, invoice, dispute  # 👈 import them

app = FastAPI(title="Invoice Tracker API")

# Include user router
app.include_router(user.router)

from fastapi import FastAPI
from app.api.routes import user, auth

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router, tags=["Auth"])
app.include_router(invoice.router)  # 👈 new
app.include_router(dispute.router)  # 👈 new

