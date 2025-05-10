import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

#nos trae el .env
load_dotenv()

#utiliza el url del .env
DATABASE_URL = os.getenv("DATABASE_URL") 
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ⬇️ Esta función es necesaria para usar la base de datos con Depends en FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
