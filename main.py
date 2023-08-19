import logging
import asyncio

from aiogram.utils import executor
from bot.handlers import *

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, skip_updates=True)
