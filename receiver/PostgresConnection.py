# TODO: set as null if connected was dropped.
import psycopg2

from receiver.consts import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD


class PostgresConnection:
    __connection = None

    @classmethod
    def get_connection(cls):
        cls.__ensure_connected()
        return cls.__connection

    @classmethod
    def close(cls) -> None:
        cls.__connection.close()
        cls.__connection = None

    @classmethod
    def __ensure_connected(cls):
        if not cls.__connection:
            cls.__connection = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT
            )
