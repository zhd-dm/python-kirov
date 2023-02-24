import asyncio
import time
from typing import List, Union

from env import PROD_CONNECTION, TEST_CONNECTION
from core.connectors.db_connector import DBConnector
from features.google_sheets.google_sheet import GoogleSheet
from features.google_sheets.config.constants import RANGE_METHODS_NAMES, SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX, RANGE_BITRIX_FIELDS_TO_DB_TYPES, RANGE_ENTITIES_CONFIG
from core.data_handlers.table_generator import TableGenerator
from core.entity_configs.gs_entity_config_wrapper import GSEntityConfigWrapper
from core.entity_configs.entity_config import EntityConfig2
from utils.mapping import get_list_by_index_of_matrix, print_now_date, get_dict_by_indexes_of_matrix
from config.constants import HOUR


#
# REFACTOR:
# Глобальный рефакторинг:
# Продумать структуру генерации БД и схем
# Продумать разделение на роли
#

async def begin():
    print_now_date('Текущее время сервера')

    connector = DBConnector()
    gsheet = GoogleSheet()
    table_gen = TableGenerator(connector)

    field_to_py_type = get_dict_by_indexes_of_matrix(SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX, gsheet._get_range_values(RANGE_BITRIX_FIELDS_TO_DB_TYPES))
    # bx_methods = get_list_by_index_of_matrix(0, gsheet._get_range_values(RANGE_METHODS_NAMES))
    bx_entity_configs = gsheet._get_range_values(RANGE_ENTITIES_CONFIG)

    for bx_entity_conf in bx_entity_configs:
        gs_en_conf = GSEntityConfigWrapper(field_to_py_type, bx_entity_conf)
        en_conf = EntityConfig2(gs_en_conf.entity_config_with_fields)
        pass
        await table_gen._generate(field_to_py_type, bx_entity_conf)

    connector.engine.pool.dispose()

async def main():
    while True:
        await begin()
        time.sleep(HOUR)

if __name__ == '__main__':
    asyncio.run(main())
