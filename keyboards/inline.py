from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Место", callback_data='mest')
    kb.button(text="Маршрут", callback_data='marsh')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def get_emotion_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Страх")
    kb.button(text="Удивление")
    kb.button(text="Умиротворение")
    kb.button(text="Разочарование")
    kb.button(text="Ввести свою...")
    kb.adjust(1,1,1,1,1)
    return kb.as_markup(resize_keyboard=True)


