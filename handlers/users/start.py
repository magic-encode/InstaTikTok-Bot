from cgitb import text
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


# @dp.message_handler(CommandStart(deep_link='men_uz'))
# async def bot_start(message: types.Message):
#     args = message.get_args()
#     text = f"Salom, {message.from_user.full_name}! \n"
#     text += f"Sizni {args} tavsiya qildi.."
#     await message.answer(text)
    
@dp.message_handler(commands=('start'))
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! \nYouTubeni va Instagramni yoki TikTokni linkini tashlang sizga videosini va musiqasini tashlab beraman..")