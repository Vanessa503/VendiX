from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from .database import SessionLocal
from .routes import users, purchases, reviews
from . import crud

app = FastAPI()

# Incluindo as rotas
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(purchases.router, prefix="/purchases", tags=["purchases"])
app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])

# Rota para o dashboard (HTML básico)
@app.get("/", response_class=HTMLResponse)
def read_dashboard():
    with open("./app/static/dashboard.html", "r") as f:
        return f.read()

# Rota para fornecer dados ao dashboard
@app.get("/dashboard-data/")
def get_dashboard_data(db: Session = Depends(SessionLocal)):
    total_users = len(crud.get_users(db))
    total_purchases = len(crud.get_purchases(db))
    total_reviews = len(crud.get_reviews(db))
    avg_rating = sum([review.rating for review in crud.get_reviews(db)]) / total_reviews if total_reviews > 0 else 0

    return {
        "total_users": total_users,
        "total_purchases": total_purchases,
        "total_reviews": total_reviews,
        "avg_rating": round(avg_rating, 2)
    }
