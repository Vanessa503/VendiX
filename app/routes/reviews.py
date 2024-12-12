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
def read_reviews(db: Session = Depends(get_db)):
    return crud.get_reviews(db)

@router.post("/")
def add_review(user_id: int, product_name: str, rating: float, comment: str, db: Session = Depends(get_db)):
    return crud.create_review(db, user_id=user_id, product_name=product_name, rating=rating, comment=comment)
