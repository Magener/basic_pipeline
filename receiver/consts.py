import os

from dotenv import load_dotenv

load_dotenv()
KAFKA_BROKER_URL = os.getenv('KAFKA_BROKER_URL')
RATING_TOPIC_NAME = os.getenv('RATING_TOPIC_NAME')



CONSUMER_CONF = {
        'bootstrap.servers': KAFKA_BROKER_URL,
        'group.id': 'websocket-consumer-group'
    }