import asyncio
import time
from typing import List, Union, Dict

# Env
from env import PROD_CONNECTION, TEST_CONNECTION
from config.constants import HOUR
from utils.mapping import print_now_date, get_dict_by_indexes_of_matrix, print_info, print_error
# Core
from core.connectors.db_connector import DBConnector
from core.data_handlers.table_generator import TableGenerator
from core.data_handlers.entity_data_importer import EntityDataImporter
from core.entity_configs.entity_config import EntityConfig
from core.entity_configs.entity_config_wrapper import EntityConfigWrapper
# GoogleSheets
from features.google_sheets.google_sheet import GoogleSheet
from features.google_sheets.config.constants import RANGE_ENTITIES_CONFIG, SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX, RANGE_BITRIX_FIELDS_TO_DB_TYPES
from features.currencies.currencies import Currencies
# Currencies
from features.currencies.config.constants import FIELD_TO_PY_TYPE


#
# REFACTOR:
# Глобальный рефакторинг:
# Продумать структуру генерации БД и схем
# Продумать разделение на роли
#

async def begin():
    print_now_date('Текущее время сервера')

    table_type = 'currencies_table'

    connector = DBConnector()
    gsheet = GoogleSheet()

    match table_type:
        case 'gs_table':
            await generate_table_from_gs(connector, gsheet)
        case 'currencies_table':
            await generate_currencies_table(connector, gsheet)

    connector.engine.pool.dispose()

async def generate_table_from_gs(connector: DBConnector, gsheet: GoogleSheet):
    table_gen = TableGenerator(connector)
    field_to_py_type = get_dict_by_indexes_of_matrix(SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX, gsheet._get_range_values(RANGE_BITRIX_FIELDS_TO_DB_TYPES))
    bx_entity_configs = gsheet._get_range_values(RANGE_ENTITIES_CONFIG)

    call_counter = 0
    for bx_entity_conf in bx_entity_configs:
        en_conf_with_fields = EntityConfigWrapper(field_to_py_type, bx_entity_conf).entity_config_with_fields
        en_conf = EntityConfig(en_conf_with_fields)
        data_importer = EntityDataImporter(connector, en_conf)
        data = await data_importer._get_bx_data()
        await table_gen._generate(en_conf, data)
        call_counter += 1

    if call_counter != bx_entity_configs.__len__():
        print_error('Не все таблицы были корректно обновлены')
    else:
        print_info('Все таблицы успешно обновлены')

async def generate_currencies_table(connector: DBConnector, gsheet: GoogleSheet):
    table_gen = TableGenerator(connector)
    field_to_py_type = FIELD_TO_PY_TYPE
    curr_entity_conf = gsheet._get_range_values('G19:K19')[0]

    en_conf_with_fields = EntityConfigWrapper(field_to_py_type, curr_entity_conf).entity_config_with_fields
    en_conf = EntityConfig(en_conf_with_fields)
    data_importer = EntityDataImporter(connector, en_conf)
    data = data_importer._get_currencies_data()
    await table_gen._generate(en_conf, data)

async def main():
    while True:
        await begin()
        time.sleep(HOUR)

if __name__ == '__main__':
    asyncio.run(main())
