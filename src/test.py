import asyncio
from types import FunctionType
from typing import Dict
import sqlalchemy
from sqlalchemy_utils import database_exists
from sqlalchemy.orm import sessionmaker, close_all_sessions

# Local imports
from tables_const import TABLES
from utils import old_get_data, get_entity_config, get_engine, get_db_url, is_exist_db
from old_fields import crm_deal_list, crm_productrow_list

from fields._exports import LIST_OF_ENTITIES_CONFIG
from fields.base_fields import ENTITY_BASE_KEYS, DEFAULT_FIELDS
from fields.base_entity_config import BaseConfig

async def test():
    conf = BaseConfig(LIST_OF_ENTITIES_CONFIG[0])
    print(conf.keys)
    print()


asyncio.run(test())

try:
    # my_dict = {keys[i]: values[i] for i in range(len(keys))}
    # print(my_dict)
    print()
    

except Exception as error:
    print(error)

finally:
    # session.commit()
    # session.close()
    close_all_sessions()