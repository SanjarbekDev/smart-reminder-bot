from utils.misc.reminder import livetime
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


weak_day={
    'yakshanba':0,
    'dushanba':1,
    'seshanba':2,
    'chorshanba':3,
    'payshanba':4,
    'juma':5,
    'shanba':6,
    
}

cancel_btn=InlineKeyboardButton(text='❌ Bekor qilish',callback_data='cancel')

weak_key=InlineKeyboardMarkup(row_width=2)
for text,call in weak_day.items():
    key=InlineKeyboardButton(text="🕐 "+text.title(),callback_data=f"{call}")
    weak_key.insert(key)
weak_key.insert(cancel_btn)

async def generate_key(data:list):
    time_key=InlineKeyboardMarkup(row_width=4)
    for i in data:
        key_t=InlineKeyboardButton(text="🗑 "+str(*i),callback_data=str(*i))
        time_key.insert(key_t)
    time_key.insert(cancel_btn)
    return time_key