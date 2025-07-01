from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.invoice import Invoice, InvoiceStatus
from app.models.dispute import Dispute
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    invoices = db.query(Invoice).filter(Invoice.user_id == current_user.id).all()
    disputes = db.query(Dispute).join(Invoice).filter(Invoice.user_id == current_user.id).all()

    total_amount = sum(i.amount for i in invoices)
    total_paid = sum(i.amount for i in invoices if i.status == InvoiceStatus.PAID)
    overdue_count = sum(1 for i in invoices if i.status == InvoiceStatus.OVERDUE)

    return {
        "total_invoices": len(invoices),
        "total_amount": total_amount,
        "paid_amount": total_paid,
        "dispute_count": len(disputes),
        "overdue_invoices": overdue_count,
    }
