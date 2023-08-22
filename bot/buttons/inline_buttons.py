import json

import requests
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def categorys_button():
    design = []
    categories = requests.get("http://127.0.0.1:8000/categories/").content.decode('utf-8')
    for category in json.loads(categories):
        design.append([InlineKeyboardButton(text=category['name'], callback_data=category['id'])])
    return InlineKeyboardMarkup(inline_keyboard=design)


async def product_button(id_: int):
    design = []
    products = requests.get(f"http://127.0.0.1:8000/category-food/{id_}/").content.decode('utf-8')
    for product in json.loads(products):
        design.append([InlineKeyboardButton(text=product['name'], callback_data=product['id'])])
    return InlineKeyboardMarkup(inline_keyboard=design)
