from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()  # Load .env config

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Invoice Reconciliation & Dispute Tracker API is running 🚀"}


from app.api.routes import user, auth, invoice, dispute, dashboard

app.include_router(user.router)
app.include_router(auth.router, tags=["Auth"])
app.include_router(invoice.router)
app.include_router(dispute.router)
app.include_router(dashboard.router, tags=["Dashboard"])
