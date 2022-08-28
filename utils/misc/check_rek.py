import asyncio
from aiogram.utils import exceptions
from . reminder import livetime
from loader import db,bot
import logging

dt_time=livetime('Asia/Samarkand')



async def check():
    
    while True:
        try:
            pass
        except exceptions.BotBlocked:
            db.update('users',set=f"status='botBlocked'",where=f"user_id='{user_id}'")
        except exceptions.ChatNotFound:
            db.update('users',set=f"status='ChatNotFound'",where=f"user_id='{user_id}'")
        except exceptions.UserDeactivated:
            db.update('users',set=f"status='UserDeactivated'",where=f"user_id='{user_id}'")
        await asyncio.sleep(60)
        """
        try:
            await bot.send_message(chat_id=user_id, text=f"{message}\n@sabina_mebel")
        except exceptions.BotBlocked:
            log.error(f"Target [ID:{user_id}]: blocked by user")
        except exceptions.ChatNotFound:
            log.error(f"Target [ID:{user_id}]: invalid user ID")
        except exceptions.RetryAfter as e:
            log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
            await asyncio.sleep(e.timeout)
            await bot.send_message(chat_id=user_id, text=f"{message}\n@sabina_mebel") # Recursive call
        except exceptions.UserDeactivated:
            log.error(f"Target [ID:{user_id}]: user is deactivated")
        except exceptions.TelegramAPIError:
            log.exception(f"Target [ID:{user_id}]: failed")
        else:
            log.info(f"Target [ID:{user_id}]: success")
        """

async def start():
    delay = 60-int(dt_time.get_time()[5])
    if delay == 60:
        delay = 0
    #
    await asyncio.sleep(delay)
    await check()
