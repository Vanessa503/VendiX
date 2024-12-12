from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .routes import users, purchases, reviews

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
