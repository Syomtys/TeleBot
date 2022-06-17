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

    # print(message)
    search = message.text
    filename = search
    search = search.replace(' ', '%20')
    # search = search.replace(' ', '+')
    # url = f'https://stock.adobe.com/ru/search/images?filters%5Bcontent_type%3Aillustration%5D=1&filters%5Bcontent_type%3Azip_vector%5D=1&filters%5Bcontent_type%3Aimage%5D=1&filters%5Borientation%5D=vertical&filters%5Bcontent_type%3Aphoto%5D=1&k={search}&order=relevance&safe_search=1&limit=100&search_type=usertyped&search_page=1&acp=&aco={search}&get_facets=1'
    url = f'https://yandex.ru/images/search?text={search}&isize=large&iorient=vertical'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # html_new = str(soup)
    fn = 'pic/'+filename
    os.mkdir(fn)
    # images = soup.find_all('a', class_='serp-item__link')
    images = soup.find_all('img')
    # print(images)

    num = 0
    media = types.MediaGroup()

    for image in images:
        num += 1
        image_src = image['src']
        if num >= 2 and num <=10:
            urlimg = 'https://'+image_src[2:]
            # print(urlimg)
            # req = requests.get(urlimg)
            # html = req.text
            # tree = etree.HTML(html)
            # content = tree.xpath('/html/body/div[13]/div[2]/div/div/div/div[3]/div/div[3]/div/div/div[1]/div[4]/div[1]/a')
            # print(content)
            # soup = BeautifulSoup(req.content, 'html.parser')
            # print(soup)
            # hromg = soup.find_all('img', class_='MMImage-Origin')
            # print(hromg)
            # image_full_src = hromg['href']
            # print(image_full_src)

            # print('----')
            f = fn + '/' + str(num) + '.jpg'
            urllib.request.urlretrieve(urlimg, f)
            # print(f)
            media.attach_photo(types.InputFile(f))
            # await bot.send_photo(message.chat.id, types.InputFile(f))
    await bot.send_media_group(message.chat.id, media=media)
    print('send imgs user')
    shutil.rmtree(fn)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)