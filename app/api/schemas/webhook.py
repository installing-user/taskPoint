import httpx
from enum import Enum
from app.config import Config
from httpx import AsyncClient
from app.tracaback.webhook import WebhookSetError, WebhookGetError,  WebhookNotDelete


class WebhookMethods(Enum):
    setWebhook = "setWebhook"
    getWebhookInfo = "getWebhookInfo"
    deleteWebhook = "deleteWebhook"


class WebhookOtherMethods(Enum):
    successful = 200
    failed = 404


class TelegramWebHook:

    @classmethod
    async def check(cls):

        host_url = Config.HOST_URL
        status_code: int = await cls._get_webhook()

        if status_code == WebhookOtherMethods.failed.value:
            await cls._set_webhook(host_url)
        else:
            await cls._delete_webhook()
            await cls._set_webhook(host_url)

    @staticmethod
    async def _set_webhook(host_url: Config.HOST_URL) -> WebhookOtherMethods.successful.value:
        async with AsyncClient() as client:
            payload = {"url": f"{host_url}/webhook"}
            request = await client.post(f"{Config.TELEGRAM_API_URL}{WebhookMethods.setWebhook.value}", json=payload)

            status_code: int = request.status_code

            try:
                request.raise_for_status()
                if status_code == WebhookOtherMethods.successful.value:
                    if Config.DEBUG:
                        print(f"Webhook set successfully: {host_url}")
                    return status_code
            except httpx.HTTPStatusError as error:
                raise WebhookSetError.print_error(error)

    @staticmethod
    async def _get_webhook() -> WebhookOtherMethods.successful.value | WebhookOtherMethods.failed.value:
        async with AsyncClient() as client:
            request = await client.post(f"{Config.TELEGRAM_API_URL}{WebhookMethods.getWebhookInfo.value}")
            status_code: int = request.status_code

            try:
                request.raise_for_status()
                if status_code == WebhookOtherMethods.successful.value or status_code == WebhookOtherMethods.failed.value:
                    return status_code
            except httpx.HTTPStatusError as error:
                raise WebhookGetError.print_error(error)

    @staticmethod
    async def _delete_webhook() -> WebhookOtherMethods.successful.value:
        async with AsyncClient() as client:
            payload = {"drop_pending_updates": True}
            request = await client.post(f"{Config.TELEGRAM_API_URL}{WebhookMethods.deleteWebhook.value}", json=payload)

            status_code: int = request.status_code

            try:
                request.raise_for_status()
                if status_code == WebhookOtherMethods.successful.value:
                    return status_code
            except httpx.HTTPStatusError as error:
                raise WebhookNotDelete.print_error(error)
