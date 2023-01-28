import asyncio
from typing import Dict, List
# from types import FunctionType
# from typing import Dict
# import sqlalchemy
# from sqlalchemy_utils import database_exists
# from sqlalchemy.orm import sessionmaker, close_all_sessions
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

# Local imports 
from env import Settings, DEFAULT_settings, AIVEN_settings
from utils import get_engine, get_data, print_error

from tables.base_table import BaseTable, Catalog
from fields._exports import LIST_OF_ENTITIES_CONFIG
from fields.base_fields import ENTITY_BASE_KEYS, DEFAULT_FIELDS
from fields.base_entity_config import BaseConfig
from fields.crm_deal_list_fields import CRM_DEAL_LIST_CONFIG

from generate_tables import DealTable

engine = get_engine()


async def main():
    try:
        entity = BaseConfig(CRM_DEAL_LIST_CONFIG)
        deals: List[Dict[str, any]] = await get_data(entity)
        deal_table = DealTable(engine)
        deal_table._drop_and_create()
        for deal in deals:
            deal_table._add_data(deal)

    except Exception as error:
        print_error(error)

asyncio.run(main())