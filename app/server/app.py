from fastapi import FastAPI
from .routes.manager import router as ManagerRouter

app = FastAPI()

app.include_router(ManagerRouter, tags=["Manager"], prefix="/manager")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
