from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from enum import Enum

class InvoiceStatus(str, Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    OVERDUE = "OVERDUE"

class InvoiceCreate(BaseModel):
    vendor_name: str
    amount: float

class InvoiceOut(BaseModel):
    id: int
    invoice_number: str
    vendor_name: str
    amount: float
    due_date: date
    status: InvoiceStatus
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True
