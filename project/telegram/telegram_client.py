import requests

from project.telegram import *


class TelegramClient:
    def __init__(self):
        self.url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    def send(self, message: str):
        requests.post(self.url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message}, timeout=10)