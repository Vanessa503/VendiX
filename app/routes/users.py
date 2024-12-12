from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.post("/")
def add_user(name: str, email: str, db: Session = Depends(get_db)):
    return crud.create_user(db, name=name, email=email)
