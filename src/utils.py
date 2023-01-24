from fast_bitrix24 import BitrixAsync
from sqlalchemy import create_engine

# Local imports
from config import webhook

from fields import crm_deal_list, catalog_document_element_list, catalog_document_list, catalog_storeproduct_list
from fields import catalog_store_list, catalog_catalog_list, crm_productrow_fields, crm_product_list

def get_engine(user: str, password: str, host: str, port: int, db: str):
    url = f'postgresql://{user}:{password}@{host}:{port}/{db}'

    # if not db_exist(url):
    #     create_db(url)

    engine = create_engine(url)
    return engine

async def get_data(field_config: dict[str, str]) -> list | dict:
    bx = BitrixAsync(webhook)
    method = '{0}.{1}.{2}'.format(field_config['parent_name'], field_config['entity_name'], field_config['type_method'])
    print(f'Method name -> {method}')

    return await bx.get_all(
        method,
        params = field_config['params']
    )

def get_fields_config(deals: list) -> list[dict[str, str | dict[str, str]]]:
    # Обязательный конфиг-массив для получения метода и списков полей
    return [
        crm_deal_list,
        catalog_document_element_list,
        catalog_document_list,
        catalog_storeproduct_list,
        catalog_store_list,
        catalog_catalog_list,
        crm_productrow_fields(deals),
        crm_product_list
    ]
    
def get_entity_config(entity: dict) -> dict:
    return entity['entity_config']

def get_entity_name(entity: dict) -> dict:
    return entity['entity_config']['entity_name']