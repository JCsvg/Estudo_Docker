from datetime import datetime, UTC
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {
        "message": "Welcome to Dockeryt!",
        "now": datetime.now(tz=UTC).isoformat(),
        "counter": 1
    }