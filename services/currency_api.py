import aiohttp
import requests

async def get_currency_data():
    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


CURRENCY_URL = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

async def get_currency():
    response = requests.get(CURRENCY_URL)
    data = response.json()
    return {item['Ccy']: item for item in data}

async def convert_currency(amount: float, currency_code: str):
    currencies = await get_currency()
    if currency_code not in currencies:
        return None
    rate = float(currencies[currency_code]['Rate'].replace(',', ''))
    return amount * rate, rate
