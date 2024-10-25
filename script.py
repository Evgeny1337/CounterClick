import requests
import json
from urllib.parse import urlparse
from dotenv import load_dotenv
import os
load_dotenv()

def is_shorten_link(url):
    netloc = urlparse(url).netloc
    if(netloc == 'vk.cc'):
        return True
    return False



def count_clicks(token, link):
    shortened_link = urlparse(link).path[1:]
    params = {'access_token':token,'key':shortened_link,'v':'5.199','interval':'forever'}
    response = requests.get('https://api.vk.ru/method/utils.getLinkStats',params=params)
    response.raise_for_status()
    views = response.json()['response']['stats']
    return views

def shorten_link(token, url):
    params = {'access_token':token,'url':url,'v':'5.199','private':0}
    response = requests.get('https://api.vk.ru/method/utils.getShortLink',params=params)
    response.raise_for_status()
    short_url = response.json()['response']['short_url']
    return short_url
    

def main():
    token =  os.environ.get('TOKEN')
    user_url = input("Введите ссылку:\n")
    if(is_shorten_link(user_url)):
        try:
            views = count_clicks(token,user_url)
        except Exception:
            print("Возникла ошибка")
        if(views):
            print('Количество переходов: ',views[0]['views'])
    else:
        try:
            short_url = shorten_link(token, user_url)
        except Exception:
            print("Возникла ошибка")
        if(short_url):
            print('Сокращенная ссылка: ',short_url)

    

if __name__ == '__main__':
    main()
