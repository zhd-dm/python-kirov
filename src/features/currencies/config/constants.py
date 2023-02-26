API_URL = 'https://www.cbr.ru/scripts/XML_daily.asp'

CURR_ENTITY_CONF_LIST = ['currencies', '', '{}', '', '@id, numcode, charcode, nominal, name, value, date']

CURR_FIELD_TO_PY_TYPE = {
    '@id': 'char',
    'numcode': 'int',
    'charcode': 'char',
    'nominal': 'int',
    'name': 'char',
    'value': 'double',
    'date': 'date'
}

INCLUDES_CURRENCY_CODES = ['USD', 'EUR']