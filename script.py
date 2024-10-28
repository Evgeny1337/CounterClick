import requests
import json
from urllib.parse import urlparse
from dotenv import load_dotenv
import os

def is_shorten_link(url):
    netloc = urlparse(url).netloc
    return netloc == 'vk.cc'



def count_clicks(token, link):
    shortened_link = urlparse(link).path[1:]
    params = {'access_token':token,'key':shortened_link,'v':'5.199','interval':'forever'}
    response = requests.get('https://api.vk.ru/method/utils.getLinkStats',params=params)
    response.raise_for_status()
    if "error" in response.json():
        raise requests.exceptions.HTTPError()
    views = response.json()['response']['stats']
    return views

def shorten_link(token, url):
    params = {'access_token':token,'url':url,'v':'5.199','private':0}
    response = requests.get('https://api.vk.ru/method/utils.getShortLink',params=params)
    response.raise_for_status()
    if "error" in response.json():
        raise requests.exceptions.HTTPError()
    short_url = response.json()['response']['short_url']
    return short_url
    

def main():
    load_dotenv()
    try:
        token =  os.environ['VK_TOKEN']
    except KeyError:
        raise KeyError('Переменная TOKEN не найдена в окружении')
    user_url = input("Введите ссылку:\n")
    if is_shorten_link(user_url):
        try:
            views = count_clicks(token,user_url)
        except requests.exceptions.HTTPError:
            raise requests.exceptions.HTTPError('Ошибка url')
        else:
            print('Количество переходов: ',views[0]['views'])
    else:
        try:
            short_url = shorten_link(token, user_url)
        except requests.exceptions.HTTPError:
            raise requests.exceptions.HTTPError('Ошибка url')
        else:
            print('Сокращенная ссылка: ',short_url)
            

    

if __name__ == '__main__':
    main()
