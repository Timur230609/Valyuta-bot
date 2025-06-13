from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from texts import TEXTS
from keyboards.main import get_currency_keyboard

router = Router()

# /start buyrug‘iga javob
@router.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer(
        "Tilni tanlang / Выберите язык / Choose language",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="🇺🇿 O‘zbek", callback_data="lang_uz"),
                    InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
                    InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en"),
                ]
            ]
        )
    )

# Til tanlangandan so‘ng ishlovchi callback
@router.callback_query(F.data.startswith("lang_"))
async def language_selected(call: CallbackQuery):
    lang_code = call.data.split("_")[1]
    await call.message.delete()
    await call.message.answer(
        TEXTS[lang_code]['welcome'],
        reply_markup=get_currency_keyboard(lang_code)
    )
