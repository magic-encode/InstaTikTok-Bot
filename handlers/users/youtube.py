import logging
from loader import dp
from io import BytesIO
from aiogram import types
from pytube import YouTube
from aiogram.dispatcher.filters import Text

logging.basicConfig(level=logging.INFO)


@dp.message_handler(Text(startswith="https://youtu.be/"))
async def get_audio(message: types.Message):
    link = message.text
    buffer = BytesIO()
    url = YouTube(link)
    if url.check_availability() is None:
        audio = url.streams.get_audio_only()
        audio.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        filename = url.title
        await message.answer_audio(audio=buffer, caption=filename)
    else:
        await message.answer('Xatolik')
