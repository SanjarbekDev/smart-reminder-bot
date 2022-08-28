import asyncio
from . reminder import livetime
from loader import db,bot
import logging

dt_time=livetime('Asia/Samarkand')

async def check():
    global dt_time
    while True:
        try:
            reminders_results = db.get_all('reminders') 
            for x in reminders_results:
                getter_zone=db.filter('users',user_id=x[2])[3]
                dt_time=livetime(getter_zone)
                time_list=dt_time.get_time()
                if x[4]==time_list[4] and time_list[3]==x[3]:
                    if x[6]:
                        await bot.send_photo(chat_id=x[2],photo=x[6],caption=f'<b>⏰ Vaqt bo\'ldi\n\n{x[5]}\nSoat: {x[4]}</b>',parse_mode='HTML')
                    else:
                        await bot.send_message(chat_id=x[2],text=f'<b>⏰ Vaqt bo\'ldi\n\n{x[5]}\nSoat: {x[4]}</b>',parse_mode='HTML')
        except Exception as e:
            logging.info(e)
            await asyncio.sleep(1)
        await asyncio.sleep(60)

async def start():
    delay = 60-int(dt_time.get_time()[5])
    if delay == 60:
        delay = 0
    #
    await asyncio.sleep(delay)
    await check()
