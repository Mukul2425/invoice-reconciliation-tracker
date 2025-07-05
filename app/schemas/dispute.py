from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DisputeBase(BaseModel):
    reason: str

from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class DisputeStatus(str, Enum):
    PENDING = "PENDING"
    RESOLVED = "RESOLVED"

class DisputeCreate(BaseModel):
    invoice_id: int
    reason: str

class DisputeOut(BaseModel):
    id: int
    invoice_id: int
    reason: str
    status: DisputeStatus
    created_at: datetime

    class Config:
        from_attributes = True
