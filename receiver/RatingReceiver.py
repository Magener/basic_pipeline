import json
from confluent_kafka.cimpl import Consumer

from receiver.consts import KAFKA_BROKER_URL
from receiver.log import logger

consumer_conf = {
        'bootstrap.servers': KAFKA_BROKER_URL,
        'group.id': 'websocket-consumer-group'
    }

consumer = Consumer(consumer_conf)

# Subscribe to Kafka topic
topic = 'book_ratings'  # Replace with your Kafka topic
consumer.subscribe([topic])


#TODO: refactor
try:
    logger.info(f'Connected to {KAFKA_BROKER_URL}')
    while True:
        msg = consumer.poll(timeout=1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == -1:
                print("some error")
                continue
            else:
                print(msg.error())
                break

        rating_data = json.loads(msg.value().decode('utf-8'))

        logger.info(f"Rating data has been received: {rating_data}")

finally:
    # Close Kafka consumer on exit
    consumer.close()
