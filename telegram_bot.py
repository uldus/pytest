from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from pars_syte_1 import get_data
import json
import os

bot = Bot(token="1656709830:AAHqUQjU8IAvm52IFVIfU6qqJyxg9bsGSOI")
#bot = Bot(token=os.getenv("TOKEN"), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["НХЛ", "РФПЛ", "КХЛ"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Результаты сегоднешних матчей", reply_markup=keyboard)


@dp.message_handler(Text(equals="НХЛ"))
async def get_discount_sneakers(message: types.Message):
    await message.answer("Please waiting...")

    await message.answer(get_data())






def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
