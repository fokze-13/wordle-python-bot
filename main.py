import asyncio

from aiogram import Bot, Dispatcher
from environs import Env
from handlers import user_handlers

async def main():
    env = Env()
    env.read_env()

    bot = Bot(token = env("TOKEN"))
    dp = Dispatcher()

    dp.include_router(user_handlers.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())