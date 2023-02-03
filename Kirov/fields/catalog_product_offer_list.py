from fields.base_fields_types import T_ENTITY_CONFIG_WITH_FIELDS
from fields.base_fields_constants import ENTITY_BASE_KEYS, BASE_FIELDS_TO_DB_TYPES


T_CATALOG_PRODUCT_OFFER_LIST_KEYS = ['parentId', 'id', 'name', 'purchasingPrice']
T_CATALOG_PRODUCT_OFFER_LIST_FIELDS_VALUES = [BASE_FIELDS_TO_DB_TYPES[i] for i in filter(lambda x: x in BASE_FIELDS_TO_DB_TYPES, T_CATALOG_PRODUCT_OFFER_LIST_KEYS)]

DICT_FIELD_AND_DB_TYPE = { T_CATALOG_PRODUCT_OFFER_LIST_KEYS[i]: T_CATALOG_PRODUCT_OFFER_LIST_FIELDS_VALUES[i] for i in range(len(T_CATALOG_PRODUCT_OFFER_LIST_KEYS)) }

CATALOG_PRODUCT_OFFER_LIST_CONFIG: T_ENTITY_CONFIG_WITH_FIELDS = {
    'entity_config': {
        'parent_name': 'catalog',
        'entity_name': 'product.offer',
        'type_method': 'list',
        'params': {
            'select': ['id', 'iblockId', '*', 'UF_*'],
            'filter': {'iblockId': 17}
        },
        'keys': [item for sublist in (ENTITY_BASE_KEYS, T_CATALOG_PRODUCT_OFFER_LIST_KEYS) for item in sublist],
        'enums': {},
        'primary_key': 'id'
    },
    'fields': DICT_FIELD_AND_DB_TYPE
}