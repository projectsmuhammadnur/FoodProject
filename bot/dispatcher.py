from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.config import Config

bot = Bot(Config.BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())