from typing import Dict, List


from fields.base_fields_types import T_ENTITY_CONFIG_WITH_FIELDS, T_ENTITY_CONFIG, T_CALL_METHOD, T_PARAMS, T_KEYS, T_ENUMS, T_PRIMARY_KEY, T_FIELDS

#
# ================== Диапазон Google Sheets ячеек конфигов сущностей ==================
#

RANGE_ENTITIES_CONFIG = 'G3:K'

#
# ================== Список ключей для маппинга списка из Google Sheets в T_ENTITY_CONFIG ==================
#

# DEPRECATED
ENTITY_CONFIG_KEYS = ['parent_name', 'entity_name', 'type_method', 'params', 'enums', 'primary_key', 'keys']

#
# ================== Список основных параметров конфига сущности ==================
#

# DEPRECATED
ENTITY_BASE_KEYS: T_KEYS = ['parent_name', 'entity_name', 'type_method', 'params']

#
# ================== Словарь полей и их тип данных в БД ==================
#

# DEPRECATED
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
    'PROPERTY_119': 'json', # {'valueId': '123', 'value': 'aaa'}
    # 'PROPERTY_119': 'int',
    # 'PROPERTY_119_VALUE': 'char'

    # catalog.product.offer.list
    'parentId': 'json',
    # 'id': 'int',                  # ==== дубль
    'name': 'char',
    'purchasingPrice': 'double',

    # catalog.product.sku.list
    # 'id': 'int',                  # ==== дубль
    'property119': 'json'
}

#
# ================== Дефолтный список params ==================
#

DEFAULT_PARAMS: T_PARAMS = { 'select': ['*', 'UF_*'] }

#
# ================== Дефолтный список keys ==================
#

# DEPRECATED
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
