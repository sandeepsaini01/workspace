from fastapi import FastAPI
from .database import engine, Base
from .routers import users, magazines, subscriptions

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(users.router, prefix="/users")
app.include_router(magazines.router, prefix="/magazines")
app.include_router(subscriptions.router, prefix="/subscriptions")
