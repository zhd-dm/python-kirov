from typing import Dict

from fields.base_fields import ENTITY_BASE_KEYS, BASE_FIELDS_TO_DB_TYPES

T_CRM_PRODUCT_LIST_FIELDS_KEYS = ['ID', 'NAME', 'PROPERTY_119', 'PROPERTY_119_VALUE']
T_CRM_PRODUCT_LIST_FIELDS_VALUES = [BASE_FIELDS_TO_DB_TYPES[i] for i in filter(lambda x: x in BASE_FIELDS_TO_DB_TYPES, T_CRM_PRODUCT_LIST_FIELDS_KEYS)]

KEY_AND_VALUE = { T_CRM_PRODUCT_LIST_FIELDS_KEYS[i]: T_CRM_PRODUCT_LIST_FIELDS_VALUES[i] for i in range(len(T_CRM_PRODUCT_LIST_FIELDS_KEYS)) }

CRM_PRODUCT_LIST_CONFIG: Dict[str, any] = {
    'entity_config': {
        'parent_name': 'crm',
        'entity_name': 'product',
        'type_method': 'list',
        'params': {
            'select': ['*', 'UF_*']
        },
        'keys': [item for sublist in (ENTITY_BASE_KEYS, T_CRM_PRODUCT_LIST_FIELDS_KEYS) for item in sublist]
    },
}
CRM_PRODUCT_LIST_CONFIG.update(KEY_AND_VALUE)