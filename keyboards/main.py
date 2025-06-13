
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🏦 Valyuta Kursi"),
                KeyboardButton(text="🧮 Ayirboshlash")
            ]
        ],
        resize_keyboard=True
    )
    

def main_menu_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
        KeyboardButton("🏦 Valyuta Kursi"),
        KeyboardButton("🧮 Ayirboshlash")
    )
    return kb


def exchange_menu_keyboard():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇸 USD", callback_data="exchange_usd"), InlineKeyboardButton(text="🇪🇺 EUR", callback_data="exchange_eur")],
        [InlineKeyboardButton(text="🇷🇺 RUB", callback_data="exchange_rub"), InlineKeyboardButton(text="🇬🇧 GBP", callback_data="exchange_gbp")],
        [InlineKeyboardButton(text="🇨🇦 CAD", callback_data="exchange_cad"), InlineKeyboardButton(text="🇨🇳 CNY", callback_data="exchange_cny")],
        [InlineKeyboardButton(text="🇰🇷 KRW", callback_data="exchange_krw"), InlineKeyboardButton(text="🇹🇷 TRY", callback_data="exchange_try")],
        [InlineKeyboardButton(text="🇦🇪 AED", callback_data="exchange_aed"), InlineKeyboardButton(text="🇦🇫 AFN", callback_data="exchange_afn")],
        [InlineKeyboardButton(text="🇰🇬 KGS", callback_data="exchange_kgs"), InlineKeyboardButton(text="🇰🇿 KZT", callback_data="exchange_kzt")],
        [InlineKeyboardButton(text="🇹🇯 TJS", callback_data="exchange_tjs"), InlineKeyboardButton(text="🇹🇲 TMT", callback_data="exchange_tmt")],
        [InlineKeyboardButton(text="⬅ Orqaga", callback_data="back_to_main")]
    ])
    return kb
