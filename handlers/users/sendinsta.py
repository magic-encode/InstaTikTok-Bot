from loader import dp
from aiogram import types

from instagram import instadown

from aiogram.dispatcher.filters import Text


@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media(message:types.Message):
    
    try:
        link = message.text
        data = instadown(link=link)
        if data == 'Tashlagan linkda xatolik bor...':
            await  message.answer('Iltimos boshqa link tashlang, bu link ishlamaydi..')
    
        else:
            if data['type'] == 'image':
                await message.answer_photo(photo=data['media'])
            elif data['type'] == 'video':
                await message.answer_video(video=data['media'])
                
            elif data['type'] == 'carousel':
                for i in data['media']:
                    await message.answer_document(document=i)
            elif data['type'] == 'story-video':
                for i in data['media']:
                    await message.answer_document(document=i)
            else:
                await  message.answer('Iltimos boshqa link tashlang, bu link ishlamaydi..')
    except:
        await  message.answer('Iltimos boshqa link tashlang video hajmi yuqori..')
                    
    
            
        