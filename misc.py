import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram import Bot
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)
