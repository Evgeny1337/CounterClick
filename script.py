import requests
import json

# 'https://t.me/lasteraevgen_bot'
#  https://vk.cc/cD7p6a

def is_shorten_link(url):
    pass

def count_clicks(token, link):
    shortened_link = link.split('vk.cc/')[1]
    params = {'access_token':token,'key':shortened_link,'v':'5.199'}
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
    token = ''
    user_url = input("Введите ссылку:\n")
    short_url = None
    try:
        short_url = shorten_link(token, user_url)
    except Exception:
        print("Возникла ошибка")
    if(short_url):
        print('Сокращенная ссылка: ',short_url)
    try:
        views = count_clicks(token,short_url)
        print('Количество переходов: ',views[0]['views'])
    except Exception:
        print("Возникла ошибка")

    


if __name__ == '__main__':
    main()
