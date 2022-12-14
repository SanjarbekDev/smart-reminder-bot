from loader import dp,db
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers import logging 
import asyncio
import re
from utils.misc.timer import start as timer_start
from utils.misc.timer_group import start_timer_group
from utils.misc.brith_day_timer import start_brith_group


async def main():
    try:
        db.create_table(table_name='users',id='INTEGER PRIMARY KEY AUTOINCREMENT',user_name='varchar(100)',user_id='varchar(15) NOT NULL UNIQUE',time_zone="REAL NOT NULL")
        db.create_table(table_name='groups',id='INTEGER PRIMARY KEY AUTOINCREMENT',title='varchar(100)',chat_id='varchar(15) NOT NULL UNIQUE')
        db.create_table(table_name='reminders',id='INTEGER PRIMARY KEY AUTOINCREMENT',user_name='varchar(100)',user_id='varchar(15)',weak_d='varchar(1) NOT NULL',time="varchar(16) DEFAULT '08:30'",comment='varchar(255)',photo_id='varchar(300)')
        db.create_table(table_name='groups_note',id='INTEGER PRIMARY KEY AUTOINCREMENT',title='varchar(100)',chat_id='varchar(15)',weak_d='varchar(1) NOT NULL',time="varchar(16) DEFAULT '08:30'",comment='varchar(255)',photo_id='varchar(300)')
        db.create_table(table_name='groups_brith',id='INTEGER PRIMARY KEY AUTOINCREMENT',chat_id='varchar(15)',data_b='varchar(1)',time="varchar(16)",comment='varchar(255)',photo_id='varchar(300)')
    except Exception as e:
        logging.info(e)

    await asyncio.gather(dp.start_polling(),timer_start(),start_timer_group(),start_brith_group())
    asyncio.sleep(1)



if __name__ == '__main__':
    asyncio.run(main=main())
    