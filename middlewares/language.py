from aiogram.types import TelegramObject
from aiogram import BaseMiddleware
from aiogram.fsm.context import FSMContext
from typing import Callable, Awaitable, Dict, Any

class LanguageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        state: FSMContext = data.get("state")
        lang_code = "uz"  # Default til

        if state:
            user_data = await state.get_data()
            lang_code = user_data.get("lang", "uz")

        data["lang"] = lang_code
        return await handler(event, data)
