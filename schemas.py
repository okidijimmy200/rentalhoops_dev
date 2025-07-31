# schemas.py
from pydantic import BaseModel
from typing import Optional
from enum import Enum

class DeliveryStatus(str, Enum):
    pending = "pending"
    accepted = "accepted"
    en_route = "en_route"
    delivered = "delivered"
    confirmed = "confirmed"

class RequestModel(BaseModel):
    sender_site: str
    recipient_name: str
    address: str

class AcceptModel(BaseModel):
    delivery_id: int
    driver_id: int

class StatusUpdateModel(BaseModel):
    delivery_id: int
    new_status: DeliveryStatus

class ConfirmModel(BaseModel):
    delivery_id: int

class UserRole(str, Enum):
    client = "client"
    driver = "driver"
    admin = "admin"
