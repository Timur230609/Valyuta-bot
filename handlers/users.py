from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from services.currency_api import convert_currency, get_currency_data
from keyboards.main import main_menu_keyboard, exchange_menu_keyboard, main_menu

router = Router()


class ConvertStates(StatesGroup):
    waiting_for_amount = State()

@router.message(F.text == "/start")
async def cmd_start(message: types.Message):
    await message.answer("Assalomu alaykum! Valyuta botga hush kelibsiz!\n📅 Asosiy menyu:", reply_markup=main_menu())

@router.message(F.text == "🏦 Valyuta Kursi")
async def show_currency(message: types.Message):
    data = await get_currency_data()
    kurslar = [
        ("USD", "🇺🇸 AQSH dollari"),
        ("EUR", "🇪🇺 EVRO"),
        ("RUB", "🇷🇺 Rossiya rubli"),
        ("GBP", "🇬🇧 Angliya funt sterlingi"),
        ("CAD", "🇨🇦 Kanada dollari"),
        ("CNY", "🇨🇳 Xitoy yuani"),
        ("KRW", "🇰🇷 Koreya Respublikasi voni"),
        ("TRY", "🇹🇷 Turkiya lirasi"),
        ("AED", "🇦🇪 BAA dirhami"),
        ("AFN", "🇦🇫 Afg’oniston afg’onisi"),
        ("KGS", "🇰🇬 Qirg’iz somi"),
        ("KZT", "🇰🇿 Qozog‘iston tengesi"),
        ("TJS", "🇹🇯 Tojikiston somonisi"),
        ("TMT", "🇹🇲 Turkmaniston manati")
    ]
    msg = "💵 <b>Xorijiy chegaradosh davlatlar valyuta kurslarining O'zbekiston valyutasidagi qiymati!:</b>\n"
    for code, name in kurslar:
        for item in data:
            if item["Ccy"] == code:
                msg += f"\n1 {name}: <b>{item['Rate']} UZS</b>"
                break
    await message.answer(msg)
    
    
    
    
    
    

@router.message(F.text == "🧮 Ayirboshlash")
async def exchange_menu(msg: Message):
    await msg.answer("Qaysi valyutani ayirboshlamoqchisiz?", reply_markup=exchange_menu_keyboard())

@router.callback_query(F.data.startswith("exchange_"))
async def ask_amount(callback: CallbackQuery, state: FSMContext):
    currency = callback.data.split("_")[1].upper()
    await state.update_data(currency=currency)
    await callback.message.edit_text(f"💰 Miqdorni kiriting ({currency}):")
    await state.set_state(ConvertStates.waiting_for_amount)

@router.message(ConvertStates.waiting_for_amount)
async def handle_amount(msg: Message, state: FSMContext):
    user_data = await state.get_data()
    currency = user_data['currency']
    try:
        amount = float(msg.text.replace(',', '.'))
        converted, rate = await convert_currency(amount, currency)
        await msg.answer(f"{amount} {currency} => {converted:.2f} UZS\n1 {currency} = {rate:.2f} UZS")
    except:
        await msg.answer("❌ Noto'g'ri miqdor. Iltimos, son kiriting.")
    await state.clear()

@router.callback_query(F.data == "back_to_main")
async def back_to_main_menu(callback: CallbackQuery):
    await callback.message.edit_text("Asosiy menyu:", reply_markup=None)
    await callback.message.answer("Kerakli bo'limni tanlang:", reply_markup=main_menu_keyboard())

@router.message(F.text == "🏦 Valyuta Kursi")
async def show_rates(msg: Message):
    await msg.answer("💱 Valyuta kurslari hozircha ishlanmoqda... (bu yerga alohida kurslar chiqadi)")

