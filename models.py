from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from schemas import DeliveryStatus, UserRole

class DeliveryRequest(Base):
    __tablename__ = "delivery_requests"

    id = Column(Integer, primary_key=True)
    sender_site = Column(String)
    recipient_name = Column(String)
    address = Column(String)
    status = Column(Enum(DeliveryStatus), default=DeliveryStatus.pending)
    driver_id = Column(String, ForeignKey("users.id"), nullable=True)

    driver = relationship("Users", back_populates="deliveries")

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String, unique=True)
    role = Column(Enum(UserRole), default=UserRole.client)

    deliveries = relationship("DeliveryRequest", back_populates="users")
