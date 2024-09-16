import os
import time

import requests
from dotenv import load_dotenv


def send_notification_via_bot(message):
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']
    bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    telegram_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}.'
    response = requests.get(telegram_url)
    response.raise_for_status()


def has_tickets():
    cookies = {
        '_ym_uid': '1726474161958694175',
        '_ym_d': '1726474161',
        '_ym_isad': '1',
        '_ym_visorc': 'b',
        'jsonFormat': 'true',
        'accessible': 'false',
        'LANG_SITE': 'ru',
        'uwyii': '766766e4-bd81-44d0-688d-845e0915e33d',
        'lang': 'ru',
        'LtpaToken2': 'SEJKRhSwtaNzKOEqoE5gobm6q4cyW0fVWrHaDiKgp7hvreX8es2AJi+Q1viRvpvZGxUcnhA3Py5VK725xh30yEf/zz34/V5qExv4kk/GtF46jCZ5qL/ey42QMvQjSZbYulodYjwn+ausl3gMCtDHyi4potQdC3jRYaQNXwwlKZ6kT/efQbaUnzZMHlsigyJmE2D4F6fWoxpumAZ09QB3vNUe1YmXjHpOxW9hxRL1JdDiPgSsG6Qhn3JsXb+cTTAxF1AlktLDH7c0/q0gh1JSshmeZBb3ZR8aNtl9AiSMEtrkncgwkgMNnSRqVJHAUO+neHEz11r18uwtDzzr1BkN5ak49YaIwS9F06fJbJoG9IPECEniQOZM6UA+z02HpJoo/ZRoHkZeXRO6Yo+9SKLuRgcvfmdHMsge1eOjPy59LYSl4UkAfyGXg8APW8YAhij95E6O6ItP7OJxkih+IE1WAlAHXNPk5umEJYmgkUWY9UpsR5YHH5i8c8OK7aTd6+GRoO/VGAEhritz5Ed4niCEBAoPfHzUYx8rxLg337nMe7niUsYi6TXzF/5WMxIIAP+kkgKfPAwjE44hSwnM6HdRC+YYgeTUpNdoaQOtatz4RoY=',
        'session-cookie': '17f5abbf5c7a2f7d55489a5ad00b08454fb1b0fbbcf50c72716227a74a457981659a2c73da2abe7863d4ea4e3054bc72',
        'oxxfgh': 'e15eb5e4-a1a7-4c28-9b59-1f922fae52a9%236%2386400000%2330000%231800000%2322900',
        'oxxLS': 'e15eb5e4-a1a7-4c28-9b59-1f922fae52a9_5',
        'uwyiert': '990af9f7-017a-4cf6-2fa8-b21dd0ae29d9',
        'JSESSIONID': '8A96FE447875B36E47C9B54FE3239A2B',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJsdHBhVG9rZW4iOiJTRUpLUmhTd3RhTnpLT0Vxb0U1Z29ibTZxNGN5VzBmVldySGFEaUtncDdodnJlWDhlczJBSmkrUTF2aVJ2cHZaR3hVY25oQTNQeTVWSzcyNXhoMzB5RWYvenozNC9WNXFFeHY0a2svR3RGNDZqQ1o1cUwvZXk0MlFNdlFqU1piWXVsb2RZanduK2F1c2wzZ01DdERIeWk0cG90UWRDM2pSWWFRTlh3d2xLWjZrVC9lZlFiYVVuelpNSGxzaWd5Sm1FMkQ0RjZmV294cHVtQVowOVFCM3ZOVWUxWW1YakhwT3hXOWh4UkwxSmREaVBnU3NHNlFobjNKc1hiK2NUVEF4RjFBbGt0TERIN2MwL3EwZ2gxSlNzaG1lWkJiM1pSOGFOdGw5QWlTTUV0cmtuY2d3a2dNTm5TUnFWSkhBVU8rbmVIRXoxMXIxOHV3dER6enIxQmtONWFrNDlZYUl3UzlGMDZmSmJKb0c5SVBFQ0VuaVFPWk02VUErejAySHBKb28vWlJvSGtaZVhSTzZZbys5U0tMdVJnY3ZmbWRITXNnZTFlT2pQeTU5TFlTbDRVa0FmeUdYZzhBUFc4WUFoaWo5NUU2TzZJdFA3T0p4a2loK0lFMVdBbEFIWE5QazV1bUVKWW1na1VXWTlVcHNSNVlISDVpOGM4T0s3YVRkNitHUm9PL1ZHQUVocml0ejVFZDRuaUNFQkFvUGZIelVZeDhyeExnMzM3bk1lN25pVXNZaTZUWHpGLzVXTXhJSUFQK2trZ0tmUEF3akU0NGhTd25NNkhkUkMrWVlnZVRVcE5kb2FRT3RhdHo0Um9ZPSIsImxvZ2luIjoiMTA5MzkwMSIsImVtYWlsIjoidml0YWxpLmJhcmFub3ZAZ21haWwuY29tIiwidXNlcl9pZCI6NTI3MzM5NCwiYWN0aXZlIjp0cnVlLCJzZXNzaW9uS2V5IjoiQXV0aF9zdmMtZmM0N2Q1YTViMzg1NzQ0YjIzNzg1MTIzZWRiYWQ2MDk2YzJkODA5ZjQzZjFlOTliZGE1MzQxNDg5MDdlMjQ3MSIsImNvcnBvcmF0ZSI6ZmFsc2UsImZpbHRlcl9jYXJyaWVycyI6W10sImtzaWQiOiJlMTVlYjVlNC1hMWE3LTRjMjgtOWI1OS0xZjkyMmZhZTUyYTlfMCIsImlzcyI6InRpY2tldC5yemQucnUiLCJleHAiOjE3MjY1NjA4NTN9.D8YbYjVFBVihr00ktsFCifoygXRtJlKOL9qiT2nlaZE',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': '_ym_uid=1726474161958694175; _ym_d=1726474161; _ym_isad=1; _ym_visorc=b; jsonFormat=true; accessible=false; LANG_SITE=ru; uwyii=766766e4-bd81-44d0-688d-845e0915e33d; lang=ru; LtpaToken2=SEJKRhSwtaNzKOEqoE5gobm6q4cyW0fVWrHaDiKgp7hvreX8es2AJi+Q1viRvpvZGxUcnhA3Py5VK725xh30yEf/zz34/V5qExv4kk/GtF46jCZ5qL/ey42QMvQjSZbYulodYjwn+ausl3gMCtDHyi4potQdC3jRYaQNXwwlKZ6kT/efQbaUnzZMHlsigyJmE2D4F6fWoxpumAZ09QB3vNUe1YmXjHpOxW9hxRL1JdDiPgSsG6Qhn3JsXb+cTTAxF1AlktLDH7c0/q0gh1JSshmeZBb3ZR8aNtl9AiSMEtrkncgwkgMNnSRqVJHAUO+neHEz11r18uwtDzzr1BkN5ak49YaIwS9F06fJbJoG9IPECEniQOZM6UA+z02HpJoo/ZRoHkZeXRO6Yo+9SKLuRgcvfmdHMsge1eOjPy59LYSl4UkAfyGXg8APW8YAhij95E6O6ItP7OJxkih+IE1WAlAHXNPk5umEJYmgkUWY9UpsR5YHH5i8c8OK7aTd6+GRoO/VGAEhritz5Ed4niCEBAoPfHzUYx8rxLg337nMe7niUsYi6TXzF/5WMxIIAP+kkgKfPAwjE44hSwnM6HdRC+YYgeTUpNdoaQOtatz4RoY=; session-cookie=17f5abbf5c7a2f7d55489a5ad00b08454fb1b0fbbcf50c72716227a74a457981659a2c73da2abe7863d4ea4e3054bc72; oxxfgh=e15eb5e4-a1a7-4c28-9b59-1f922fae52a9%236%2386400000%2330000%231800000%2322900; oxxLS=e15eb5e4-a1a7-4c28-9b59-1f922fae52a9_5; uwyiert=990af9f7-017a-4cf6-2fa8-b21dd0ae29d9; JSESSIONID=8A96FE447875B36E47C9B54FE3239A2B',
        'Origin': 'https://ticket.rzd.ru',
        'Pragma': 'no-cache',
        'Referer': 'https://ticket.rzd.ru/booking/rail/007%D0%9C/service',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sentry-trace': 'ba7c26db19f440c6a8f293a868ce023f-b1800d38345c9917-1',
    }

    params = {
        'service_provider': 'B2B_RZD',
        'isBonusPurchase': 'false',
    }

    json_data = {
        'OriginCode': '2000006',
        'DestinationCode': '2100001',
        'Provider': 'P1',
        'DepartureDate': '2024-09-27T22:12:00',
        'TrainNumber': '007М',
        'SpecialPlacesDemand': 'StandardPlacesAndForDisabledPersons',
        'OnlyFpkBranded': False,
        'CarIssuingType': 'All',
    }

    response = requests.post(
        'https://ticket.rzd.ru/apib2b/p/Railway/V1/Search/CarPricing',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    # response = requests.get("https://grandtrain.ru/tickets/2078001-2000000/30.09.2024/")
    response.raise_for_status()
    places = []
    for car in response.json()['Cars']:
        if not 'invalid' in car['CarPlaceType'].lower() and int(car['FreePlaces']) % 2 == 1:
            places.append((car['CarNumber'], car['FreePlaces']))
    return places


def main():
    has_tickets()
    load_dotenv()
    attempts = 0
    send_notification_via_bot("Начинаем мониторить")
    while True:
        try:
            time.sleep(60)
            result = has_tickets()
            if len(result) > 0:
                send_notification_via_bot(f"Есть места на 27 число: {result} ")
                time.sleep(600)
            attempts += 1
            if attempts % 1000 == 0:
                send_notification_via_bot(f"Бот жив, продолжает вести наблюдение, попыток {attempts}")
        except Exception as e:
            send_notification_via_bot(str(e))


if __name__ == '__main__':
    main()
