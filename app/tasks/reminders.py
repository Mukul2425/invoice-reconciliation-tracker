# app/tasks/reminders.py

from datetime import date
from celery import shared_task
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.invoice import Invoice, InvoiceStatus

@shared_task
def send_due_invoice_reminders():
    db: Session = SessionLocal()
    today = date.today()
    due_invoices = db.query(Invoice).filter(
        Invoice.due_date <= today,
        Invoice.status == InvoiceStatus.PENDING
    ).all()

    for invoice in due_invoices:
        print(f"[Reminder] Invoice {invoice.invoice_number} is due for vendor {invoice.vendor_name}")

    db.close()
