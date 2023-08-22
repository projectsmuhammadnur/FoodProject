import json

import requests
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.buttons.text import back, order


async def main_menu_buttons():
    design = [
        [order]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def phone_number():
    design = [[KeyboardButton(text="Telefon raqamni yuborish📲", request_contact=True)]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def location():
    design = [[KeyboardButton(text="Joylashuvni yuborish📍", request_location=True)], [back]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def back_categories():
    design = [[back]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, row_width=2)
