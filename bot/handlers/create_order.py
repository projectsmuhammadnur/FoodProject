from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ContentType
from geopy import Nominatim

from bot.buttons.inline_buttons import categorys_button, product_button
from bot.buttons.reply_buttons import location, back_categories
from bot.buttons.text import order, back
from bot.dispatcher import dp

geolocator = Nominatim(user_agent="myGeocoder")


@dp.message_handler(Text(order))
async def order_create(msg: types.Message, state: FSMContext):
    await state.set_state('location')
    await msg.answer(text="<b>Buyurtmani davom ettirish uchun iltimos lokatsiyangizni yuboring 🗺</b>",
                     parse_mode="HTML",
                     reply_markup=await location())


@dp.message_handler(state='location', content_types=ContentType.LOCATION)
async def location_handler(msg: types.Message, state: FSMContext):
    lat = msg.location.latitude
    lon = msg.location.longitude
    location = geolocator.reverse((lat, lon), exactly_one=True)
    async with state.proxy() as data:
        data['location'] = location.address
    await state.set_state('categories')
    await msg.answer(text=f"<b>Sizning manzilingiz: {location.address}</b>", parse_mode="HTML",
                     reply_markup=await back_categories())
    await msg.answer(text=f"<b>Bo'limlardan birini tanlang</b>", parse_mode="HTML",
                     reply_markup=await categorys_button())


@dp.message_handler(Text(back), state='categories')
async def order_create(msg: types.Message, state: FSMContext):
    await state.set_state('location')
    await msg.answer(text="<b>Yangi lokatsiyangizni yuboring 🗺</b>", parse_mode="HTML",
                     reply_markup=await location())


@dp.callback_query_handler(state='categories')
async def categories_handler(call: types.CallbackQuery, state: FSMContext):
    await state.set_state("product")
    await call.message.edit_text(text=f"<b>Mahsulotlardan birini tanlang</b>", parse_mode="HTML",
                                 reply_markup=await product_button(int(call.data)))


@dp.message_handler(Text(back), state='product')
async def order_create(msg: types.Message, state: FSMContext):
    await state.set_state('categories')
    await msg.answer(text=f"<b>Bo'limlardan birini tanlang</b>", parse_mode="HTML",
                     reply_markup=await categorys_button())
