import os

from dotenv import load_dotenv

load_dotenv()
KAFKA_BROKER_URL = os.getenv('KAFKA_BROKER_URL')
RATING_TOPIC_NAME = os.getenv('RATING_TOPIC_NAME', "book_ratings")
CONSUMER_POLL_TIMEOUT = float(os.getenv('CONSUMER_POLL_TIMEOUT', 0.4))

COMMAND_TIMEOUT = int(os.getenv('COMMAND_TIMEOUT', 60))
