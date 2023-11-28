# TODO: set as null if connected was dropped.
import psycopg2

# TODO: move variables to .env
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "pgsql"
DB_HOST = "localhost"
DB_PORT = "5432"


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
