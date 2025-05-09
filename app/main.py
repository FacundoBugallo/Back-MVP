from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user  # importar router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "API funcionando"}
