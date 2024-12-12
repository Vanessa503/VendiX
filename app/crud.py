from sqlalchemy.orm import Session
from . import models

# CRUD para usuários
def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, name: str, email: str):
    user = models.User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# CRUD para compras
def get_purchases(db: Session):
    return db.query(models.Purchase).all()

def create_purchase(db: Session, user_id: int, product_name: str, price: float):
    purchase = models.Purchase(user_id=user_id, product_name=product_name, price=price)
    db.add(purchase)
    db.commit()
    db.refresh(purchase)
    return purchase

# CRUD para avaliações
def get_reviews(db: Session):
    return db.query(models.Review).all()

def create_review(db: Session, user_id: int, product_name: str, rating: float, comment: str):
    review = models.Review(user_id=user_id, product_name=product_name, rating=rating, comment=comment)
    db.add(review)
    db.commit()
    db.refresh(review)
    return review
