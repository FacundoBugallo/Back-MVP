from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user, income, expense, auth



app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(expense.router)
app.include_router(user.router)
app.include_router(income.router)  
@app.get("/")
def read_root():
    return {"message": "API funcionando"}
