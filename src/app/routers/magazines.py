from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/magazines", response_model=list[schemas.Magazine])
def get_magazines(db: Session = Depends(get_db)):
    return crud.get_magazines(db)
