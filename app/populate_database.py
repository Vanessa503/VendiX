import csv
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import SessionLocal, Base, engine
from app.models import User, Purchase, Review

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

# Função para popular o banco de dados
def populate_database():
    db: Session = SessionLocal()

    try:
        # Populando tabela de usuários
        with open('./data/users.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user = User(
                    id=int(row['id']),
                    name=row['nome'],
                    email=row['email'],
                )
                db.add(user)

        # Populando tabela de compras
        with open('./data/purchases.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                purchase = Purchase(
                    id=int(row['id']),
                    user_id=int(row['user_id']),
                    product_name=row['produto'],
                    price=float(row['valor']),
                )
                db.add(purchase)

        # Populando tabela de avaliações
        with open('./data/reviews.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                review = Review(
                    id=int(row['id']),
                    user_id=int(row['user_id']),
                    product_name=row['produto'],
                    rating=float(row['nota']),
                    comment=row['comentario'],
                )
                db.add(review)

        db.commit()
        print("Banco de dados populado com sucesso!")
    except Exception as e:
        db.rollback()
        print(f"Erro ao popular o banco de dados: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    populate_database()
