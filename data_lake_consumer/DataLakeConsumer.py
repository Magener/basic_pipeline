import pandas as pd
from confluent_kafka.cimpl import Consumer
from deltalake.writer import write_deltalake

from data_lake_consumer.MessageValidation import validate_message
from data_lake_consumer.consts import PATH_TO_DB, CONSUMER_CONF, KAFKA_BROKER_URL, CONSUMER_POLL_TIMEOUT
from data_lake_consumer.log import logger
from sensor.consts import RATING_TOPIC_NAME

consumer = Consumer(CONSUMER_CONF)
consumer.subscribe([RATING_TOPIC_NAME])

try:
    logger.info(f'Connected to {KAFKA_BROKER_URL}')
    while True:
        msg = consumer.poll(timeout=CONSUMER_POLL_TIMEOUT)

        if msg:
            validate_message(msg)

            content = msg.value().decode("utf-8")
            logger.info(f"Received message: {content}")

            new_data = {"incoming_data": content}
            data_arrived = pd.DataFrame(data=new_data, index=["message"])
            write_deltalake(PATH_TO_DB, data_arrived, mode="append")
finally:
    consumer.close()
