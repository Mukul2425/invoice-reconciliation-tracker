import time
from celery import Celery

celery_app = Celery(
    "invoice_tracker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)


@celery_app.task(name="dummy_task")
def dummy_task(message: str):
    print(f"[Celery Task] {message}")
    return f"Task received: {message}"

@celery_app.task(name="send_invoice_notification")
def send_invoice_notification(invoice_id: int, vendor_name: str):
    time.sleep(3)
    print(f"[Celery] New invoice created: ID={invoice_id}, Vendor={vendor_name}")
    return f"Notification sent for invoice {invoice_id}"
