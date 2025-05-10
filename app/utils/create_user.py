from sqlalchemy.orm import Session
from app import models, auth
from app.models import User
from app.database import SessionLocal

def create_user():
    db: Session = SessionLocal()
    user = User(
        name="Facundo",
        email="face1@face.com",
        password_hash=auth.hash_password("face1")
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    print("Usuario creado con éxito:", user.email)

if __name__ == "__main__":
    create_user()
