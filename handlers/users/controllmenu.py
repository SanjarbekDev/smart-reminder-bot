from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from states.utcmenu import UtcKey,updates
from aiogram.types import CallbackQuery
from keyboards.inline.utc import UtcKey1,UtcKey2,UtcKey3,UtcKey4,UtcKey5,UPD_UtcKey1,UPD_UtcKey2,UPD_UtcKey3,UPD_UtcKey4,UPD_UtcKey5
from loader import dp,db
from utils.misc.reminder import livetime
import logging

#1 to 2
@dp.callback_query_handler(text='next',state=UtcKey.key1)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='2️⃣ Mahaliy vaqni tanlang!',reply_markup=await UtcKey2())
    await state.set_state(UtcKey.key2)

@dp.callback_query_handler(text='back',state=UtcKey.key2)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="ortga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='1️⃣ Mahaliy vaqni tanlang!',reply_markup=await UtcKey1())
    await state.set_state(UtcKey.key1)

#2 to 3
@dp.callback_query_handler(text='next',state=UtcKey.key2)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='3️⃣ Mahaliy vaqni tanlang!',reply_markup=await UtcKey3())
    await state.set_state(UtcKey.key3)

#3 to 2
@dp.callback_query_handler(text='back',state=UtcKey.key3)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='2️⃣ Mahaliy vaqni tanlang!',reply_markup=await UtcKey2())
    await state.set_state(UtcKey.key2)

#3 to 4
@dp.callback_query_handler(text='next',state=UtcKey.key3)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='4️⃣ Mahaliy vaqni tanlang!',reply_markup=await UtcKey4())
    await state.set_state(UtcKey.key4)

#4 to 3
@dp.callback_query_handler(text='back',state=UtcKey.key4)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='3️⃣ Mahaliy vaqni tanlang!',reply_markup=await UtcKey3())
    await state.set_state(UtcKey.key3)

#4 to 5
@dp.callback_query_handler(text='next',state=UtcKey.key4)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='5️⃣ Mahaliy vaqni tanlang!',reply_markup=await UtcKey5())
    await state.set_state(UtcKey.key5)

#5 to 4
@dp.callback_query_handler(text='back',state=UtcKey.key5)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='4️⃣ Mahaliy vaqni tanlang!',reply_markup=await UtcKey4())
    await state.set_state(UtcKey.key4)


#Updates time zone controll
##################################################################################################

@dp.callback_query_handler(text='cancel',state='*')
async def cancel_state(call: CallbackQuery, state: FSMContext):
    """
    Allow user to cancel any action
    """
    try:
        current_state = await state.get_state()
        if current_state is None:
            return

        logging.info('Cancelling state %r', current_state)
       # Cancel state and inform user about it
        await state.finish()
       # And remove keyboard (just in case)
        await call.message.delete()
        await call.message.answer('✅ Bekor qilindi')

    except Exception as e:
        print(e)

#1 to 2
@dp.callback_query_handler(text='next',state=updates.upd_key1)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='2️⃣ Mahaliy vaqni tanlang!',reply_markup=await UPD_UtcKey2())
    await state.set_state(updates.upd_key2)

@dp.callback_query_handler(text='back',state=updates.upd_key2)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="ortga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='1️⃣ Mahaliy vaqni tanlang!',reply_markup=await UPD_UtcKey1())
    await state.set_state(updates.upd_key1)

#2 to 3
@dp.callback_query_handler(text='next',state=updates.upd_key2)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='3️⃣ Mahaliy vaqni tanlang!',reply_markup=await UPD_UtcKey3())
    await state.set_state(updates.upd_key3)

#3 to 2
@dp.callback_query_handler(text='back',state=updates.upd_key3)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='2️⃣ Mahaliy vaqni tanlang!',reply_markup=await UPD_UtcKey2())
    await state.set_state(updates.upd_key2)

#3 to 4
@dp.callback_query_handler(text='next',state=updates.upd_key3)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='4️⃣ Mahaliy vaqni tanlang!',reply_markup=await UPD_UtcKey4())
    await state.set_state(updates.upd_key4)

#4 to 3
@dp.callback_query_handler(text='back',state=updates.upd_key4)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='3️⃣ Mahaliy vaqni tanlang!',reply_markup=await UPD_UtcKey3())
    await state.set_state(updates.upd_key3)

#4 to 5
@dp.callback_query_handler(text='next',state=updates.upd_key4)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='5️⃣ Mahaliy vaqni tanlang!',reply_markup=await UPD_UtcKey5())
    await state.set_state(updates.upd_key5)

#5 to 4
@dp.callback_query_handler(text='back',state=updates.upd_key5)
async def back_control(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Oldinga",cache_time=60)
    await call.message.delete()
    await call.message.answer(text='4️⃣ Mahaliy vaqni tanlang!',reply_markup=await UPD_UtcKey4())
    await state.set_state(updates.upd_key4)

#########################################################################

#check update

@dp.callback_query_handler(lambda x:x.data in livetime.show_time_zone(),state=[updates.upd_key1,updates.upd_key2,updates.upd_key3,updates.upd_key4,updates.upd_key5])
async def set_timezone(call: CallbackQuery, state: FSMContext):
    data={
        'user_name':call.from_user.username,
        'user_id':call.from_user.id,
        'time_zone':call.data
    }
    try:
        db.update('users',set=f"time_zone='{data['time_zone']}'",where=f"user_id='{data['user_id']}'")
        await call.answer(text=f"Muvoffaqiyatli o'zgartirildi:{call.data}")
    except Exception as e:
            logging.info(e)
    await call.message.answer(text=f"<b>Botdan foydalanishingiz mumkin\n/help</b>")
    await state.finish()

#########################################################################
@dp.callback_query_handler(lambda x:x.data in livetime.show_time_zone(),state='*')
async def set_timezone(call: CallbackQuery, state: FSMContext):
    data={
        'user_name':call.from_user.username,
        'user_id':call.from_user.id,
        'time_zone':call.data
    }

    if db.filter(table_name='users',user_id=call.from_user.id):
        await call.message.answer(
            text="<b>⚠️ Siz allaqachon hududni belgilagansiz\no'gartirish uchun: /update_zone</b>"
            )
    else:
        try:
            db.add_to_table('users',data)
        except Exception as e:
            logging.info(e)
        await call.answer(text=f"Muvoffaqiyatli belgilandi:{call.data}")
    await call.message.answer(text=f"<b>Botdan foydalanishingiz mumkin\n/help</b>")
    await state.finish()


