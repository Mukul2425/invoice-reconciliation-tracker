# app/models/invoice.py

from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum

class InvoiceStatus(str, enum.Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    OVERDUE = "OVERDUE"

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, unique=True, index=True, nullable=False)
    vendor_name = Column(String, index=True)
    amount = Column(Float, nullable=False)
    due_date = Column(Date)
    status = Column(Enum(InvoiceStatus), default=InvoiceStatus.PENDING)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="invoices")
    # Add inside Invoice class
    disputes = relationship("Dispute", back_populates="invoice")

