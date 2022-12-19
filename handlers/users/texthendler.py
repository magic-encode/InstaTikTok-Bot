from operator import contains
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Text



@dp.message_handler(Text(contains='assalom' , ignore_case=True))
@dp.message_handler(Text(equals='assalom alaykum' , ignore_case=True))
async def txt_filter(msg: types.Message):
    await msg.answer('Vaalykum Assalom')


#boshqa parametrlar
#  startwith
#  endswith


