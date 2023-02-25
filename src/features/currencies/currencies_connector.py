from features.currencies.config.constants import API_URL, FIELD_TO_PY_TYPE


class CurrenciesConnector:
    
    @property
    def api_url(self):
        return API_URL

    @property
    def field_to_py_type(self):
        return FIELD_TO_PY_TYPE