import asyncio
import time
from typing import Dict, List, Union

from fast_bitrix24 import BitrixAsync
from sqlalchemy import MetaData

# Local imports
from env import webhook
from fields.base_config import BaseConfig
from fields.catalog_catalog_list_fields import CATALOG_CATALOG_LIST_CONFIG
from fields.catalog_document_element_list_fields import CATALOG_DOCUMENT_ELEMENT_LIST_CONFIG
from fields.catalog_document_list_fields import CATALOG_DOCUMENT_LIST_CONFIG
from fields.catalog_store_list import CATALOG_STORE_LIST_CONFIG
from fields.catalog_storeproduct_list_fields import CATALOG_STOREPRODUCT_LIST_CONFIG
from fields.crm_deal_list_fields import CRM_DEAL_LIST_CONFIG
from fields.crm_product_list_fields import CRM_PRODUCT_LIST_CONFIG
from fields.crm_productrow_list_fields import CRM_PRODUCTROW_LIST_CONFIG
from fields.catalog_product_offer_list import CATALOG_PRODUCT_OFFER_LIST_CONFIG
from fields.catalog_product_sku_list import CATALOG_PRODUCT_SKU_LIST_CONFIG
from fields import LIST_OF_ENTITIES_CONFIG

from google_sheets.google_sheet import GoogleSheet
from google_sheets import RANGE_BASE_FIELDS_TO_DB_TYPES, SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX
from utils import Utils, print_error, key_dict_to_lower, get_dict_by_indexes_of_list_of_lists
from tables import BaseTable


utils = Utils()
engine = utils.engine

# Подумать куда вынести
async def get_data(config: BaseConfig) -> Union[List, Dict]:
    bx = BitrixAsync(webhook)
    method = f'{config.parent_name}.{config.entity_name}.{config.type_method}'
    print(f'Method name -> {method}')

    return await bx.get_all(
        method,
        params = config.params
    )
#


async def main():
    try:
        google_sheet = GoogleSheet()
        base_fields_to_db_types = get_dict_by_indexes_of_list_of_lists(
            SHEET_BITRIX_FIELD_INDEX,
            SHEET_PYTHON_TYPE_INDEX,
            google_sheet._get_range_values(RANGE_BASE_FIELDS_TO_DB_TYPES)
        )
        print(base_fields_to_db_types)




        # for entity_config in [CRM_DEAL_LIST_CONFIG]:
        #     config = BaseConfig(entity_config)
        #     data: List[Dict[str, any]] = await get_data(config)
        #     table = BaseTable(engine, config)
        #     table._drop_and_create()
        #     table._add_data(data)
        #     time.sleep(1)


    except Exception as error:
        print_error(error)

    finally:
        engine.pool.dispose()

asyncio.run(main())