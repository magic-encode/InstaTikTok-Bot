# from aiogram import types
# from loader import dp


# from pytube import YouTube
# from aiogram.dispatcher.filters import Text

# @dp.message_handler(Text(startswith="http"))
# async def get_audio(message: types.Message):
#     link=message.text
#     from io import BytesIO
#     buffer=BytesIO()
#     url=YouTube(link)
#     if url.check_availability() is None:
#         audio=url.streams.get_audio_only()
#         audio.stream_to_buffer(buffer=buffer)
#         buffer.seek(0)
#         filename=url.title
#         await message.answer_audio(audio=buffer, caption=filename)
#     else:
#         await message.answer('Xatolik')
        
        
import logging
from io import BytesIO
from aiogram import Bot, Dispatcher, executor, types
from pytube import YouTube

API_TOKEN = '5472463935:AAGLQHHdLtLJEAYRg_PttD_DRhKT64vS1oI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

from aiogram.dispatcher.filters import Text

@dp.message_handler(Text(startswith="http"))
async def get_audio(message: types.Message):
    link=message.text
    buffer=BytesIO()
    url=YouTube(link)
    if url.check_availability() is None:
        audio=url.streams.get_audio_only()
        audio.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        filename=url.title
        await message.answer_audio(audio=buffer, caption=filename)
    else:
        await message.answer('Xatolik')

if __name__ == '__main__':
    executor.start_polling(dp)