from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import RequestModel, DeliveryStatus
from models import DeliveryRequest

router = APIRouter()

@router.post("/request")
def create_request(request: RequestModel, db: Session = Depends(get_db)):
    new_request = DeliveryRequest(
        sender_site=request.sender_site,
        recipient_name=request.recipient_name,
        address=request.address
    )
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request

@router.get("/requests")
def list_pending_requests(db: Session = Depends(get_db)):
    requests = db.query(DeliveryRequest).filter(DeliveryRequest.status == "pending").all()
    return requests

@router .post("/accept")
def accept_request(delivery_id: int, driver_id: int, db: Session = Depends(get_db)):
    delivery = db.query(DeliveryRequest).get(delivery_id)
    if delivery.status != DeliveryStatus.pending:
        raise HTTPException(status_code=400, detail="Already accepted")

    delivery.status = DeliveryStatus.ACCEPTED
    delivery.driver_id = driver_id
    db.commit()
    return {"message": "Job accepted"}

@router .patch("/status")
def update_status(delivery_id: int, new_status: str, db: Session = Depends(get_db)):
    delivery = db.query(DeliveryRequest).get(delivery_id)
    if new_status not in DeliveryStatus.__members__:
        raise HTTPException(status_code=400, detail="Invalid status")
    delivery.status = DeliveryStatus[new_status]
    db.commit()
    return {"message": f"Status updated to {new_status}"}

@router .post("/confirm")
def confirm_delivery(delivery_id: int, db: Session = Depends(get_db)):
    delivery = db.query(DeliveryRequest).get(delivery_id)
    if delivery.status != DeliveryStatus.DELIVERED:
        raise HTTPException(status_code=400, detail="Cannot confirm yet")
    delivery.status = DeliveryStatus.CONFIRMED
    db.commit()
    return {"message": "Delivery confirmed"}
