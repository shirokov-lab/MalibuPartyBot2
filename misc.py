import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram import Bot
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage



bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
