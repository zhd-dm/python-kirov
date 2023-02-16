from fields.types import T_KEYS

#
# ================== Список ключей для маппинга списка из Google Sheets в T_ENTITY_CONFIG ==================
#

ENTITY_CONFIG_KEYS: T_KEYS = ['parent_name', 'entity_name', 'type_method', 'params', 'enums', 'primary_key', 'keys']

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
