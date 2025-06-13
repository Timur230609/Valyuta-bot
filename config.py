import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

load_dotenv()

BOT_TOKEN="8199864701:AAHUWxSWpeEfF6cVZqfuwJYcpNTbOiUoY2E"
ADMIN_IDS=[7776081021]

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

dp = Dispatcher(storage=MemoryStorage())
