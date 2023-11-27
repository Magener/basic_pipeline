import json
from confluent_kafka.cimpl import Consumer, KafkaException

from receiver.consts import KAFKA_BROKER_URL, CONSUMER_CONF, RATING_TOPIC_NAME
from receiver.log import logger


def ensure_message_valid(msg) -> None:
    if msg.error() and msg.error().code() != KafkaException._PARTITION_EOF:
        raise SystemExit(msg.error())


consumer = Consumer(CONSUMER_CONF)
consumer.subscribe([RATING_TOPIC_NAME])

try:
    logger.info(f'Connected to {KAFKA_BROKER_URL}')
    while True:
        msg = consumer.poll(timeout=1.0)

        if msg is not None:
            ensure_message_valid(msg)
            rating_data = json.loads(msg.value().decode("utf-8"))
            logger.info(f"Rating data has been received: {rating_data}")
except SystemExit as e:
    logger.error(str(e))
finally:
    consumer.close()