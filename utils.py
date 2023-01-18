import psycopg2
from fast_bitrix24 import BitrixAsync
from config import webhook

bx = BitrixAsync(webhook)

def connect_db(host: str, db: str, username: str, password: str):
    return psycopg2.connect(
            host = host,
            dbname = db,
            user = username,
            password = password
        )

async def get_data(parent_name: str, entity_name: str, type_method: str) -> list | dict:
    return await bx.get_all(
        '{}.{}.{}'.format(parent_name, entity_name, type_method),
        params = {
            'select': ['*', 'UF_*']
        }
    )

def get_columns(parent_name: str, entity_name: str) -> list:
    str = '{}.{}'.format(parent_name, entity_name)
    match str:
        case 'crm.deal':
            return ['ID', 'TITLE', 'TYPE_ID', 'STAGE_ID', 'PROBABILITY', 'CURRENCY_ID', 'OPPORTUNITY', 'IS_MANUAL_OPPORTUNITY']
        case 'crm.invoice':
            return []
        case 'crm.product':
            return []
        case 'crm.company':
            return []
        case 'crm.contact':
            return []
        case 'catalog.document':
            return []
        case 'catalog.document.element':
            return []
        case _:
            return []