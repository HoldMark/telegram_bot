import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PAS = os.environ.get("DB_PAS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
TG_USER_ID = os.environ.get("TG_USER_ID")
