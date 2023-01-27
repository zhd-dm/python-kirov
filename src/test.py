import asyncio
from types import FunctionType
from typing import Dict
import sqlalchemy
from sqlalchemy_utils import database_exists
from sqlalchemy.orm import sessionmaker, close_all_sessions

# Local imports
from tables_const import TABLES
from utils import get_data, get_entity_config, get_engine, get_db_url, is_exist_db
from old_fields import crm_deal_list, crm_productrow_list

from fields.base_fields import ENTITY_BASE_KEYS
from fields.base_entity_config_generator import EntityConfig
from fields.catalog_catalog_list_fields import CATALOG_CATALOG_LIST_CONFIG
from fields.catalog_document_element_list_fields import CATALOG_DOCUMENT_ELEMENT_LIST_CONFIG
from fields.catalog_document_list_fields import CATALOG_DOCUMENT_LIST_CONFIG
from fields.catalog_store_list import CATALOG_STORE_LIST_CONFIG
from fields.catalog_storeproduct_list_fields import CATALOG_STOREPRODUCT_LIST_CONFIG
from fields.crm_deal_list_fields import CRM_DEAL_LIST_CONFIG
from fields.crm_product_list_fields import CRM_PRODUCT_LIST_CONFIG

ENTITIES_CONFIG = [
    CATALOG_CATALOG_LIST_CONFIG,
    CATALOG_DOCUMENT_ELEMENT_LIST_CONFIG,
    CATALOG_DOCUMENT_LIST_CONFIG,
    CATALOG_STORE_LIST_CONFIG,
    CATALOG_STOREPRODUCT_LIST_CONFIG,
    CRM_DEAL_LIST_CONFIG,
    CRM_PRODUCT_LIST_CONFIG
]

async def test():

    print(EntityConfig(CRM_DEAL_LIST_CONFIG).get_fields())

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