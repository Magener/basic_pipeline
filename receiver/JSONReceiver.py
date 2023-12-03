import asyncio
import json

from aiokafka import AIOKafkaConsumer

from receiver.MessageHandlingStrategy import MessageHandlingStrategy
from receiver.consts import RATING_TOPIC_NAME, KAFKA_BROKER_URL
from receiver.log import logger


class JSONReceiver:
    def __init__(self, handler_strategy: MessageHandlingStrategy) -> None:
        self.handler_strategy = handler_strategy

    def start(self) -> None:
        asyncio.run(self.__consume_json_messages())

    async def __consume_json_messages(self) -> None:
        consumer = self.__initialize_kafka_consumer()

        await consumer.start()

        try:
            async for message in consumer:
                data = json.loads(message.value)
                logger.info(f"Received Data: {data}")
                await self.handler_strategy.on_message(data)
        finally:
            await consumer.stop()

    @staticmethod
    def __initialize_kafka_consumer() -> AIOKafkaConsumer:
        return AIOKafkaConsumer(
            RATING_TOPIC_NAME,
            loop=asyncio.get_event_loop(),
            bootstrap_servers=KAFKA_BROKER_URL
        )
