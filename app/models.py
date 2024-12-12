from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    creation_date = Column(DateTime, default=datetime.utcnow)  # Adiciona a coluna data_criacao

    purchases = relationship("Purchase", back_populates="user")
    reviews = relationship("Review", back_populates="user")

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_name = Column(String, index=True)
    price = Column(Float)
    purchase_date = Column(DateTime, default=datetime.utcnow)  # Adiciona a coluna data_compra

    user = relationship("User", back_populates="purchases")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_name = Column(String)
    rating = Column(Float)
    comment = Column(String)
    review_date = Column(DateTime, default=datetime.utcnow)  # Adiciona a coluna data_avaliacao

    user = relationship("User", back_populates="reviews")
