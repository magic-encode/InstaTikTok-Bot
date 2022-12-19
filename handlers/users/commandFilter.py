from ast import arg
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command



@dp.message_handler(Command('til'))
async def changeCity(message: types.Message):
    arg = message.get_command()
    await message.answer(f"Til o'zgardi..")


