import asyncio
import json
from dataclasses import asdict

from aiokafka import AIOKafkaConsumer

from receiver.MessageValidation import extract_rating_data
from receiver.consts import KAFKA_BROKER_URL, RATING_TOPIC_NAME
from receiver.log import logger
from receiver.postgresql.Review import commit_review


async def initialize_kafka_consumer():
    return AIOKafkaConsumer(
        RATING_TOPIC_NAME,
        loop=asyncio.get_event_loop(),
        bootstrap_servers=KAFKA_BROKER_URL
    )


async def consume_messages():
    consumer = await initialize_kafka_consumer()

    await consumer.start()

    try:
        async for message in consumer:
            rating_data = json.loads(message.value)
            transformed_rating = extract_rating_data(rating_data).apply_transformation()
            await commit_review(**asdict(transformed_rating))
            logger.info(f"Saved in DB: {transformed_rating}")
    finally:
        await consumer.stop()


async def main():
    await consume_messages()


if __name__ == "__main__":
    asyncio.run(main())
