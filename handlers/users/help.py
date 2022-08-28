from loader import dp,db
from aiogram.types import Message



@dp.message_handler(commands='help',state='*')
async def send(msg: Message):
    message="Botdan foydalanish:\n"
    message+="/set [hafta kunni] [vaqt] [kamentariya] - eslatma qo'shish\n"
    message+="/update_zone-hududni o'zgartirish\n"
    message+="/del_r - eslatmani o'chirish"
    await msg.answer(text=message)
    
    