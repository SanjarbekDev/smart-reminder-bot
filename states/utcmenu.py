from aiogram.dispatcher.filters.state import State,StatesGroup


class UtcKey(StatesGroup):
    key1=State()
    key2=State()
    key3=State()
    key4=State()
    key5=State()

class updates(StatesGroup):
    upd_key1=State()
    upd_key2=State()
    upd_key3=State()
    upd_key4=State()
    upd_key5=State()

class photo_filter(StatesGroup):
    get_photo=State()
