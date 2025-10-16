import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config.config import Config, load_config
from database.database import init_db

#from database.database import init_db

#Что бот должен уметь?
# Загружать страницы книги из хранилища и присылать их в чат в виде сообщений с кнопками.
# Сохранять страницу, на которой остановился пользователь и загружать книгу на этом месте.
# Переходить в начало книги.

logger = logging.getLogger(__name__)

async def main():
    config:Config = load_config()

    logging.basicConfig(
        level=logging.getLevelName(level=config.log.level),
        format=config.log.format
    )
    logger.info('Bot start')

    bot = Bot(
        token = config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    logger.info('Подготовка книги!')
    book = prepare_book("book/book.txt")
    logger.info('book is upload. Total pages %d',len(book))

    db: dict = init_db()

    dp.workflow_data.update(book=book, db=db)

    await set_main_menu(bot)

    dp.include_router(user_router)
    dp.include_router(other_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())