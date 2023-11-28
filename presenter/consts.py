import os

from dotenv import load_dotenv

load_dotenv()
BOOKS_PRESENTED = int(os.getenv('BOOKS_PRESENTED'))