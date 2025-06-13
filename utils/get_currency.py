import aiohttp

async def get_exchange_rate(code: str) -> str:
    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

    for val in data:
        if val["Ccy"] == code:
            return f"💱 {val['CcyNm_UZ']} ({val['Ccy']}): {val['Rate']} so'm\n📅 {val['Date']}"
    return "Valyuta topilmadi."
