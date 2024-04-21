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
    response = requests.get("https://grandtrain.ru/tickets/2000000-2078001/19.06.2024/028%D0%A7/")
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    return len([s.find('span') for s in soup.findAll('div', class_='car-class__fare-item') if
                'нижн' in s.find('span').text]) > 0


def main():
    load_dotenv()
    successive_attempts = 0
    send_notification_via_bot("Начинаем мониторить")
    while True:
        try:
            time.sleep(60)
            if has_tickets():
                send_notification_via_bot("Есть нижнее место")
            successive_attempts += 1
            if successive_attempts % (60 * 24) == 0:
                send_notification_via_bot("Бот жив, продолжает вести наблюдение")
        except Exception as e:
            send_notification_via_bot(str(e))


if __name__ == '__main__':
    main()
