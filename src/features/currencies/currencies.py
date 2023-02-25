import datetime
from typing import Dict, List


from features.currencies.currencies_api import CurrenciesApi
from features.currencies.currencies_connector import CurrenciesConnector


class Currencies:

    # @property
    # def current_currency(self):
    #     return self.__current_currency

    @property
    def date(self) -> str:
        return self.__currency.get('@Date')
    
    @property
    def currencies(self) -> Dict[str, any]:
        return self.__currencies

    def __init__(self, requested_date: datetime = None):
        self.__currency: Dict[str, any] = None
        self.__currencies: List[Dict[str, any]] = None
        self.__connector = CurrenciesConnector()

        if requested_date is not None:
            self.__currency = CurrenciesApi()._get_currencies(f'{self.__connector.api_url}?date_req={requested_date}')
        else:
            self.__currency = CurrenciesApi()._get_currencies(self.__connector.api_url)

        self.__prepare_response()

    def __prepare_response(self):
        self.__currency = self.__currency.get('ValCurs')
        self.__currencies = self.__currency.get('Valute')

        for currency in self.__currencies:
            currency['date'] = self.date