import asyncio
import json

from aiokafka import AIOKafkaConsumer

from receiver.consts import KAFKA_BROKER_URL, RATING_TOPIC_NAME
from receiver.log import logger
from temporarily_shared_files.sql_alchemy.AsyncPostgresConnection import AsyncPostgresConnection
from receiver.receiver.MessageHandlingStrategy import error_handling_async_wrapper, MessageHandlingStrategy


class JSONReceiver:
    def __init__(self, handler_strategy: MessageHandlingStrategy) -> None:
        self.handler_strategy = handler_strategy

    def start(self) -> None:
        asyncio.run(self.__consume_json_messages())

    async def __consume_json_messages(self) -> None:
        consumer = self.__initialize_kafka_consumer()

        await consumer.start()

        async for message in consumer:
            try:
                data = message.value
                logger.info(f"Received Data: {data}")
                asyncio.create_task(error_handling_async_wrapper(self.handler_strategy.on_message(data)))
            except BaseException as e:
                logger.error(f"Exception has been raised: {e}")

        await AsyncPostgresConnection.close()
        await consumer.stop()

    @staticmethod
    def __initialize_kafka_consumer() -> AIOKafkaConsumer:
        return AIOKafkaConsumer(
            RATING_TOPIC_NAME,
            loop=asyncio.get_event_loop(),
            bootstrap_servers=KAFKA_BROKER_URL,
            value_deserializer=json.loads
        )
