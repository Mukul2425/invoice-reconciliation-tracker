# app/models/invoice.py

from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum

class InvoiceStatus(str, enum.Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    OVERDUE = "OVERDUE"

from sqlalchemy import Column, Integer, String, Float, Date, Enum as PgEnum, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from datetime import timedelta, date
import uuid

from app.db.base_class import Base
from app.models.user import User
from app.schemas.invoice import InvoiceStatus

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, unique=True, index=True, default=lambda: str(uuid.uuid4())[:8])
    vendor_name = Column(String, index=True, nullable=False)
    amount = Column(Float, nullable=False)
    due_date = Column(Date, default=lambda: date.today() + timedelta(days=30))
    status = Column(PgEnum(InvoiceStatus), default=InvoiceStatus.PENDING)
    created_at = Column(DateTime, server_default=func.now())

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="invoices")
    disputes = relationship("Dispute", back_populates="invoice")  # ✅ Add this



