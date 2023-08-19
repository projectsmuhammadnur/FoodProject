from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def phone_number():
    design = [[KeyboardButton(text="Telefon raqamni yuborish📲", request_contact=True)]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def location():
    design = [[KeyboardButton(text="Joylashuvni yuborish📍", request_location=True)]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)