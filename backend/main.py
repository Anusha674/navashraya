from fastapi import FastAPI
from database import engine

app = FastAPI(title="Navashraya API")


@app.get("/")
def home():
    return {
        "project": "Navashraya",
        "status": "running"
    }


@app.get("/database")
def database_test():
    try:
        with engine.connect() as connection:
            return {
                "database": "connected",
                "status": "success"
            }
    except Exception as e:
        return {
            "database": "connection failed",
            "error": str(e)
        }