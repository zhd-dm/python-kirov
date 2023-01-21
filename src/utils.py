import psycopg2
from fast_bitrix24 import BitrixAsync
from sqlalchemy import create_engine

# Local imports
from config import webhook
from fields import crm_deal_list

bx = BitrixAsync(webhook)

def connect_db(host: str, db: str, user: str, password: str):
    return psycopg2.connect(
            host = host,
            dbname = db,
            user = user,
            password = password
        )

def get_engine(user: str, password: str, host: str, port: int, db: str):
    url = f'postgresql://{user}:{password}@{host}:{port}/{db}'

    # if not db_exist(url):
    #     create_db(url)

    engine = create_engine(url)
    return engine

async def get_data(entity_config: dict[str, str]) -> list | dict:
    method = '{0}.{1}.{2}'.format(entity_config['parent_name'], entity_config['entity_name'], entity_config['type_method'])
    print('Method name -> {}'.format(method))

    return await bx.get_all(
        method,
        params = {
            'select': ['*', 'UF_*']
        }
    )

def get_entities() -> list[dict[str, str | dict[str, str]]]:
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
