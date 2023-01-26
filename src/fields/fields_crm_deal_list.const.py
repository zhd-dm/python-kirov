from typing import Dict

from fields.base_fields import ENTITY_BASE_KEYS

T_CRM_DEAL_LIST_FIELDS_KEYS = ['ID', 'TITLE', 'STAGE_ID', 'CURRENCY_ID', 'OPPORTUNITY', 'CLOSEDATE', 'CLOSED', 'UF_CRM_1668857275565']
T_CRM_DEAL_LIST_FIELDS_VALUES = ['int', 'text', 'text', 'text', 'double', 'date', 'char', 'enum']

KEY_AND_VALUE = { T_CRM_DEAL_LIST_FIELDS_KEYS[i]: T_CRM_DEAL_LIST_FIELDS_VALUES[i] for i in range(len(T_CRM_DEAL_LIST_FIELDS_KEYS)) }

CRM_DEAL_LIST_CONFIG: Dict[str, any] = {
    'entity_config': {
        'parent_name': 'crm',
        'entity_name': 'deal',
        'type_method': 'list',
        'params': {
            'select': ['*', 'UF_*']
        },
        'keys': [item for sublist in (ENTITY_BASE_KEYS, T_CRM_DEAL_LIST_FIELDS_KEYS) for item in sublist]
    },
}
CRM_DEAL_LIST_CONFIG.update(KEY_AND_VALUE)