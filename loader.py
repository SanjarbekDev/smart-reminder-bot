from aiogram import Bot,Dispatcher
from utils.db_api.api_ref import data_db
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config

bot=Bot(token=config.BOT_TOKEN,parse_mode="HTML")
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
db=data_db(path_db='reminder.db')
