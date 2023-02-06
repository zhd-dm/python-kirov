from fields.types import T_KEYS

#
# ================== Список ключей для маппинга списка из Google Sheets в T_ENTITY_CONFIG ==================
#

ENTITY_CONFIG_KEYS: T_KEYS = ['parent_name', 'entity_name', 'type_method', 'params', 'enums', 'primary_key', 'keys']

#
# REFACTOR:
# Подумать как получать из Google Sheets
#

BITRIX_METHODS = [
    'crm.deal.list',
    'catalog.catalog.list',
    'catalog.document.element.list',
    'catalog.document.list',
    'catalog.product.offer.list',
    'catalog.product.sku.list',
    'catalog.store.list',
    'catalog.storeproduct.list',
    'crm.product.list',
    'crm.productrow.list',
    'crm.company.list',
    'user.get'
]

#
# ================== Метод получения списка кастомных параметров запроса ==================
#

def ENTITIES_WITH_CUSTOM_PARAMS(conn = None):
    entities_with_custom_params = {
        'crm.productrow.list': []
    }

    if not conn:
        return entities_with_custom_params.keys()
    else:
        entities_with_custom_params['crm.productrow.list'] = [row[0] for row in conn.execute('SELECT id FROM deal').fetchall()]

    return entities_with_custom_params
