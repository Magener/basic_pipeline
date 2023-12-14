import os

from dotenv import load_dotenv

load_dotenv()
PROCESSING_INTERVAL = float(os.getenv('PROCESSING_INTERVAL'))
