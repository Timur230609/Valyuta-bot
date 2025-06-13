import asyncio
from config import bot, dp
from middlewares.language import LanguageMiddleware
from handlers import users

dp.include_router(users.router)
dp.message.middleware(LanguageMiddleware())

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
