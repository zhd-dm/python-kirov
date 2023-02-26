from features.currencies.config.constants import API_URL, CURR_FIELD_TO_PY_TYPE, CURR_ENTITY_CONF_LIST, INCLUDES_CURRENCY_CODES


class CurrenciesConnector:
    
    @property
    def api_url(self):
        return API_URL

    @property
    def field_to_py_type(self):
        return CURR_FIELD_TO_PY_TYPE

    @property
    def entity_conf_list(self):
        return CURR_ENTITY_CONF_LIST

    @property
    def includes_corr_codes(self):
        return INCLUDES_CURRENCY_CODES