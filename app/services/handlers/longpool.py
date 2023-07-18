import time
import requests
from app.config import Config
from ..modules.longpool import send_message


def longpool():
    url = f'https://api.telegram.org/bot{Config.TELEGRAM_TOKEN}/getUpdates'
    offset = None

    while True:
        try:
            response = requests.get(url, params={'offset': offset}, timeout=30)
            json_response = response.json()

            if json_response['ok'] and len(json_response['result']) > 0:
                for result in json_response['result']:
                    # Обработка полученных сообщений
                    message = result['message']
                    chat_id = message['chat']['id']
                    text = message['text']
                    send_message(chat_id, text)

                # Установка нового значения offset для получения следующих сообщений
                last_update = json_response['result'][-1]
                offset = last_update['update_id'] + 1
        except requests.exceptions.RequestException as e:
            print('Произошла ошибка при получении обновлений:', e)
        time.sleep(0.5)
