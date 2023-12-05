import asyncpg

from insight_api.consts import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, COMMAND_TIMEOUT


class AsyncPostgresConnection:
    __connection_pool = None

    @classmethod
    async def get_connection(cls):
        await cls.__ensure_pool_is_connected()

        return cls.__connection_pool.acquire()

    @classmethod
    async def __ensure_pool_is_connected(cls):
        if not cls.__connection_pool or cls.__connection_pool.is_closing():
            cls.__connection_pool = await asyncpg.create_pool(user=DB_USER, password=DB_PASSWORD,
                                                              database=DB_NAME, host=DB_HOST, port=DB_PORT,
                                                              command_timeout=COMMAND_TIMEOUT)

    @classmethod
    async def close(cls) -> None:
        if not cls.__connection_pool:
            await cls.__connection_pool.close()

        cls.__connection_pool = None