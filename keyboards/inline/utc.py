from utils.misc.reminder import livetime
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


back_btn=InlineKeyboardButton(text='⬅️',callback_data='back')
next_btn=InlineKeyboardButton(text='➡️',callback_data='next')
cancel_btn=InlineKeyboardButton(text='❌ Bekor qilish',callback_data='cancel')

async def UtcKey1():
    Key1=InlineKeyboardMarkup(row_width=2)
    for key in livetime.show_time_zone()[:10]:
        btn1=InlineKeyboardButton(text='🕙'+key,callback_data=key)
        Key1.insert(btn1)
    Key1.insert(next_btn)
    return Key1

async def UtcKey2():
    Key2=InlineKeyboardMarkup(row_width=2)
    for key in livetime.show_time_zone()[10:20]:
        btn2=InlineKeyboardButton(text='🕚 '+key,callback_data=key)
        Key2.insert(btn2)
    Key2.insert(back_btn)
    Key2.insert(next_btn)
    return Key2

async def UtcKey3():
    Key3=InlineKeyboardMarkup(row_width=2)
    for key in livetime.show_time_zone()[20:30]:
        btn3=InlineKeyboardButton(text='🕡 '+key,callback_data=key)
        Key3.insert(btn3)
    Key3.insert(back_btn)
    Key3.insert(next_btn)
    return Key3

async def UtcKey4():
    Key4=InlineKeyboardMarkup(row_width=2)
    for key in livetime.show_time_zone()[30:40]:
        btn4=InlineKeyboardButton(text='🕡 '+key,callback_data=key)
        Key4.insert(btn4)
    Key4.insert(back_btn)
    Key4.insert(next_btn)
    return Key4

async def UtcKey5():
    Key5=InlineKeyboardMarkup(row_width=2)
    for key in livetime.show_time_zone()[40:50]:
        btn5=InlineKeyboardButton(text='🕦 '+key,callback_data=key)
        Key5.insert(btn5)
    Key5.insert(back_btn)
    return Key5

#updater key
async def UPD_UtcKey1():
    Key1=InlineKeyboardMarkup(row_width=2)
    for key in livetime.show_time_zone()[:10]:
        btn1=InlineKeyboardButton(text='🕙'+key,callback_data=key)
        Key1.insert(btn1)
    Key1.insert(next_btn)
    Key1.insert(cancel_btn)
    return Key1

async def UPD_UtcKey2():
    Key2=InlineKeyboardMarkup(row_width=2)
    for key in livetime.show_time_zone()[10:20]:
        btn2=InlineKeyboardButton(text='🕚 '+key,callback_data=key)
        Key2.insert(btn2)
    Key2.insert(back_btn)
    Key2.insert(next_btn)
    Key2.insert(cancel_btn)
    return Key2

async def UPD_UtcKey3():
    Key3=InlineKeyboardMarkup(row_width=2)
    for key in livetime.show_time_zone()[20:30]:
        btn3=InlineKeyboardButton(text='🕡 '+key,callback_data=key)
        Key3.insert(btn3)
    Key3.insert(back_btn)
    Key3.insert(next_btn)
    Key3.insert(cancel_btn)
    return Key3

async def UPD_UtcKey4():
    Key4=InlineKeyboardMarkup(row_width=2)
    for key in livetime.show_time_zone()[30:40]:
        btn4=InlineKeyboardButton(text='🕡 '+key,callback_data=key)
        Key4.insert(btn4)
    Key4.insert(back_btn)
    Key4.insert(next_btn)
    Key4.insert(cancel_btn)
    return Key4

async def UPD_UtcKey5():
    Key5=InlineKeyboardMarkup(row_width=2)
    for key in livetime.show_time_zone()[40:50]:
        btn5=InlineKeyboardButton(text='🕦 '+key,callback_data=key)
        Key5.insert(btn5)
    Key5.insert(back_btn)
    Key5.insert(cancel_btn)
    return Key5


cancel_key_g_n=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='❌ Bekor qilish',callback_data='cancel_g_n')
        ]
    ]
)

cancel_key_g_b=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='❌ Bekor qilish',callback_data='cancel_g_b')
        ]
    ]
)

cancel_key_p=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='❌ Bekor qilish',callback_data='cancel_p')
        ]
    ]
)
    