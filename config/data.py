import os
from dotenv import load_dotenv

load_dotenv()

class Data:
    """Данные для авторизации, которые подтягиваются из .env"""
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')