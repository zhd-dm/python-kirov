from fields.base_fields_types import T_ENTITY_CONFIG_WITH_FIELDS
from fields.base_fields_constants import ENTITY_BASE_KEYS, BASE_FIELDS_TO_DB_TYPES


T_CRM_PRODUCT_LIST_FIELDS_KEYS = ['ID', 'NAME', 'PROPERTY_119']
T_CRM_PRODUCT_LIST_FIELDS_VALUES = [BASE_FIELDS_TO_DB_TYPES[i] for i in filter(lambda x: x in BASE_FIELDS_TO_DB_TYPES, T_CRM_PRODUCT_LIST_FIELDS_KEYS)]

DICT_FIELD_AND_DB_TYPE = { T_CRM_PRODUCT_LIST_FIELDS_KEYS[i]: T_CRM_PRODUCT_LIST_FIELDS_VALUES[i] for i in range(len(T_CRM_PRODUCT_LIST_FIELDS_KEYS)) }

CRM_PRODUCT_LIST_CONFIG: T_ENTITY_CONFIG_WITH_FIELDS = {
    'entity_config': {
        'parent_name': 'crm',
        'entity_name': 'product',
        'type_method': 'list',
        'params': {
            'select': ['*', 'NAME']
        },
        'keys': [item for sublist in (ENTITY_BASE_KEYS, T_CRM_PRODUCT_LIST_FIELDS_KEYS) for item in sublist],
        'enums': {},
        'primary_key': 'id'
    },
    'fields': DICT_FIELD_AND_DB_TYPE
}