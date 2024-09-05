from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class Magazine(BaseModel):
    id: int
    name: str
    description: str
    base_price: float

    class Config:
        orm_mode = True

class Plan(BaseModel):
    id: int
    title: str
    description: str
    renewal_period: int
    tier: int
    discount: float

    class Config:
        orm_mode = True

class Subscription(BaseModel):
    id: int
    user_id: int
    magazine_id: int
    plan_id: int
    price: float
    renewal_date: date
    is_active: bool

    class Config:
        orm_mode = True
