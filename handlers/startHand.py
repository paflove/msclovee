from keyboards.inline import get_start_kb, get_emotion_kb
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import CallbackQuery



router = Router()  # [1]

@router.message(Command(commands=["start"]))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Приветстсвуем вас в нашем канале!",
        reply_markup=get_start_kb()
    )



@router.callback_query(F.data == 'mest')
async def get_mest(call: CallbackQuery):
    await call.message.answer('Выберите эмоцию',
                              reply_markup=get_emotion_kb()
                              )



@router.message(F.text.lower() == "маршрут")
async def answer_marsh(message: Message):
    await message.answer(
        "маршрут",

    )
