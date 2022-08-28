from loader import dp,db,bot
import logging
from aiogram.types import Message
from keyboards.inline.utc import UtcKey1
from states.utcmenu import UtcKey
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from filters.private_chat import IsPrivate
from filters.group_chat import IsGroup


@dp.message_handler(IsGroup(),commands='start',state='*',user_id=ADMINS[0])
async def send(msg: Message, state: FSMContext):
    data={
        "title":msg.chat.title,
        'chat_id':msg.chat.id
    }
    try:
        db.add_to_table('groups',data)
    except Exception as e:
        logging.info(e)
    await msg.answer(text="/help - yordam")

@dp.message_handler(IsGroup(),commands='help',state='*',user_id=ADMINS[0])
async def send(msg: Message, state: FSMContext):
    message="Buyruqlar:\n"
    message+="/set - eslatma qo'shish\nmasalan: /set dushanba 08:30 birinchi para dasturlash fani\n"
    message+="/brith_day - tug'ilgan kun tabrigi\nmasalan: /brith_day 15-06-1999 Dilshod bugun sening kuning"
    await msg.answer(text=message)

@dp.message_handler(IsPrivate(),commands='start',state='*',user_id=ADMINS[0])
async def send(msg: Message, state: FSMContext):
    await msg.answer(text="<b>Assalomu aleykum admin.</b>\nMahalliy vaqtni tanlang",reply_markup=await UtcKey1())
    await state.set_state(UtcKey.key1)

@dp.message_handler(IsPrivate(),commands='rating',state='*',user_id=ADMINS[0])
async def send(msg: Message, state: FSMContext):
    try:
        users=db.counter('users')[0]
        reminders=db.counter('reminders')[0]
        groups=db.counter('groups')[0]
        groups_note=db.counter('groups_note')[0]
        brith_day=db.counter('groups_brith')[0]
    except Exception as e:
        logging.info(e)
    await msg.answer(text=f"📊 Statistika:\n\n<b>Foydalanuvchilar soni: {users}\nGruhlar : {groups}\nTabriknomalar : {brith_day}\nGruh uchun eslatmalar : {groups_note}\nEslatmalar soni: {reminders}</b>")

@dp.message_handler(IsPrivate(),commands='start',state='*')
async def send(msg: Message, state: FSMContext):
    user=msg.from_user.id
    mention=f"<a href='tg://user?id={user}'>{msg.from_user.full_name}</a>"
    await msg.answer(text="Mahalliy vaqtni tanlang",reply_markup=await UtcKey1())
    try:
        await bot.send_message(chat_id=ADMINS[0],text=f"<b>Foydalanuvchi {mention} botga qo'shildi</b>")
    except Exception as e:
        logging.info(e)
    await state.set_state(UtcKey.key1)
    