from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum

class InvoiceStatus(str, Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    OVERDUE = "OVERDUE"

class InvoiceBase(BaseModel):
    invoice_number: str
    vendor_name: Optional[str] = None
    amount: float
    due_date: Optional[date] = None
    status: InvoiceStatus = InvoiceStatus.PENDING

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceOut(InvoiceBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
