import os

from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

MIN_RATINGS_FOR_INCLUSION = int(os.getenv('MIN_RATINGS_FOR_INCLUSION'))
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))