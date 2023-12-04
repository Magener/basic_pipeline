import os

from dotenv import load_dotenv

load_dotenv()
PATH_TO_DB = os.getenv('PATH_TO_DB')
KAFKA_BROKER_URL = os.getenv('KAFKA_BROKER_URL')
RATING_TOPIC_NAME = os.getenv('RATING_TOPIC_NAME', "book_ratings")
CONSUMER_POLL_TIMEOUT = float(os.getenv('CONSUMER_POLL_TIMEOUT', 0.4))


CONSUMER_CONF = {
        'bootstrap.servers': KAFKA_BROKER_URL,
        'group.id': 'websocket-consumer-group'
    }