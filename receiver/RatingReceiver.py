import json
from confluent_kafka.cimpl import Consumer

from receiver.PostgresConnection import PostgresConnection
from receiver.consts import KAFKA_BROKER_URL, CONSUMER_CONF, RATING_TOPIC_NAME, CONSUMER_POLL_TIMEOUT
from receiver.log import logger
from receiver.postgresql.Review import commit_review


def validate_message(msg) -> None:
    if msg.error():
        raise RuntimeError(msg.error())


consumer = Consumer(CONSUMER_CONF)
consumer.subscribe([RATING_TOPIC_NAME])

try:
    logger.info(f'Connected to {KAFKA_BROKER_URL}')
    while True:
        msg = consumer.poll(timeout=CONSUMER_POLL_TIMEOUT)

        if msg:
            validate_message(msg)
            rating_data = json.loads(msg.value())
            #TODO: ensure type of json fields beforehand
            commit_review(int(rating_data["User-ID"]), rating_data["ISBN"], int(rating_data["Book-Rating"]))
            logger.info(f"Saved in DB: {rating_data}")
except RuntimeError as e:
    logger.error(str(e))
finally:
    consumer.close()

PostgresConnection().close()