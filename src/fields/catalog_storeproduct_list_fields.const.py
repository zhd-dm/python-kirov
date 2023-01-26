from typing import Dict

from fields.base_fields import ENTITY_BASE_KEYS

T_CATALOG_STOREPRODUCT_LIST_FIELDS_KEYS = ['amount', 'productId', 'quantityReserved', 'storeId']
T_CATALOG_STOREPRODUCT_LIST_FIELDS_VALUES = ['double', 'int', 'double', 'int']

KEY_AND_VALUE = { T_CATALOG_STOREPRODUCT_LIST_FIELDS_KEYS[i]: T_CATALOG_STOREPRODUCT_LIST_FIELDS_VALUES[i] for i in range(len(T_CATALOG_STOREPRODUCT_LIST_FIELDS_KEYS)) }

CATALOG_STOREPRODUCT_LIST_CONFIG: Dict[str, any] = {
    'entity_config': {
        'parent_name': 'catalog',
        'entity_name': 'storeproduct',
        'type_method': 'list',
        'params': {
            'select': ['*', 'UF_*']
        },
        'keys': [item for sublist in (ENTITY_BASE_KEYS, T_CATALOG_STOREPRODUCT_LIST_FIELDS_KEYS) for item in sublist]
    },
}
CATALOG_STOREPRODUCT_LIST_CONFIG.update(KEY_AND_VALUE)