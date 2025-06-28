from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()  # Load .env config

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Invoice Reconciliation & Dispute Tracker API is running 🚀"}
