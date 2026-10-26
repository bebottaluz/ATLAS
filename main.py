from fastapi import FastAPI
from routers.home import router as home_router

app = FastAPI(title="ATLAS API")

app.include_router(home_router)