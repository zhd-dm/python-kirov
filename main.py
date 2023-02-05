import asyncio
import time
from typing import Dict, List, Union

from fast_bitrix24 import BitrixAsync


from env import webhook
from fields.base_config import BaseConfig
from fields.entity_config_with_fields import EntityConfigWithFields
from fields.constants import BITRIX_METHODS
from google_sheets.google_sheet import GoogleSheet
from google_sheets.constants import RANGE_BITRIX_FIELDS_TO_DB_TYPES, SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX
from tables.base_table import BaseTable
from utils import Utils, get_dict_by_indexes_of_matrix, replace_custom_value


#
# REFACTOR:
# Глобальный рефакторинг:
# Продумать структуру генерации БД и схем
# Продумать разделение на роли
#


utils = Utils()
engine = utils.engine

# Подумать куда вынести
async def get_data(config: BaseConfig) -> Union[List, Dict]:
    bx = BitrixAsync(webhook)
    method = f'{config.parent_name}.{config.entity_name}.{config.type_method}' if config.parent_name else f'{config.entity_name}.{config.type_method}'
    print(f'Method name -> {method}')

    return await bx.get_all(
        method,
        params = config.params
    )
#

async def main():

    fields_from_sheets = get_dict_by_indexes_of_matrix(
        SHEET_BITRIX_FIELD_INDEX,
        SHEET_PYTHON_TYPE_INDEX,
        GoogleSheet()._get_range_values(RANGE_BITRIX_FIELDS_TO_DB_TYPES)
    )

    deal_ids: List = []

    for bitrix_method in BITRIX_METHODS:
        ecwf = EntityConfigWithFields(entity_key = bitrix_method, bitrix_fields_to_db_types = fields_from_sheets)

        for entity_config in [ecwf.entity_config_with_fields]:
            config = BaseConfig(entity_config)
            
            #
            # REFACTOR: сделать проверку на то, существует ли метод в списке кастомных методов
            # 
            replace_custom_value(config.params, 'custom', deal_ids)

            data: List[Dict[str, any]] = await get_data(config)

            if config.entity_name == 'deal':
                deal_ids = [deal['ID'] for deal in data]
 
            table = BaseTable(engine, config)
            table._drop_and_create()
            table._add_data(data)
            time.sleep(1)

    engine.pool.dispose()

asyncio.run(main())