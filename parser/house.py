import httpx
from parsel import Selector
from aiogram import Router, F, types

parser_router = Router()

MAIN_URL = "https://www.house.kg/snyat"
ORIGINAL_URL = "https://www.house.kg/"


def get_page(url):
    response = httpx.get(url)
    # print("Response", response.status_code, response.url)
    html = Selector(text=response.text)
    return html

def clean_text(text: str):
    if text is None:
        return ""
    text = " ".join(text.split())
    return text.strip().replace("\t", "").replace("\n", "")

def get_house_data(html: Selector):
    houses = html.css("div.listing")
    house_list = []
    for house in houses:
        house_data = {}
        house_data["title"] = clean_text(house.css("div.right-info a::text").get())
        house_data['link'] = (ORIGINAL_URL + clean_text(house.css("a::attr(href)").get()))
        house_data["price"] = clean_text(house.css("div.price ::text").get())
        house_data["som_price"] = clean_text(house.css("div.price-addition ::text").get())
        # house_data["address"] = clean_text(house.css("div.address ::text").get())
        house_list.append(house_data)
    return house_list


@parser_router.callback_query(F.data == "house")
async def house_parser(call: types.CallbackQuery):
    html = get_page(MAIN_URL)
    houses = get_house_data(html)
    for house in houses:
        text = (f"{house['title']}\n"
                f"{house['price']}\n"
                f"{house['som_price']}\n"
                f"{house['link']}")
        await call.message.answer(text)
