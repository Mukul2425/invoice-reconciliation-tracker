from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DisputeBase(BaseModel):
    reason: str

class DisputeCreate(DisputeBase):
    invoice_id: int

class DisputeOut(DisputeBase):
    id: int
    created_at: datetime
    invoice_id: int

    class Config:
        from_attributes = True
