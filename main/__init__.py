from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
#API_ID = config("API_ID", default=None, cast=int)
#API_HASH = config("API_HASH", default=None)
#BOT_TOKEN = config("BOT_TOKEN", default=None)
#BOT_UN = config("BOT_UN", default=None)
#AUTH_USERS = config("AUTH_USERS", default=None, cast=int)
#LOG_CHANNEL = config("LOG_CHANNEL", default=None)
#LOG_ID = config("LOG_ID", default=None)
#FORCESUB = config("FORCESUB", default=None)
#FORCESUB_UN = config("FORCESUB_UN", default=None)
#ACCESS_CHANNEL = config("ACCESS_CHANNEL", default=None)
#MONGODB_URI = config("MONGODB_URI", default=None)

API_ID = 13216322
API_HASH = "15e5e632a8a0e52251ac8c3ccbe462c7"
BOT_TOKEN ="7034502580:AAGf4uNwTeHKF6HpkXSGPa97Y6HfXz6yHBo"
BOT_UN = "@videoxconvertorbot"
AUTH_USERS = 5642570692
LOG_CHANNEL = "oekendien"
LOG_ID = -1002017655900
FORCESUB = 1913863954
FORCESUB_UN = "@mehulbots"
ACCESS_CHANNEL = -1002017655900
MONGODB_URI = "mongodb+srv://user123456:123456user@cluster0.fysntw5.mongodb.net/"

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
