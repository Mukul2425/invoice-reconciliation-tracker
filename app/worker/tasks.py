# app/worker/tasks.py

from app.worker.celery_worker import celery_app
import time

@celery_app.task
def send_invoice_reminder(invoice_id: int):
    # Replace this with actual email logic
    print(f"Sending reminder for invoice {invoice_id}")
    time.sleep(2)
    print(f"Reminder sent for invoice {invoice_id}")
    return f"Reminder sent for invoice {invoice_id}"
