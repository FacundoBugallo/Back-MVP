from fastapi import FastAPI
from app.database import Base, engine

app = FastAPI()

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "API funcionando"}

