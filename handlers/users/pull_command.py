from aiogram.types import Message,CallbackQuery
import re
from loader import dp,db
import logging
from keyboards.inline.utc import UtcKey1,UtcKey2
from states.utcmenu import updates,UtcKey
from aiogram.dispatcher import FSMContext
from states.utcmenu import photo_filter
from keyboards.inline.utc import cancel_key_p
from filters.private_chat import IsPrivate


weak_day={
    'yakshanba':0,
    'dushanba':1,
    'seshanba':2,
    'chorshanba':3,
    'payshanba':4,
    'juma':5,
    'shanba':6,
    
}

@dp.message_handler(IsPrivate(),commands='set',state='*')
async def setreminder(msg :Message,state:FSMContext):
    data_parse=re.compile(r"(/set) ?(\w+)? ?([\d+^:]+)? ?([\w\D+]+)?")
    parsed=data_parse.match(msg.text)
    data_w=parsed.group(2)
    data_h=parsed.group(3)
    comment=parsed.group(4)
    if data_w:
        await state.update_data(
            {
                'user_name':msg.from_user.username,
                'user_id':msg.from_user.id,
                'weak_d':weak_day[data_w],
                'time':data_h,
                'comment':comment
            }
        )

        text=f'<b>🖼 Rasim qo\'shishni xohlasangiz biror rasim yuboring yoki bekor qilish tugmasini bosing‼️\n\n✅Qabul qilindi\nHafta kuni :{data_w},\nsoat :{data_h}</b>'
        
    else:
        await msg.answer(text='<b>❌ Hafta kuni kiritilishi shart.</b>',parse_mode='HTML')
    await msg.reply(text=text,reply_markup=cancel_key_p)
    await state.set_state(photo_filter.get_photo)

@dp.callback_query_handler(text='cancel_p',state=photo_filter.get_photo)
async def cancelled(call: CallbackQuery, state: FSMContext):
    data_frame=await state.get_data()
    try:
        db.add_to_table('reminders',data_frame)
    except Exception as e:
        logging.info(e)
    await call.message.answer(text="<b>✅Bekor qilindi va malumotlar saqlandi</b>")
    await state.reset_state()

@dp.message_handler(content_types='photo',state=photo_filter.get_photo)
async def get_photo(msg:Message,state:FSMContext):
    photo=msg.photo[-1].file_id
    await state.update_data(
        {
            'photo_id':photo
        }
    )
    data_frame=await state.get_data()
    try:
        db.add_to_table('reminders',data_frame)
    except Exception as e:
        logging.info(e)
    await msg.reply(text="<b>✅Malumotlar saqlandi</b>")
    await state.reset_state()

