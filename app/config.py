import toml

toml_data = toml.load("../pyproject.toml")


class Config:

    TELEGRAM_TOKEN = toml_data['TELEGRAM_TOKEN']

    PORT_APP = 80
    HOST_URL = toml_data["server"]['HOST_URL']
    REPOSITORY = toml_data["repository"]['REPOSITORY']

    DEBUG = True
    DEBUG_URL = ''  # problem import

    TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/"
