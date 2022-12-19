from loader import dp
from aiogram import types
from aiogram.dispatcher import filters



@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    await msg.answer('Bu nima rasm?')
    
    
@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def photo_handler(msg: types.Message):
    await msg.answer('Qaytarvor yaxshi eshitmadm!!')
    

@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def photo_handler(msg: types.Message):
    await msg.answer('Bu contakt kerakmas menga boshqa tasha')
    
    
@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def photo_handler(msg: types.Message):
    await msg.answer('E bachkana bome o\'l')    
    
    