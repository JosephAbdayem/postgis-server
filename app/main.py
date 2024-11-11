from fastapi import FastAPI
from .db.database import engine, Base
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
