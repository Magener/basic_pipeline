import os

from dotenv import load_dotenv

load_dotenv()

RATINGS_FILE_PATH = os.getenv('RATINGS_FILE_PATH')
HOST_URL = os.getenv('URL')
HOST_PORT = os.getenv('PORT', 9000)
KAFKA_BROKER_URL = os.getenv('KAFKA_BROKER_URL')
RATING_TOPIC_NAME = os.getenv('RATING_TOPIC_NAME', "book_ratings")
MIN_NEW_RATING_RATE = float(os.getenv("MIN_NEW_RATING_RATE", 0.5))
MAX_NEW_RATING_RATE = float(os.getenv("MAX_NEW_RATING_RATE", 1))