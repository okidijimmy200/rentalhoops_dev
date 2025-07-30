from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from schemas import DeliveryStatus

class DeliveryRequest(Base):
    __tablename__ = "delivery_requests"

    id = Column(Integer, primary_key=True)
    sender_site = Column(String)
    recipient_name = Column(String)
    address = Column(String)
    status = Column(Enum(DeliveryStatus), default=DeliveryStatus.pending)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=True)

    driver = relationship("Driver", back_populates="deliveries")

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String, unique=True)

    deliveries = relationship("DeliveryRequest", back_populates="driver")
