from typing import Dict, List


from fields.base_fields_types import T_ENTITY_CONFIG_WITH_FIELDS, T_ENTITY_CONFIG, T_CALL_METHOD, T_PARAMS, T_KEYS, T_ENUMS, T_PRIMARY_KEY, T_FIELDS


#
# ================== Список основных параметров конфига сущности ==================
#

ENTITY_BASE_KEYS: List[str] = ['parent_name', 'entity_name', 'type_method', 'params']

#
# ================== Словарь полей и их тип данных в БД ==================
#

BASE_FIELDS_TO_DB_TYPES: Dict[str, str] = {

    # crm.deal.list
    'ID': 'int',
    'TITLE': 'text',
    'STAGE_ID': 'text',
    'CURRENCY_ID': 'text',
    'OPPORTUNITY': 'double',
    'CLOSEDATE': 'date',
    'CLOSED': 'char',
    'UF_CRM_1668857275565': 'enum',

    # catalog.document.element.list
    'amount': 'double',
    'elementId': 'int',
    'storeTo': 'int',

    # catalog.document.list
    'id': 'int',

    # catalog.storeproduct.list
    # 'amount': 'double',           # ==== дубль
    'productId': 'int',
    'quantityReserved': 'double',
    'storeId': 'int',

    # catalog.store.list
    # 'id': 'int',                  # ==== дубль
    'title': 'text',

    # catalog.catalog.list
    'NAME': 'text',

    # crm.productrow.list
    # 'ID': 'int',                  # ==== дубль
    'OWNER_ID': 'int',
    'PRODUCT_ID': 'int',
    'PRODUCT_NAME': 'text',
    'QUANTITY': 'double',

    # crm.product.list
    # 'ID': 'int',                  # ==== дубль
    # 'NAME': 'text',               # ==== дубль
    'PROPERTY_119': 'json' # {'valueId': '123', 'value': 'aaa'}
    # 'PROPERTY_119': 'int',
    # 'PROPERTY_119_VALUE': 'char'
}

#
# ================== Дефолтный список params ==================
#

DEFAULT_PARAMS: T_PARAMS = { 'select': ['*', 'UF_*'] }

#
# ================== Дефолтный список keys ==================
#

DEFAULT_KEYS: T_KEYS = ['parent_name', 'entity_name', 'type_method', 'params', 'id', 'title']

#
# ================== Дефолтный словарь enums ==================
#

DEFAULT_ENUMS: T_ENUMS = {}

#
# ================== Дефолтный словарь fields ==================
#

DEFAULT_FIELDS: T_FIELDS = { 'id': 'int', 'title': 'text' }

#
# ================== Дефолтный список вызываемого метода entity_config ==================
#

DEFAULT_CALL_METHOD: T_CALL_METHOD = ['catalog', 'store', 'list']

#
# ================== Дефолтное поле PK ==================
#

DEFAULT_PRIMARY_KEY: T_PRIMARY_KEY = ''

#
# ================== Дефолтный словарь entity_config ==================
#

DEFAULT_ENTITY_CONFIG: T_ENTITY_CONFIG = {
    'parent_name': DEFAULT_CALL_METHOD[0],
    'entity_name': DEFAULT_CALL_METHOD[1],
    'type_method': DEFAULT_CALL_METHOD[2],
    'params': DEFAULT_PARAMS,
    'keys': DEFAULT_KEYS,
    'primary_key_field': DEFAULT_PRIMARY_KEY
}

#
# ================== Дефолтный словарь entity_config_with_fields ==================
#

DEFAULT_ENTITY_CONFIG_WITH_FIELDS: T_ENTITY_CONFIG_WITH_FIELDS = { 
    'entity_config': DEFAULT_ENTITY_CONFIG,
    'fields': DEFAULT_FIELDS
}

#
# ================== Словарь полей, где entity_config - конфиг запрашиваемой сущности ==================
#
# entity_config {
#   parent_name - имя родительского метода
#   entity_name - имя сущности
#   type_method - тип метода сущности
#   params - params которые будут отправлены с запросом
# }
#
# остальные поля:
# ключ = имя поля
# значение = тип данных в БД
# 
# ================== Пример использования: ==================
# 
# CRM_DEAL_LIST_CONFIG['entity_config']['type_method'] ==> 'crm'
# CRM_DEAL_LIST_CONFIG['entity_config']['entity_name'] ==> 'deal'
# CRM_DEAL_LIST_CONFIG['entity_config']['type_method'] ==> 'list'
# CRM_DEAL_LIST_CONFIG['entity_config']['params'] ==> {'select': ['*', 'UF_*']}
# CRM_DEAL_LIST_CONFIG['entity_config']['keys'] ==> ['parent_name', 'entity_name', 'type_method', 'params', 'ID', 'TITLE', 'STAGE_ID', ...]
# CRM_DEAL_LIST_CONFIG['ID'] ==> int
# CRM_DEAL_LIST_CONFIG['id'] ==> KeyError: 'id'
# 
# ================== Создание конфига: ==================
#
# T_CRM_DEAL_LIST_FIELDS_KEYS = ['ID', 'TITLE', 'STAGE_ID', 'CURRENCY_ID', 'OPPORTUNITY', 'CLOSEDATE', 'CLOSED', 'UF_CRM_1668857275565']
# T_CRM_DEAL_LIST_FIELDS_VALUES = ['int', 'text', 'text', 'text', 'double', 'date', 'char', 'enum']
# DICT_FIELD_AND_DB_TYPE = { T_CRM_DEAL_LIST_FIELDS_KEYS[i]: T_CRM_DEAL_LIST_FIELDS_VALUES[i] for i in range(len(T_CRM_DEAL_LIST_FIELDS_KEYS)) }
# CRM_DEAL_LIST_CONFIG: Dict[str, any] = {
#     'entity_config': {
#         'parent_name': 'crm',
#         'entity_name': 'deal',
#         'type_method': 'list',
#         'params': {
#             'select': ['*', 'UF_*']
#         },
#         'keys': [item for sublist in (ENTITY_BASE_KEYS, T_CRM_DEAL_LIST_FIELDS_KEYS) for item in sublist]
#     },
#     'fields': DICT_FIELD_AND_DB_TYPE
# }