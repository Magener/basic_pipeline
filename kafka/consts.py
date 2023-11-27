import os

from dotenv import load_dotenv

load_dotenv()
KAFKA_BROKER_URL = os.getenv('KAFKA_BROKER_URL')