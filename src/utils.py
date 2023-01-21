import psycopg2
from fast_bitrix24 import BitrixAsync
from config import webhook
from fields import crm_deal_list

bx = BitrixAsync(webhook)

def connect_db(host: str, db: str, username: str, password: str):
    return psycopg2.connect(
            host = host,
            dbname = db,
            user = username,
            password = password
        )

async def get_data(entity_config: dict[str, str]) -> list | dict:
    method = '{0}.{1}.{2}'.format(entity_config['parent_name'], entity_config['entity_name'], entity_config['type_method'])
    print(method)

    return await bx.get_all(
        method,
        params = {
            'select': ['*', 'UF_*']
        }
    )

def get_entities() -> list[dict[str, str]]:
    return [
        crm_deal_list,
        # crm_invoice_list,
        # crm_product_list,
        # crm_company_list,
        # crm_contact_list,
        # catalog_document_list,
        # catalog_document_element_list
    ]

def get_list_columns(entity, columns: list[str]) -> list:
    list = []
    for key in columns:
        if key == entity[key]:
            list.append(entity[key])
    
    return list

def create_table_query(table_name: str) -> str:
    return """
        CREATE TABLE {}
        (ID integer, TITLE varchar)
    """.format(table_name)

def get_clear_table_query(table_name: str) -> str:
    return 'TRUNCATE TABLE {}'.format(table_name)

def insert_data_query(table_name: str, id: str, title: str, type_id: str, stage_id: str, probability: str, currency_id: str, opportunity: str, is_manual_opportunity: str) -> str:
    return """
        INSERT INTO {0} ({1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    """.format(table_name, id, title, type_id, stage_id, probability, currency_id, opportunity, is_manual_opportunity)