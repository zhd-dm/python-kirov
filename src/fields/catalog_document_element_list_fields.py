from typing import Dict

from fields.base_fields import ENTITY_BASE_KEYS, BASE_FIELDS_TO_DB_TYPES

T_CATALOG_DOCUMENT_ELEMENT_LIST_FIELDS_KEYS = ['amount', 'elementId', 'storeTo']
T_CATALOG_DOCUMENT_ELEMENT_LIST_FIELDS_VALUES = [
    BASE_FIELDS_TO_DB_TYPES[i] for i in filter(lambda x: x in BASE_FIELDS_TO_DB_TYPES, T_CATALOG_DOCUMENT_ELEMENT_LIST_FIELDS_KEYS)
]

DICT_FIELD_AND_DB_TYPE = {
    T_CATALOG_DOCUMENT_ELEMENT_LIST_FIELDS_KEYS[i]: T_CATALOG_DOCUMENT_ELEMENT_LIST_FIELDS_VALUES[i] for i in range(len(T_CATALOG_DOCUMENT_ELEMENT_LIST_FIELDS_KEYS))
}

CATALOG_DOCUMENT_ELEMENT_LIST_CONFIG: Dict[str, any] = {
    'entity_config': {
        'parent_name': 'catalog',
        'entity_name': 'document.element',
        'type_method': 'list',
        'params': {
            'select': ['*', 'UF_*']
        },
        'keys': [item for sublist in (ENTITY_BASE_KEYS, T_CATALOG_DOCUMENT_ELEMENT_LIST_FIELDS_KEYS) for item in sublist]
    },
}
CATALOG_DOCUMENT_ELEMENT_LIST_CONFIG.update(DICT_FIELD_AND_DB_TYPE)