import os
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


def send_notification_via_bot(message):
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']
    bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    telegram_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}.'
    response = requests.get(telegram_url)
    response.raise_for_status()


def has_tickets():
    cookies = {
        '__ddg1_': 'pnUS0DjQQKVVle7xl4Qc',
        'BITRIX_SM_kernel': '-crpt-kernel_0',
        'tmr_lvid': 'bc5b35ca898bbc68df2a9eba6d67fa57',
        'tmr_lvidTS': '1723452336624',
        'BX_USER_ID': '541f5efd628012af674e57a34b9e5949',
        '_ym_uid': '1698387524683105062',
        '_ym_d': '1723452337',
        '_ym_isad': '1',
        'domain_sid': 'PY0dpZ8nhmDAa8ERTPECJ%3A1723452342526',
        'travel_page_opened': '1',
        'transfer_train_hash': '%5B%5D',
        '_ym_visorc': 'b',
        'PHPSESSID': '6R0ss4GLi3zVDFhjfmQP12UamhIMUGrH',
        'search_stations': '2078001%2A%D0%A1%D0%B8%D0%BC%D1%84%D0%B5%D1%80%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C%2C2000000%2A%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0',
        'cookie_attention_confirmed': '1',
        'BITRIX_SM_kernel_0': 'GboPhp3oQKvkUGeKufaKiEsyqXXBKpFrjqHo3_YhVLCjuzajrxiCa3A_XnNdj1W62I7qZYc9HUOPo9nX5L1iZkRan1FxZ1gJHMXRfUZXacJIzYqrGX5strChZbGJN3JdsOyP-e8N6UeJoqw_wx6Yd_4ganeWNsnDOAuzQB7LKRmbD7kHyPQG0nAfz6mXKL6tETQKO7BhaHvvlFvvVfKdhkY42xQ9OFa5oHoiLLbcRizWUQqafDitPvVSc3jqd7VmsNyQ4n0RKC564lPGTEyUSKDIpNGUljDWmqjXJFbMv4Jl2w-P8AKOZGNit9ywcZjtSDBYy00UlNKjweOVSIlnGX92JY3-zXsciKDgKhr59gu85F6gCgKg3z4XjK7Yzetgaw_1GghHyXu4SMJ8qt8-CiCSygWFL8EZFAp_w8j5eAS-6ayeClh-8VjH_7x12sXKUVKqnN4xuOzOuqH1bqd3gsMGlq9how4kANozCICNiEbtgxN9ntXZbbtwa6Lgq0VwVNAe4uEJXLUl7DlKJr-VpbFd_YSrVQnuEgpihC-RkTA2-FTwQ5Ki9nYbMGNevsangKJCipMSe3MA8aE43AXL30AfApcX5gaz9v34dC32aVITVoMMR5nPlzV7RFMJ6naqZa95OJNZRJGskMetr6J5mqQ2oAsz_nKZaUxfpoXp5Pp9HvF3Tp3agkX1_RoyazRiz7rODUVWD9nY6N2i8UsUO7Z8oEg1NqgBrLDxrszRXBN6Ai8',
        'tmr_detect': '1%7C1723455925374',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'bx-ajax': 'true',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '__ddg1_=pnUS0DjQQKVVle7xl4Qc; BITRIX_SM_kernel=-crpt-kernel_0; tmr_lvid=bc5b35ca898bbc68df2a9eba6d67fa57; tmr_lvidTS=1723452336624; BX_USER_ID=541f5efd628012af674e57a34b9e5949; _ym_uid=1698387524683105062; _ym_d=1723452337; _ym_isad=1; domain_sid=PY0dpZ8nhmDAa8ERTPECJ%3A1723452342526; travel_page_opened=1; transfer_train_hash=%5B%5D; _ym_visorc=b; PHPSESSID=6R0ss4GLi3zVDFhjfmQP12UamhIMUGrH; search_stations=2078001%2A%D0%A1%D0%B8%D0%BC%D1%84%D0%B5%D1%80%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C%2C2000000%2A%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; cookie_attention_confirmed=1; BITRIX_SM_kernel_0=GboPhp3oQKvkUGeKufaKiEsyqXXBKpFrjqHo3_YhVLCjuzajrxiCa3A_XnNdj1W62I7qZYc9HUOPo9nX5L1iZkRan1FxZ1gJHMXRfUZXacJIzYqrGX5strChZbGJN3JdsOyP-e8N6UeJoqw_wx6Yd_4ganeWNsnDOAuzQB7LKRmbD7kHyPQG0nAfz6mXKL6tETQKO7BhaHvvlFvvVfKdhkY42xQ9OFa5oHoiLLbcRizWUQqafDitPvVSc3jqd7VmsNyQ4n0RKC564lPGTEyUSKDIpNGUljDWmqjXJFbMv4Jl2w-P8AKOZGNit9ywcZjtSDBYy00UlNKjweOVSIlnGX92JY3-zXsciKDgKhr59gu85F6gCgKg3z4XjK7Yzetgaw_1GghHyXu4SMJ8qt8-CiCSygWFL8EZFAp_w8j5eAS-6ayeClh-8VjH_7x12sXKUVKqnN4xuOzOuqH1bqd3gsMGlq9how4kANozCICNiEbtgxN9ntXZbbtwa6Lgq0VwVNAe4uEJXLUl7DlKJr-VpbFd_YSrVQnuEgpihC-RkTA2-FTwQ5Ki9nYbMGNevsangKJCipMSe3MA8aE43AXL30AfApcX5gaz9v34dC32aVITVoMMR5nPlzV7RFMJ6naqZa95OJNZRJGskMetr6J5mqQ2oAsz_nKZaUxfpoXp5Pp9HvF3Tp3agkX1_RoyazRiz7rODUVWD9nY6N2i8UsUO7Z8oEg1NqgBrLDxrszRXBN6Ai8; tmr_detect=1%7C1723455925374',
        'origin': 'https://grandtrain.ru',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://grandtrain.ru/tickets/2078001-2000000/30.09.2024/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    data = {
        'from': '34',
        'to': '19',
        'forward_date': '30.08.2024',
        'backward_date': '',
        'multimodal': '0',
        'pagestyle': 'tav',
        'timeout': '5',
    }

    response = requests.post(
        'https://grandtrain.ru/local/components/oscompany/train.select/ajax.php',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    # response = requests.get("https://grandtrain.ru/tickets/2078001-2000000/30.09.2024/")
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    return soup.findAll("div", class_="train_seats_count")


def main():
    load_dotenv()
    attempts = 0
    send_notification_via_bot("Начинаем мониторить")
    while True:
        try:
            time.sleep(60)
            if has_tickets():
                send_notification_via_bot("Есть места на 30 число")
                time.sleep(600)
            attempts += 1
            if attempts % 1000 == 0:
                send_notification_via_bot(f"Бот жив, продолжает вести наблюдение, попыток {attempts}")
        except Exception as e:
            send_notification_via_bot(str(e))


if __name__ == '__main__':
    main()
