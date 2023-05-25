import logging

from decouple import config
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = config('TELEGRAM_BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт я перший бот на Python на курсі Hillel")


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == 'Привіт':
        await message.answer('Привіт, як справи?')
    elif message.text == 'Добре':
        await message.answer('Це добре')
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)