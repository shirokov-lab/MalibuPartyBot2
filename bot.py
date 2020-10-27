from misc import dp 
from aiogram import executor
from data_base.misc import session
import handlers

if __name__ == '__main__':
    executor.start_polling(dp)


