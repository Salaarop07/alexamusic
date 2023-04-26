import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "22591542"))
API_HASH = getenv("API_HASH", "66e5f190dd81d951674d8edc78f162e5)
BOT_USERNAME = getenv("BOT_USERNAME")
BOT_TOKEN = getenv("BOT_TOKEN")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL")
SUPPORT_GROUP = getenv("SUPPORT_GROUP")
OWNER_USERNAME = getenv("OWNER_USERNAME")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5715680680").split()))
aiohttpsession = aiohttp.ClientSession()
