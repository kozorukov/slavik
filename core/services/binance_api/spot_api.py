import requests
from ast import literal_eval

from core.interfaces.binance_api.spot_api import ISpotClient
from core.services.binance_api.exceptions.token_not_found_exception import TokenNotFoundException


class SpotClient(ISpotClient):
    def __init__(self):
        self.url = 'https://api.binance.com/api/v3/'

    def get_token_price(self, token: str):
        response = requests.get(self.url + 'ticker/price')
        list_all_tokens = literal_eval(response.text)
        try:
            return next(x for x in list_all_tokens if x['symbol'] == f'{token.upper()}USDT')
        except StopIteration:
            raise TokenNotFoundException
