from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.dispute import DisputeCreate, DisputeOut
from app.models.dispute import Dispute
from app.models.invoice import Invoice
from app.db.session import get_db
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter()

# @router.post("/dispute/", response_model=DisputeOut)
# app/api/routes/dispute.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.dispute import DisputeCreate
from app.models.dispute import Dispute
from app.models.invoice import Invoice
from app.db.session import get_db
from app.core.auth import get_current_user
from app.models.user import User

@router.post("/disputes/")
def create_dispute(
    dispute: DisputeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Verify that the invoice exists and belongs to the user
    invoice = db.query(Invoice).filter(
        Invoice.id == dispute.invoice_id,
        Invoice.user_id == current_user.id
    ).first()

    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found or unauthorized")

    new_dispute = Dispute(**dispute.dict())
    db.add(new_dispute)
    db.commit()
    db.refresh(new_dispute)
    return new_dispute



@router.get("/dispute/", response_model=List[DisputeOut])
def list_disputes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Dispute).join(Invoice).filter(Invoice.user_id == current_user.id).all()
