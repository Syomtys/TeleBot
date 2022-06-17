import logging
import shutil
from aiogram import Bot, Dispatcher, executor, types
import os
import requests
from bs4 import BeautifulSoup
import urllib.request


API_TOKEN = '5425767916:AAGoAjS-TxQ4lXNDcC3-ojGRdBF7SEgc6s0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Ты пишешь слово,\nя отправляю несколько картинок\n по твоему запросу.")

@dp.message_handler()
async def echo(message: types.Message):

    usinfo = str(message.chat.id) + ':' + message.chat.first_name + ':' + message.chat.username + ':' + message.text
    print(usinfo)

    f = open('usrs', 'r+')
    f.read()
    f.write(usinfo+ '\n')
    f.close()

    search = message.text
    filename = search
    search = search.replace(' ', '%20')
    url = f'https://yandex.ru/images/search?text={search}&isize=large&iorient=vertical'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    fn = 'pic/'+filename
    os.mkdir(fn)
    images = soup.find_all('div', role='listitem')
    # print(images)

    num = 0
    media = types.MediaGroup()

    for image in images:
        num += 1
        if num >= 2 and num <=5:
            image_src = image['data-bem']
            spl = image_src.split('img_href')[-1:]
            spl = spl[0].split('useProxy')[:-1]
            spl = spl[0][3:]
            image_src = spl[:-3]
            print(image_src)
            # urlimg = 'https://'+image_src[2:]
            f = fn + '/' + str(num) + '.jpg'
            # if requests.get(image_src).status_code == 200:
            r = requests.get(image_src)
            print(r.status_code)
            if r.status_code == 200:
                # urllib.request.urlretrieve(image_src, f)
                with open(f, 'wb') as outfile:
                    outfile.write(r.content)
                media.attach_photo(types.InputFile(f))
            else:
                print('photo hueta')

    await bot.send_media_group(message.chat.id, media=media)
    print('send imgs user')
    shutil.rmtree(fn)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)