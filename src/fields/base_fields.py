#
# ================== Список основных параметров конфига сущности ==================
#

ENTITY_BASE_KEYS = ['parent_name', 'entity_name', 'type_method', 'params']

#
# ================== Словарь полей и их тип данных в БД ==================
#

BASE_FIELDS_TO_DB_TYPES = {

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
    # 'PROPERTY_119': 'json' {'valueId': '123', 'value': 'aaa'}
    'PROPERTY_119': 'int',
    'PROPERTY_119_VALUE': 'char'
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
# KEY_AND_VALUE = { T_CRM_DEAL_LIST_FIELDS_KEYS[i]: T_CRM_DEAL_LIST_FIELDS_VALUES[i] for i in range(len(T_CRM_DEAL_LIST_FIELDS_KEYS)) }
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
# }
# CRM_DEAL_LIST_CONFIG.update(KEY_AND_VALUE)