import os

from dotenv import load_dotenv

load_dotenv()

MIN_RATINGS_FOR_INCLUSION = int(os.getenv('MIN_RATINGS_FOR_INCLUSION', 5))
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT', 9000))
COMMAND_TIMEOUT = int(os.getenv('COMMAND_TIMEOUT', 60))
