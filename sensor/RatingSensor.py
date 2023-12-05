import json
import random
import time

from confluent_kafka.cimpl import Producer

from sensor.CSVLoader import generator_from_csv
from sensor.consts import RATINGS_FILE_PATH, KAFKA_BROKER_URL, RATING_TOPIC_NAME, MIN_NEW_RATING_RATE, \
    MAX_NEW_RATING_RATE
from sensor.log import logger


producer_conf = {
    'bootstrap.servers': KAFKA_BROKER_URL
}

producer = Producer(producer_conf)

for row in generator_from_csv(RATINGS_FILE_PATH):
    delay_between_ratings = random.uniform(MIN_NEW_RATING_RATE, MAX_NEW_RATING_RATE)

    producer.produce(topic=RATING_TOPIC_NAME, value="asdf")#json.dumps(row))
    logger.info(f"Rating has been sent! {row}")

    time.sleep(delay_between_ratings)

producer.flush()