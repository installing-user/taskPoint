from fastapi import FastAPI
from app.services.handlers.callback import telegram_app


def create_routing(app: FastAPI):
    app.include_router(telegram_app.router)
