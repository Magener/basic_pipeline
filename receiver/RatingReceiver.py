import json
from confluent_kafka.cimpl import Consumer

from receiver.consts import KAFKA_BROKER_URL, CONSUMER_CONF, RATING_TOPIC_NAME, CONSUMER_POLL_TIMEOUT
from receiver.log import logger


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
            logger.info(f"Rating data has been received: {rating_data}")
except SystemExit as e:
    logger.error(str(e))
finally:
    consumer.close()