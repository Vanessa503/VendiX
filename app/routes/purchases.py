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
def read_purchases(db: Session = Depends(get_db)):
    return crud.get_purchases(db)

@router.post("/")
def add_purchase(user_id: int, product_name: str, price: float, db: Session = Depends(get_db)):
    return crud.create_purchase(db, user_id=user_id, product_name=product_name, price=price)
