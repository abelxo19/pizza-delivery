from fastapi import FastAPI
from auth_route import auth_router
from order_route import order_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(order_router)