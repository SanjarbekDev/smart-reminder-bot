from loader import dp,db,bot
import logging
from aiogram.types import Message,CallbackQuery
from keyboards.inline.targetbtns import TargetButtons,ChekRek,ChekSwitchBTN
from states.reklama import rek
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from filters.private_chat import IsPrivate



@dp.message_handler(IsPrivate(),commands='rek',user_id=ADMINS[0])
async def rekstart(msg:Message,state:FSMContext):
    await msg.answer(text="<b>👨‍💻 Xo'sh nimani reklamma qilmoqchisiz ?(text,video,rasim)\nReklama qilmoqchi bo'lgan kontentni yuboring.</b>")
    await state.set_state(rek.rek_state)

@dp.message_handler(IsPrivate(),user_id=ADMINS[0],state=rek.rek_state)
async def rekstart(msg:Message,state:FSMContext):
    await state.update_data(
        data={
            "message":msg.text
        }
    )
    await msg.answer(text="<b>👨‍💻 Xabarni yuborishni tasdiqlang.</b>",reply_markup=ChekRek)
    await state.set_state(rek.chek)


@dp.message_handler(IsPrivate(),content_types='photo',user_id=ADMINS[0],state=rek.rek_state)
async def rekstart(msg:Message,state:FSMContext):
    photo= msg.photo[-1].file_id
    caption= msg.caption
    await state.update_data(
        data={
            "photo":photo,
            'caption':caption
        }
    )
    await msg.answer(text="🕹 Tugma qo'shishasizmi ?",reply_markup=ChekSwitchBTN)
    

@dp.message_handler(IsPrivate(),content_types='video',user_id=ADMINS[0],state=rek.rek_state)
async def rekstart(msg:Message,state:FSMContext):
    photo= msg.video.file_id
    caption= msg.caption
    await state.update_data(
        data={
            "video":photo,
            'caption':caption
        }
    )
    await msg.answer(text="🕹 Tugma qo'shishasizmi ?",reply_markup=ChekSwitchBTN)
    

@dp.callback_query_handler(text='yes',state=rek.rek_state)
async def target_button(call:CallbackQuery,state:FSMContext):
    await call.message.answer(text="<b>⚙️ Tugma detallarini yuboring</b>")
    await state.set_state(rek.target_btns)

@dp.callback_query_handler(text='no',state=rek.rek_state)
async def target_button(call:CallbackQuery,state:FSMContext):
    await call.message.answer(f"✉️ Kontent tayyor bo'ldi.",reply_markup=ChekRek)
    await state.set_state(rek.chek)
    

@dp.message_handler(IsPrivate(),user_id=ADMINS[0],state=rek.target_btns)
async def generate_buttons(msg:Message,state:FSMContext):
    equal=lambda x:(x[0:int(len(x)/2)],x[int(len(x)/2):])
    btn_data={}
    try:
        for key,value in equal(list(msg.text.split())):
            btn_data.update({
                key:value
            })
        markup=await TargetButtons(data=btn_data)
        await state.update_data(
            {
                "btn_data":btn_data
            }
        )
    except Exception as e:
        await msg.answer(f'Xato: {e}')
    data = await state.get_data()
    if data.get('video'):
        message=await msg.answer_video(video=data['video'],caption=data['caption'],reply_markup=markup)
        await state.update_data(
            {
                'message_id':message.message_id
            }
        )
    if data.get('photo'):
        message=await msg.answer_photo(photo=data['photo'],caption=data['caption'],reply_markup=markup)
        await state.update_data(
            {
                'message_id':message.message_id
            }
        )
    await msg.answer(f"✉️ Kontent tayyor bo'ldi {message.message_id} | {message.chat.id} .",reply_markup=ChekRek)
    await state.set_state(rek.chek)

@dp.callback_query_handler(text='push',user_id=ADMINS[0],state=rek.chek)
async def push(call:CallbackQuery,state:FSMContext):
    data=await state.get_data()
    try:
        chats=db.get_all('groups')
        users=db.get_all('users')
        if data.get('btn_data'):
            markup=await TargetButtons(data['btn_data'])
        if data.get('photo'):
            for chat in chats:
                try:
                    await bot.send_photo(chat_id=chat[2],photo=data['photo'],caption=data['caption'],reply_markup=markup)
                except UnboundLocalError:
                    await bot.send_photo(chat_id=chat[2],photo=data['photo'],caption=data['caption'])
                except Exception as e:
                    await call.message.answer(text=f"<b>🆘 xato: {e}\nchat: {chat[2]}</b>")
                
            for user in users:
                try:
                    await bot.send_photo(chat_id=user[2],photo=data['photo'],caption=data['caption'],reply_markup=markup)
                except UnboundLocalError:
                    await bot.send_photo(chat_id=user[2],photo=data['photo'],caption=data['caption'])
                except Exception as e:
                    await call.message.answer(text=f"<b>🆘 xato: {e} \nchat: {user[2]}</b>")

        if data.get('video'):
            for chat in chats:
                try:
                    await bot.send_video(chat_id=chat[2],video=data['video'],caption=data['caption'],reply_markup=markup)
                    # await bot.copy_message(chat_id=call.message.chat.id,from_chat_id=chat[2],message_id=message['message_id'])
                except UnboundLocalError:
                    await bot.send_video(chat_id=chat[2],video=data['video'],caption=data['caption'])
                except Exception as e:
                    await call.message.answer(text=f"<b>🆘 xato: {e}\nchat: {chat[2]}</b>")
            for user in users:
                try:
                    await bot.send_video(chat_id=user[2],video=data['video'],caption=data['caption'],reply_markup=markup)
                except UnboundLocalError:
                    await bot.send_video(chat_id=user[2],video=data['video'],caption=data['caption'])
                except Exception as e:
                    await call.message.answer(text=f"<b>🆘 xato: {e} \nchat: {user[2]}</b>")

        if data.get('message'):
            for chat in chats:
                try:
                    await bot.send_message(chat_id=chat[2],text=data['message'])
                except Exception as e:
                    await call.message.answer(text=f"<b>🆘 xato: {e}\nchat: {chat[2]}</b>")
            for user in users:
                try:
                    await bot.send_message(chat_id=user[2],text=data['message'])
                except Exception as e:
                    await call.message.answer(text=f"<b>🆘 xato: {e} \nchat: {user[2]}</b>")
    except Exception as e:
        logging.info(e)
        await call.message.answer(text=f"🆘 xatolik paydo o'ldi: {e}")

    await call.answer("Xabar yuborildi",cache_time=60)
    await state.reset_state()
