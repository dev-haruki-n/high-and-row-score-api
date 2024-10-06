from fastapi import FastAPI
from routers import user_api

app = FastAPI()

app.include_router(user_api.router)