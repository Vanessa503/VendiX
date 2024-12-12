import csv
from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app.models import User, Purchase, Review

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

def populate_database():
    db: Session = SessionLocal()

    try:
        # Populando tabela de usuários
        with open('./data/users.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            reader.fieldnames = [header.replace('\ufeff', '').strip() for header in reader.fieldnames]  # Remove BOM
            print("Cabeçalhos users.csv corrigidos:", reader.fieldnames)  # Debug
            for row in reader:
                print("Linha lida users.csv:", row)  # Debug
                user = User(
                    id=int(row['id']),
                    name=row['nome'],
                    email=row['email'],
                )
                db.add(user)

        # Populando tabela de compras
        with open('./data/purchases.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            reader.fieldnames = [header.replace('\ufeff', '').strip() for header in reader.fieldnames]  # Remove BOM
            print("Cabeçalhos purchases.csv corrigidos:", reader.fieldnames)  # Debug
            for row in reader:
                print("Linha lida purchases.csv:", row)  # Debug
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
            reader.fieldnames = [header.replace('\ufeff', '').strip() for header in reader.fieldnames]  # Remove BOM
            print("Cabeçalhos reviews.csv corrigidos:", reader.fieldnames)  # Debug
            for row in reader:
                print("Linha lida reviews.csv:", row)  # Debug
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
