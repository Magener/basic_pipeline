import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT', 5432))

DB_CONNECTION_POOL_MIN_SIZE = int(os.getenv('DB_CONNECTION_POOL_MIN_SIZE', 10))
DB_CONNECTION_POOL_MAX_SIZE = int(os.getenv('DB_CONNECTION_POOL_MAX_SIZE', 20))