# TODO: set as null if connected was dropped.
import asyncpg

from insight_api.consts import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD


class AsyncPostgresConnection:
    __connection = None

    @classmethod
    async def get_connection(cls):
        if not cls.__connection:
            cls.__connection = await asyncpg.connect(user=DB_USER, password=DB_PASSWORD,
                                                     database=DB_NAME, host=DB_HOST, port=DB_PORT)

        return cls.__connection

    @classmethod
    async def close(cls) -> None:
        await cls.__connection.close()
        cls.__connection = None