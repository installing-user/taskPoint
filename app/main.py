import asyncio
import threading
from config import Config
from fastapi import FastAPI
from services import longpool
from api.routes.telegram import create_routing
from api.schemas.webhook import TelegramWebHook


def main():
    if Config.DEBUG:
        longpool()
    else:
        app = FastAPI()
        create_routing(app)
        threading.Thread(target=asyncio.run,  args=(TelegramWebHook.check(),), daemon=True).start()


if __name__ == '__main__':
    main()
