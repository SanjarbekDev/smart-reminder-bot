from utils.misc.reminder import livetime
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton



async def TargetButtons(data:dict):
    markup=InlineKeyboardMarkup(row_width=2)
    for text,url in data.items():
        btn=InlineKeyboardButton(text=text,url=url)
        markup.insert(btn)

    return markup

ChekSwitchBTN=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅ Ha',callback_data='yes'),
            InlineKeyboardButton(text="❌ Yo'q",callback_data="no")
        ]
    ]
)

ChekRek=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✈️ Jo'natish",callback_data='push')
        ],
        [
            InlineKeyboardButton(text="🚫 To'xtatish",callback_data='cancel')
        ]
    ]
)
