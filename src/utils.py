from fast_bitrix24 import BitrixAsync
from sqlalchemy import create_engine

# Local imports
from config import webhook
from fields import catalog_document_element_list, catalog_document_list, catalog_storeProduct_getFields, catalog_store_getFields, crm_catalog_fields, crm_productrow_fields, crm_deal_list, crm_product_list

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
        params = {
            'select': ['*', 'UF_*']
        }
    )

def get_entities() -> list[dict[str, str | dict[str, str]]]:
    # Обязательный конфиг-массив для получения метода и списков полей
    return [
        catalog_document_element_list,
        # catalog_document_list,
        # catalog_storeProduct_getFields,
        # catalog_store_getFields,
        # crm_catalog_fields,
        # crm_productrow_fields,
        crm_deal_list,
        # crm_product_list
    ]
