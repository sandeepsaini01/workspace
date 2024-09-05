import bcrypt
from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime, timedelta

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.User(
        username=user.username, 
        email=user.email, 
        hashed_password=hashed_password.decode('utf-8')
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_magazines(db: Session):
    return db.query(models.Magazine).all()

def get_plans(db: Session):
    return db.query(models.Plan).all()

def create_subscription(db: Session, user_id: int, magazine_id: int, plan_id: int):
    magazine = db.query(models.Magazine).filter(models.Magazine.id == magazine_id).first()
    plan = db.query(models.Plan).filter(models.Plan.id == plan_id).first()
    price = magazine.base_price * (1 - plan.discount)
    renewal_date = datetime.now() + timedelta(days=30 * plan.renewal_period)
    subscription = models.Subscription(
        user_id=user_id, 
        magazine_id=magazine_id, 
        plan_id=plan_id, 
        price=price, 
        renewal_date=renewal_date, 
        is_active=True
    )
    db.add(subscription)
    db.commit()
    db.refresh(subscription)
    return subscription
