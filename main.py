import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from handlers import user_handlers, callback_handlers
from fsm import game_fsm
import logging
from configs.config import load, Config

config: Config = load()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=config.logger_format)

async def main():
    bot = Bot(token = config.token, default=DefaultBotProperties(parse_mode=config.parse_mode))
    dp = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(callback_handlers.router)
    dp.include_router(game_fsm.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logger.info("Bot started!")
    asyncio.run(main())