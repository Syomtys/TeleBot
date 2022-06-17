from aiogram import Bot, Dispatcher, executor, types
import logging
import asyncio

API_TOKEN = '5425767916:AAGoAjS-TxQ4lXNDcC3-ojGRdBF7SEgc6s0'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def mg():

    msg = input()
    id = '728473742'
    # for i in range(1):
    await bot.send_message(id,msg)

asyncio.run(mg())