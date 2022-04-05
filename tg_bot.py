from parse import *
from tg_tkn import token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from igroman import get_all_info
bot = Bot(token=token,parse_mode = types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Film.ru","Igromania"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Choose the site",reply_markup = keyboard)

# @dp.message_handler(commands="all_news")
@dp.message_handler(Text(equals='Film.ru'))
async def get_all_news(message: types.Message):
    for i in range(len(box_for_info_text)-1, -1, -1):
        await bot.send_photo(message.chat.id, images[i], parse_mode="HTML")
        await message.answer(f"<b>{b[i]}</b>" + box_for_info_text[i], parse_mode="HTML")

@dp.message_handler(Text(equals='Igromania'))
async def get_igromania_news(message: types.Message):
    await message.answer("Data processing...")
    kast_list = get_all_info()
    for mes in kast_list:
        await bot.send_photo(message.chat.id, mes['img'],parse_mode="HTML")
        await message.answer(f"<b>{mes['title']}</b>" + '\n'+ '\n' + mes['text'] + '\n')
if __name__ == "__main__":
    executor.start_polling(dp)
