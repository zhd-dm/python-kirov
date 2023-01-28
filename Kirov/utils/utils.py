from typing import Union, List, Dict

from fast_bitrix24 import BitrixAsync
import sqlalchemy
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists

# Local imports
from env import webhook
from utils.settings import Settings
from fields.base_entity_config import BaseConfig


def get_db_url() -> str:
    url = Settings().db_url
    return url

def get_engine() -> Engine:
    engine = create_engine(get_db_url())
    return engine

async def get_data(config: BaseConfig) -> Union[List, Dict]:
    bx = BitrixAsync(webhook)
    method = '{0}.{1}.{2}'.format(config.parent_name, config.entity_name, config.type_method)
    print(f'Method name -> {method}')

    return await bx.get_all(
        method,
        params = config.params
    )

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
    print(f"""
        ------ SUCCESS----------------------------------------------------------- SUCCESS ------
                                {message}
        ----------------------------------------------------------------------------------------
        """
    )


def print_error(error: Exception):
    print(f"""
        ------ ERROR----------------------------------------------------------- ERROR ------
                                {error}
        ------------------------------------------------------------------------------------
        """
    )