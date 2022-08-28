from aiogram.types import Message,CallbackQuery
import re
from loader import dp,db
import logging
from states.utcmenu import updates,UtcKey
from aiogram.dispatcher import FSMContext
from states.utcmenu import photo_filter
from keyboards.inline.utc import cancel_key_g_b,cancel_key_g_n
from filters.group_chat import IsGroup

weak_day={
    'yakshanba':0,
    'dushanba':1,
    'seshanba':2,
    'chorshanba':3,
    'payshanba':4,
    'juma':5,
    'shanba':6,
    
}
#set brith day
@dp.message_handler(IsGroup(),commands='brith_day',state='*')
async def setreminder(msg :Message,state:FSMContext):
    text=f'<b>🖼 Rasim qo\'shishni xohlasangiz biror rasim yuboring yoki bekor qilish tugmasini bosing‼️\n\n✅Qabul qilindi</b>'
    data_parse=re.compile(r"(/brith_day) ?([\d\,\-]+)? ?([\d:]+)? ?([\w\-\s\+]+)?")
    parsed=data_parse.match(msg.text)
    data_b=parsed.group(2)
    comment=parsed.group(4)
    if data_b:
        if parsed.group(3):
            data_h=parsed.group(3)
        else:
            data_h="07:30"
        await state.update_data(
            {   
                'chat_id':msg.chat.id,
                'data_b':data_b,
                'time':data_h,
                'comment':comment
            }
        )

        
    else:
        await msg.answer(text='<b>❌  Tugilgan kuni (05-06-2000) shu formatda kiritilishi shart.</b>',parse_mode='HTML')
    await msg.reply(text=text,reply_markup=cancel_key_g_b)
    await state.set_state(photo_filter.get_photo)

@dp.callback_query_handler(text='cancel_g_b',state=photo_filter.get_photo)
async def cancelled(call: CallbackQuery, state: FSMContext):
    data_frame=await state.get_data()
    try:
        db.add_to_table('groups_brith',data_frame)
    except Exception as e:
        logging.info(e)
    await call.message.answer(text="<b>✅Bekor qilindi va malumotlar saqlandi</b>")
    await state.reset_state()

@dp.message_handler(IsGroup(),content_types='photo',state=photo_filter.get_photo)
async def get_photo(msg:Message,state:FSMContext):
    photo=msg.photo[-1].file_id
    await state.update_data(
        {
            'photo_id':photo
        }
    )
    data_frame=await state.get_data()
    try:
        db.add_to_table('groups_brith',data_frame)
    except Exception as e:
        logging.info(e)
    await msg.reply(text="<b>✅Malumotlar saqlandi</b>")
    await state.reset_state()




#set notes
@dp.message_handler(IsGroup(),commands='set',state='*')
async def setreminder(msg :Message,state:FSMContext):
    data_parse=re.compile(r"(/set) ?(\w+)? ?([\d+^:]+)? ?([\w\D+]+)?")
    parsed=data_parse.match(msg.text)
    weak_d=parsed.group(2)
    data_h=parsed.group(3)
    comment=parsed.group(4)
    text=f'<b>🖼 Rasim qo\'shishni xohlasangiz biror rasim yuboring yoki bekor qilish tugmasini bosing‼️\n\n✅Qabul qilindi</b>'
    if weak_d:
        await state.update_data(
            {   
                'title':msg.chat.title,
                'chat_id':msg.chat.id,
                'weak_d':weak_day[weak_d],
                'time':data_h,
                'comment':comment
            }
        )

        
        
    else:
        await msg.answer(text='<b>❌  Hafta kuni kiritilishi shart.</b>',parse_mode='HTML')
    await msg.reply(text=text,reply_markup=cancel_key_g_n)
    await state.set_state(photo_filter.get_photo)

@dp.callback_query_handler(text='cancel_g_n',state=photo_filter.get_photo)
async def cancelled(call: CallbackQuery, state: FSMContext):
    data_frame=await state.get_data()
    try:
        db.add_to_table('groups_note',data_frame)
    except Exception as e:
        logging.info(e)
    await call.message.answer(text="<b>✅Bekor qilindi va malumotlar saqlandi</b>")
    await state.reset_state()

@dp.message_handler(IsGroup(),content_types='photo',state=photo_filter.get_photo)
async def get_photo(msg:Message,state:FSMContext):
    photo=msg.photo[-1].file_id
    await state.update_data(
        {
            'photo_id':photo
        }
    )
    data_frame=await state.get_data()
    try:
        db.add_to_table('groups_note',data_frame)
    except Exception as e:
        logging.info(e)
    await msg.reply(text="<b>✅Malumotlar saqlandi</b>")
    await state.reset_state()

