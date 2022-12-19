from loader import dp
from tiktok import tk
from aiogram import types

from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@dp.message_handler(Text(startswith='https://vt.tiktok.com/'))
@dp.message_handler(Text(startswith='https://www.tiktok.com/'))
async def tests(message:types.Message):
    natija = tk(message.text)
    qoshiq = natija['music']
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text = "Musiqasini yuklab olish..",
            url="{}". format(qoshiq))]
        ]
    )
    await message.answer_audio(natija['video'],reply_markup=btn)

    
    
    