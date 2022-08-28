from aiogram.types import Message
from loader import dp
from keyboards.inline.utc import UPD_UtcKey1
from states.utcmenu import updates
from aiogram.dispatcher import FSMContext
from filters.private_chat import IsPrivate

@dp.message_handler(IsPrivate(),commands='update_zone',state='*')
async def updater(msg: Message,state: FSMContext):
    await msg.answer(text='‼️ Hududni tanlashingiz mumkin',reply_markup=await UPD_UtcKey1())
    await state.set_state(updates.upd_key1)

