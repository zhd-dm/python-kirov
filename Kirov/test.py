import asyncio
from typing import Dict, List, Union

from fast_bitrix24 import BitrixAsync

# Local imports
from env import webhook
from fields.base_entity_config import BaseConfig
from fields.crm_deal_list_fields import CRM_DEAL_LIST_CONFIG
from fields.catalog_storeproduct_list_fields import CATALOG_STOREPRODUCT_LIST_CONFIG


from utils import Utils, print_error, key_dict_to_lower
from tables import BaseTable, BaseColumns


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
        pass
        config = BaseConfig(CRM_DEAL_LIST_CONFIG)
        table = BaseTable(engine, config)
        table._drop_and_create()
        
        data: List[Dict[str, any]] = await get_data(config)
        table._add_data(data)


    except Exception as error:
        print_error(error)

    finally:
        engine.pool.dispose()

asyncio.run(main())