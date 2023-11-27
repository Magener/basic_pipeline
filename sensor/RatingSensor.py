import json
from confluent_kafka.cimpl import Producer

from sensor.CSVLoader import generator_from_csv
from sensor.consts import RATINGS_FILE_PATH, KAFKA_BROKER_URL, RATING_TOPIC_NAME
from sensor.log import logger


producer_conf = {
    'bootstrap.servers': KAFKA_BROKER_URL
}

producer = Producer(producer_conf)

logger.info("User has been connected!")

for row in generator_from_csv(RATINGS_FILE_PATH):
    # TODO: readd sleep for time.
    #rating_rate = random.uniform(MIN_NEW_RATING_RATE, MAX_NEW_RATING_RATE)

    producer.produce(topic=RATING_TOPIC_NAME, value=json.dumps(row))
    logger.info(f"Rating has been sent! {row}")

#TODO: should I move flush to inside of the loop?
producer.flush()