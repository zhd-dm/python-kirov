import requests
import xmltodict


class CurrenciesApi:

    def _get_currencies(self, req_obj: str):
        data = requests.get(req_obj)
        return xmltodict.parse(data.content)