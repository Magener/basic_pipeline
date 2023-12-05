import os

from dotenv import load_dotenv

load_dotenv()
KAFKA_BROKER_URL = os.getenv('KAFKA_BROKER_URL')
RATING_TOPIC_NAME = os.getenv('RATING_TOPIC_NAME', "book_ratings")
CONSUMER_POLL_TIMEOUT = float(os.getenv('CONSUMER_POLL_TIMEOUT', 0.4))
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT', 5432)

COMMAND_TIMEOUT = int(os.getenv('COMMAND_TIMEOUT', 60))
