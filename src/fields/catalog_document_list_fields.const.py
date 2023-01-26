from typing import Dict

from fields.base_fields import ENTITY_BASE_KEYS

T_CATALOG_DOCUMENT_LIST_FIELDS_KEYS = ['id']
T_CATALOG_DOCUMENT_LIST_FIELDS_VALUES = ['int']

KEY_AND_VALUE = { T_CATALOG_DOCUMENT_LIST_FIELDS_KEYS[i]: T_CATALOG_DOCUMENT_LIST_FIELDS_VALUES[i] for i in range(len(T_CATALOG_DOCUMENT_LIST_FIELDS_KEYS)) }

CATALOG_DOCUMENT_LIST_CONFIG: Dict[str, any] = {
    'entity_config': {
        'parent_name': 'catalog',
        'entity_name': 'document',
        'type_method': 'list',
        'params': {
            'select': ['*', 'UF_*']
        },
        'keys': [item for sublist in (ENTITY_BASE_KEYS, T_CATALOG_DOCUMENT_LIST_FIELDS_KEYS) for item in sublist]
    },
}
CATALOG_DOCUMENT_LIST_CONFIG.update(KEY_AND_VALUE)