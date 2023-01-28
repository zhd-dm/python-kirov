from typing import Union, List, Dict

from fast_bitrix24 import BitrixAsync
import sqlalchemy
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists

# Local imports
from env import webhook, settings
from fields.base_entity_config import BaseConfig

from old_fields import crm_deal_list, catalog_document_element_list, catalog_document_list, catalog_storeproduct_list
from old_fields import catalog_store_list, catalog_catalog_list, crm_productrow_list, crm_product_list

def get_db_url() -> str:
    return 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(settings['user'], settings['password'], settings['host'], settings['port'], settings['db'])

def get_engine() -> Engine:
    engine = create_engine(get_db_url())
    return engine

# @deprecated
async def old_get_data(field_config: dict[str, str]) -> list | dict:
    bx = BitrixAsync(webhook)
    method = '{0}.{1}.{2}'.format(field_config['parent_name'], field_config['entity_name'], field_config['type_method'])
    print(f'Method name -> {method}')

    return await bx.get_all(
        method,
        params = field_config['params']
    )

async def get_data(config: BaseConfig) -> Union[List, Dict]:
    bx = BitrixAsync(webhook)
    method = '{0}.{1}.{2}'.format(config.parent_name, config.entity_name, config.type_method)
    print(f'Method name -> {method}')

    return await bx.get_all(
        method,
        params = config.params
    )

def prepare_db_table(entity: BaseConfig, data: List | Dict) -> bool:
    # Тут нужно проверить, можно ли эти данные занести в таблицу
    # Примерно так -> if insert_data(data) -> bool return True

    # truncate_table(table: Table, session: Session)
    return True

def insert_data_to_table(data: List | Dict) -> bool:
    try:
        query_insert_data(data)
        session.commit()
        return True
    except Exception as error:
        print_error(error)

def get_fields_config(deals: list) -> list[dict[str, str | dict[str, str]]]:
    # Обязательный конфиг-массив для получения метода и списков полей
    return [
        crm_deal_list,
        catalog_document_element_list,
        catalog_document_list,
        catalog_storeproduct_list,
        catalog_store_list,
        catalog_catalog_list,
        crm_productrow_list(deals),
        crm_product_list
    ]

# @deprecated
def get_entity_config(entity: dict) -> dict:
    return entity['entity_config']

# @deprecated
def get_entity_name(entity: dict) -> dict:
    return entity['entity_config']['entity_name']

def is_exist_db(db_url: str) -> bool:
    return database_exists(db_url)

def is_empty_table(session: Session, table) -> bool:
    return session.query(table).count() == 0

def is_exist_table(engine: Engine, tablename: str) -> bool:
    return sqlalchemy.inspect(engine).has_table(tablename)

def in_full_record_table(session: Session, table, number_of_records: int) -> bool:
    return session.query(table).count() == number_of_records

def records_in_table(session: Session, table) -> int:
    return session.query(table).count()

def print_success(message: str):
    print('===== SUCCESS =====')
    print(message)
    print('===== SUCCESS =====')

def print_error(error: Exception):
    print('===== ERROR =====')
    print(error)
    print('===== ERROR =====')