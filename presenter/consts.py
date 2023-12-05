import os

from dotenv import load_dotenv

load_dotenv()
BOOKS_PRESENTED = int(os.getenv('BOOKS_PRESENTED', 5))
API_ENDPOINT = os.getenv('API_ENDPOINT')
