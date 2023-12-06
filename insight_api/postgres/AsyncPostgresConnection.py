from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from insight_api.consts import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


class AsyncPostgresConnection:
    __engine = None
    __session_generator = None

    @classmethod
    def get_connection(cls):
        cls.__ensure_pool_is_connected()

        return cls.__session_generator()

    @classmethod
    def __ensure_pool_is_connected(cls):
        if not cls.__engine:
            DB_CONNECTION_POOL_MIN_SIZE = 10  # TODO: move to .env
            DB_CONNECTION_POOL_MAX_SIZE = 20
            cls.__engine = create_async_engine(
                f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
                echo=True,
                pool_size=DB_CONNECTION_POOL_MIN_SIZE, max_overflow=DB_CONNECTION_POOL_MAX_SIZE
            )

            cls.__session_generator = sessionmaker(cls.__engine, class_=AsyncSession, expire_on_commit=False)

    @classmethod
    async def close(cls) -> None:
        if not cls.__engine:
            await cls.__engine.dispose()

        cls.__engine = None
        cls.__session_generator = None
