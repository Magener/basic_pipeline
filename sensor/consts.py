import os

from dotenv import load_dotenv

load_dotenv()

RATINGS_FILE_PATH = os.getenv('RATINGS_FILE_PATH')
HOST_URL = os.getenv('URL')
HOST_PORT = os.getenv('PORT')
MIN_NEW_RATING_RATE = 0.5
MAX_NEW_RATING_RATE = 2