from aiogram.fsm.state import State, StatesGroup

class SearchStates(StatesGroup):
    waiting_for_region = State()
    waiting_for_district = State()
    waiting_for_mahalla = State()
    waiting_for_property_type = State()
    waiting_for_area = State()
    waiting_for_repair = State()
    waiting_for_price = State()
