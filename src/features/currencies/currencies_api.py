import requests
import xmltodict
from datetime import datetime
from typing import List, Dict


from features.currencies.currencies_connector import CurrenciesConnector


class CurrenciesApi:

    @property
    def date(self) -> str:
        return self.__currency.get('@Date')

    def __init__(self):
        self.__curr_conn = CurrenciesConnector()
        self.__currency = None
        self.__currencies = None

    def _get_currencies(self, requested_date: datetime = None):
        data = None
        self.__requested_date = requested_date

        if self.__requested_date is not None:
            data = requests.get(f'{self.__curr_conn.api_url}?date_req={self.__requested_date}')
        else:
            data = requests.get(self.__curr_conn.api_url)

        self.__prepare_response(xmltodict.parse(data.content))

        return self.__currencies

    def __prepare_response(self, response: Dict[str, Dict[str, any]]):
        self.__currency = response.get('ValCurs')
        self.__currencies = self.__currency.get('Valute')
        self.__set_date_to_curr()

    def __set_date_to_curr(self):
        for curr in self.__currencies:
            curr['date'] = self.__requested_date if self.__requested_date is not None else self.date