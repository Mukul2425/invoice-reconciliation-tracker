from sqlalchemy import Column, Integer, String, Float, Date, Enum as PgEnum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime, timedelta
import enum

class InvoiceStatus(str, enum.Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    OVERDUE = "OVERDUE"

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, unique=True, index=True)
    vendor_name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(PgEnum(InvoiceStatus), default=InvoiceStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    due_date = Column(Date, default=lambda: datetime.utcnow().date() + timedelta(days=30))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="invoices")
    disputes = relationship("Dispute", back_populates="invoice", cascade="all, delete-orphan")




