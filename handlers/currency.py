from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from texts import TEXTS

router = Router()

# --- STATES ---
class CurrencyStates(StatesGroup):
    waiting_for_currency = State()
    waiting_for_amount = State()

# --- VALYUTA TUGMALARI ---
def get_currency_list_keyboard(lang_code):
    currency_buttons = [
        [InlineKeyboardButton(text="USD", callback_data="currency_usd")],
        [InlineKeyboardButton(text="EUR", callback_data="currency_eur")],
        [InlineKeyboardButton(text="RUB", callback_data="currency_rub")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=currency_buttons)

# --- 1. BOSQICH ---
@router.callback_query(F.data == "calculate_currency")
async def ask_currency(call: CallbackQuery, state: FSMContext):
    lang = call.from_user.language_code or "uz"
    await call.message.edit_text(
        TEXTS[lang]["choose_currency"],
        reply_markup=get_currency_list_keyboard(lang)
    )
    await state.set_state(CurrencyStates.waiting_for_currency)

# --- 2. BOSQICH ---
@router.callback_query(F.data.startswith("currency_"), CurrencyStates.waiting_for_currency)
async def ask_amount(call: CallbackQuery, state: FSMContext):
    currency = call.data.split("_")[1]  # usd, eur, rub
    await state.update_data(currency=currency)
    lang = call.from_user.language_code or "uz"
    await call.message.edit_text(TEXTS[lang]["enter_amount"])
    await state.set_state(CurrencyStates.waiting_for_amount)

# --- 3. BOSQICH ---
@router.message(CurrencyStates.waiting_for_amount)
async def calculate_result(message: Message, state: FSMContext):
    user_data = await state.get_data()
    currency = user_data.get("currency")
    amount_text = message.text.strip()

    try:
        amount = float(amount_text)
    except ValueError:
        await message.answer("Faqat son kiriting!")
        return

    rates = {"usd": 12500, "eur": 13500, "rub": 140}  # 💡 API o'rniga vaqtincha
    result = amount * rates[currency]
    lang = message.from_user.language_code or "uz"
    await message.answer(TEXTS[lang]["result"].format(amount=amount, currency=currency.upper(), result=result))
    await state.clear()
