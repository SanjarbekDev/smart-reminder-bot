from aiogram.dispatcher.filters.state import State,StatesGroup


class DelState(StatesGroup):
    select_w=State()
    select_t=State()
    