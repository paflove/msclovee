import asyncio
from aiogram import Bot, Dispatcher
from handlers import startHand


token = '7489996248:AAGzp39JAMGBURIxTgtrJPL-bAekjR-6A30'






async def start():
    dp = Dispatcher()
    bot = Bot(token=token)
    try:
        dp.include_routers(startHand.router)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())