from typing import Dict

from fields.base_fields import ENTITY_BASE_KEYS, BASE_FIELDS_TO_DB_TYPES

T_CRM_PRODUCTROW_LIST_FIELDS_KEYS = ['ID', 'OWNER_ID', 'PRODUCT_ID', 'PRODUCT_NAME', 'QUANTITY']
T_CRM_PRODUCTROW_LIST_FIELDS_VALUES = [BASE_FIELDS_TO_DB_TYPES[i] for i in filter(lambda x: x in BASE_FIELDS_TO_DB_TYPES, T_CRM_PRODUCTROW_LIST_FIELDS_KEYS)]

DICT_FIELD_AND_DB_TYPE = { T_CRM_PRODUCTROW_LIST_FIELDS_KEYS[i]: T_CRM_PRODUCTROW_LIST_FIELDS_VALUES[i] for i in range(len(T_CRM_PRODUCTROW_LIST_FIELDS_KEYS)) }
# [deal['ID'] for deal in deals]

CRM_PRODUCTROW_LIST_CONFIG: Dict[str, any] = {
    'entity_config': {
        'parent_name': 'crm',
        'entity_name': 'productrow',
        'type_method': 'list',
        'params': {
            'filter': {'OWNER_TYPE': 'D', 'OWNER_ID': 'custom'}
        },
        'keys': [item for sublist in (ENTITY_BASE_KEYS, T_CRM_PRODUCTROW_LIST_FIELDS_KEYS) for item in sublist]
    },
}
CRM_PRODUCTROW_LIST_CONFIG.update(DICT_FIELD_AND_DB_TYPE)
