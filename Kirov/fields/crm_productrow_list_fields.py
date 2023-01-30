from fields.base_fields_types import T_ENTITY_CONFIG_WITH_FIELDS
from fields.base_fields_constants import ENTITY_BASE_KEYS, BASE_FIELDS_TO_DB_TYPES


T_CRM_PRODUCTROW_LIST_FIELDS_KEYS = ['ID', 'OWNER_ID', 'PRODUCT_ID', 'PRODUCT_NAME', 'QUANTITY']
T_CRM_PRODUCTROW_LIST_FIELDS_VALUES = [BASE_FIELDS_TO_DB_TYPES[i] for i in filter(lambda x: x in BASE_FIELDS_TO_DB_TYPES, T_CRM_PRODUCTROW_LIST_FIELDS_KEYS)]

DICT_FIELD_AND_DB_TYPE = { T_CRM_PRODUCTROW_LIST_FIELDS_KEYS[i]: T_CRM_PRODUCTROW_LIST_FIELDS_VALUES[i] for i in range(len(T_CRM_PRODUCTROW_LIST_FIELDS_KEYS)) }

CRM_PRODUCTROW_LIST_CONFIG: T_ENTITY_CONFIG_WITH_FIELDS = {
    'entity_config': {
        'parent_name': 'crm',
        'entity_name': 'productrow',
        'type_method': 'list',
        'params': {
            'filter': {'OWNER_TYPE': 'D', 'OWNER_ID': 'custom'} # [deal['ID'] for deal in deals]
        },
        'keys': [item for sublist in (ENTITY_BASE_KEYS, T_CRM_PRODUCTROW_LIST_FIELDS_KEYS) for item in sublist]
    },
    'fields': DICT_FIELD_AND_DB_TYPE
}