import json

from confluent_kafka.cimpl import Consumer

from receiver.MessageValidation import validate_message, extract_rating_data
from receiver.PostgresConnection import PostgresConnection
from receiver.consts import KAFKA_BROKER_URL, CONSUMER_CONF, RATING_TOPIC_NAME, CONSUMER_POLL_TIMEOUT
from receiver.log import logger
from receiver.postgresql.Review import commit_review

consumer = Consumer(CONSUMER_CONF)
consumer.subscribe([RATING_TOPIC_NAME])

try:
    logger.info(f'Connected to {KAFKA_BROKER_URL}')
    while True:
        msg = consumer.poll(timeout=CONSUMER_POLL_TIMEOUT)

        if msg:
            validate_message(msg)
            rating_data = json.loads(msg.value())
            commit_review(*extract_rating_data(rating_data))
            logger.info(f"Saved in DB: {rating_data}")
finally:
    consumer.close()
    PostgresConnection().close()