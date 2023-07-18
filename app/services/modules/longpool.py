import requests
from app.config import Config


def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{Config.TELEGRAM_TOKEN}/sendMessage'

    data = {
        'chat_id': chat_id,
        'text': text
    }

    requests.post(url, data=data)
