import asyncio
from . reminder import livetime
from loader import db,bot
import logging

dt_time=livetime('Asia/Samarkand')

async def check_group_brith():
    while True:
        try:
            reminders_results = db.get_all('groups_brith') 
            for x in reminders_results:
                time_list=dt_time.get_time()
                data_b_chek=dt_time.get_sql_format()
                if x[2][:5]==data_b_chek and time_list[4]==x[3]:
                    if x[5]:
                        await bot.send_photo(chat_id=x[1],photo=x[5],caption=f'<b>🎉🎊Tabriknoma🎊🎉\nJarvis {int(time_list[0])-int(x[2][6:])} yoshingiz bilan qutlaydi.\n{x[4]}\nSoat: {time_list[4]}</b>',parse_mode='HTML')
                    else:
                        await bot.send_message(chat_id=x[1],text=f'<b>🎉🎊Tabriknoma🎊🎉\nJarvis sizni {int(time_list[0])-int(x[2][6:])}\n{x[4]} yoshingiz bilan qutlaydi.\nSoat: {time_list[4]}</b>',parse_mode='HTML')
        except Exception as e:
            logging.info(e)
            await asyncio.sleep(1)
        await asyncio.sleep(60)

async def start_brith_group():
    delay = 60-int(dt_time.get_time()[5])
    if delay == 60:
        delay = 0
    #
    await asyncio.sleep(delay)
    await check_group_brith()
