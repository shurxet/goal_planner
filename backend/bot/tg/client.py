import os
from bot.tg import GetUpdatesResponse, SendMessageResponse
import requests


class TgClient:
    def __init__(self, token: str):
        self.token = token

    @staticmethod
    def _generate_verification_code() -> str:
        return os.urandom(12).hex()

    def get_verification_code(self):
        return self._generate_verification_code()

    def get_url(self, method: str) -> str:
        return f"https://api.telegram.org/bot{self.token}/{method}"

    def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdatesResponse:
        url = self.get_url('getUpdates')
        response = requests.get(url, params={'offset': offset, 'timeout': timeout})
        return GetUpdatesResponse(**response.json())

    def send_message(self, chat_id: int, text: str) -> SendMessageResponse:
        url = self.get_url('sendMessage')
        response = requests.get(url, json={'chat_id': chat_id, 'text': text})
        return SendMessageResponse(**response.json())
