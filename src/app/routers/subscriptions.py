from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from datetime import datetime

router = APIRouter()

@router.post("/subscribe", response_model=schemas.Subscription)
def subscribe(magazine_id: int, plan_id: int, user_id: int, db: Session = Depends(get_db)):
    subscription = crud.create_subscription(db, user_id, magazine_id, plan_id)
    return subscription
