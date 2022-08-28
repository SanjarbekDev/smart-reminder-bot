from loader import dp,db
import logging
from aiogram.types import Message,CallbackQuery
from keyboards.inline.delete_key import weak_key,generate_key
from states.deletstate import DelState
from aiogram.dispatcher import FSMContext
from filters.private_chat import IsPrivate


@dp.message_handler(IsPrivate(),commands='del_r',state='*')
async def send(msg: Message, state: FSMContext):
    await msg.answer(text="Haftani tanlang",reply_markup=weak_key)
    await state.set_state(DelState.select_w)


@dp.callback_query_handler(state=DelState.select_w) 
async def selectw(call:CallbackQuery, state: FSMContext):
    weak_d=call.data
    try: 
        keys=db.get_filters('reminders',select='time',user_id=call.from_user.id,weak_d=weak_d)
    except Exception as e:
        logging.info(e)
    if keys:
        await call.message.edit_reply_markup(reply_markup=await generate_key(data=keys))
        await state.set_state(DelState.select_t)
    else:
        await call.answer('😥 Hech narsa topilmadi',cache_time=60)
        

@dp.callback_query_handler(state=DelState.select_t) 
async def delete_reminder(call:CallbackQuery, state: FSMContext):
    try:
        db.delete('reminders',where=f"user_id={call.from_user.id} AND time='{call.data}'")
        await call.answer(f"{call.data} vaqtdagi eslatma o'chirildi.",cache_time=60)
        await call.message.delete()
        await call.message.answer(text="✅Tayyor")
        await state.reset_state()
    except Exception as e:
        await call.message.answer(text="😥 O'chirishni imkoni bo'lmadi qayta urinib ko'ring: /del")
        await state.reset_state()
        logging.info(e)