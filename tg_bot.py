from email import utils
from parse import *
from tg_tkn import token
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=token)
dp = Dispatcher(bot)

# ["Сегодня","Все новости"]
# @dp.message_handler(commands="start")
# async def start(message: types.Message):
#     start


@dp.message_handler(commands="all_news")
async def get_all_news(message: types.Message):
    for i in range(len(box_for_info_text)-1, -1, -1):
        await bot.send_photo(message.chat.id, images[i], parse_mode="HTML")
        await message.answer(f"<b>{b[i]}</b>" + box_for_info_text[i], parse_mode="HTML")
if __name__ == "__main__":
    executor.start_polling(dp)
