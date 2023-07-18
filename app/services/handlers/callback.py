from fastapi import FastAPI
from app.api.schemas.messages import MessageBodyModel

telegram_app = FastAPI()


@telegram_app.post("/webhook")
async def callback(event: MessageBodyModel):
    print(event)
