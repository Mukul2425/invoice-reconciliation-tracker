from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.invoice import InvoiceCreate, InvoiceOut
from app.models.invoice import Invoice
from app.db.session import get_db
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/invoices/", response_model=InvoiceOut)
def create_invoice(
    invoice: InvoiceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_invoice = Invoice(**invoice.dict(), user_id=current_user.id)
    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
    return new_invoice

@router.get("/invoices/", response_model=List[InvoiceOut])
def list_invoices(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Invoice).filter(Invoice.user_id == current_user.id).all()
