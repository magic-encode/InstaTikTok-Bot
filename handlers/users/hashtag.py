from loader import dp
from aiogram import types


@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['eur', 'usd'])
async def hashtag_handler(msg: types.Message):
    await msg.answer('Yee, akang kuchaydiyu !!!')




