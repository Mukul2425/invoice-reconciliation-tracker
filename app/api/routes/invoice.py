from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.invoice import InvoiceCreate, InvoiceOut
from app.models.invoice import Invoice
from app.db.session import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.worker.tasks import send_invoice_reminder
from app.worker.tasks import send_invoice_reminder
from celery_worker import send_invoice_notification
from celery_worker import dummy_task

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import date, timedelta
import uuid

from app.schemas.invoice import InvoiceCreate, InvoiceOut
from app.models.invoice import Invoice
from app.db.session import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.worker.tasks import send_invoice_reminder
from celery_worker import send_invoice_notification, dummy_task

router = APIRouter(prefix="/invoices", tags=["Invoices"])

@router.post("/", response_model=InvoiceOut)
def create_invoice(
    invoice: InvoiceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_invoice = Invoice(
        invoice_number=str(uuid.uuid4())[:8],
        vendor_name=invoice.vendor_name,
        amount=invoice.amount,
        due_date=date.today() + timedelta(days=30),
        user_id=current_user.id
    )
    db.add(new_invoice)
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="Failed to create invoice")

    db.refresh(new_invoice)

    send_invoice_notification.delay(new_invoice.id, new_invoice.vendor_name)
    send_invoice_reminder.delay(new_invoice.id)

    return new_invoice


@router.get("/", response_model=List[InvoiceOut])
def list_invoices(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Invoice).filter(Invoice.user_id == current_user.id).all()

@router.post("/trigger-dummy-task/")
def trigger_dummy_task(current_user: User = Depends(get_current_user)):
    dummy_task.delay("Hello from FastAPI")
    return {"message": "Dummy task triggered"}

@router.get("/test-task")
def run_task():
    dummy_task.delay("Hello from test endpoint")
    return {"message": "Test task sent to Celery!"}
