import asyncio
import time
from typing import List, Union, Dict

from env import PROD_CONNECTION, TEST_CONNECTION
from core.connectors.db_connector import DBConnector
from features.google_sheets.google_sheet import GoogleSheet
from features.google_sheets.config.constants import RANGE_ENTITIES_CONFIG, SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX, RANGE_BITRIX_FIELDS_TO_DB_TYPES
from core.data_handlers.table_generator import TableGenerator
from features.google_sheets.gs_entity_config_wrapper import GSEntityConfigWrapper
from core.entity_configs.entity_config import EntityConfig
from utils.mapping import get_list_by_index_of_matrix, print_now_date, get_dict_by_indexes_of_matrix, print_info, print_error
from config.constants import HOUR


#
# REFACTOR:
# Глобальный рефакторинг:
# Продумать структуру генерации БД и схем
# Продумать разделение на роли
#

async def begin():
    print_now_date('Текущее время сервера')

    table_type = 'dynamic'

    connector = DBConnector()
    gsheet = GoogleSheet()
    table_gen = TableGenerator(connector)

    # В будущем тянуть из PG
    field_to_py_type = get_dict_by_indexes_of_matrix(SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX, gsheet._get_range_values(RANGE_BITRIX_FIELDS_TO_DB_TYPES))

    if table_type == 'dynamic':
        await generate_dynamic_table(gsheet, table_gen, field_to_py_type)

    connector.engine.pool.dispose()

async def generate_dynamic_table(gsheet: GoogleSheet, table_gen: TableGenerator, field_to_py_type: Dict[str, any]):
    bx_entity_configs = gsheet._get_range_values('G11:K11')

    call_counter = 0
    for bx_entity_conf in bx_entity_configs:
        gs_en_conf = GSEntityConfigWrapper(field_to_py_type, bx_entity_conf)
        en_conf = EntityConfig(gs_en_conf.entity_config_with_fields)
        await table_gen._generate(en_conf)
        call_counter += 1

    if call_counter != bx_entity_configs.__len__():
        print_error('Не все таблицы были корректно обновлены')
    else:
        print_info('Все таблицы успешно обновлены')

async def main():
    while True:
        await begin()
        time.sleep(HOUR)

if __name__ == '__main__':
    asyncio.run(main())
