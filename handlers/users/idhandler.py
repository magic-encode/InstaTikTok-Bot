from loader import dp
from aiogram import types
from aiogram.dispatcher import filters


SUPERUSERS = [900574498, 32323412]
QORAROYXAT = [1313311, 13131131]

# @dp.message_handler(filter.IDFilter(chat_id=SUPERUSERS))
@dp.message_handler(chat_id='900574498', commands='start')
async def id_filter(msg: types.Message):
    await msg.answer('Xush kelibsz, SuperUSER')



