from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
ADM_CHAT_ID = int(os.getenv('ADM_CHAT_ID'))
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
