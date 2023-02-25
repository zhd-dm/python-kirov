import asyncio
import time
from typing import List, Union, Dict

# Env
from env import PROD_CONNECTION, TEST_CONNECTION
from features.date_transformer.config.constants import SEC_IN_HOUR
from utils.mapping import get_dict_by_indexes_of_matrix
# Core
from core.connectors.db_connector import DBConnector
from core.data_handlers.table_generator import TableGenerator
from core.data_handlers.entity_data_importer import EntityDataImporter
from core.entity_configs.entity_config import EntityConfig
from core.entity_configs.entity_config_wrapper import EntityConfigWrapper
# GoogleSheets
from features.google_sheets.google_sheet import GoogleSheet
from features.google_sheets.config.constants import RANGE_ENTITIES_CONFIG, SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX, RANGE_BITRIX_FIELDS_TO_DB_TYPES
# Currencies
from features.currencies.config.constants import FIELD_TO_PY_TYPE
# DateTransformer
from features.date_transformer.date_transformer import DateTransformer
# Print
from features.print.print import Print


#
# REFACTOR:
# Глобальный рефакторинг:
# Продумать структуру генерации БД и схем
# Продумать разделение на роли
#

async def begin():
    DateTransformer._print_now_date('Текущее время сервера')

    table_type = 'gs_table'

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
        await asyncio.sleep(1)

    if call_counter != bx_entity_configs.__len__():
        Print().print_error('Не все таблицы были корректно обновлены')
    else:
        Print().print_info('Все таблицы успешно обновлены')

async def generate_currencies_table(connector: DBConnector, gsheet: GoogleSheet):
    table_gen = TableGenerator(connector, is_static = True, is_first = True)
    field_to_py_type = FIELD_TO_PY_TYPE
    curr_entity_conf = gsheet._get_range_values('G19:K19')[0]
    list_of_half_year_ago = DateTransformer()._get_list_of_half_year_ago()

    for day in list_of_half_year_ago:
        en_conf_with_fields = EntityConfigWrapper(field_to_py_type, curr_entity_conf).entity_config_with_fields
        en_conf = EntityConfig(en_conf_with_fields)
        data_importer = EntityDataImporter(connector, en_conf)
        data = data_importer._get_currencies_data(day)
        await table_gen._generate(en_conf, data)
        await asyncio.sleep(0.3)

    Print().print_info('Таблица currency обновлена')

async def main():
    # while True:
    #     await begin()
    #     time.sleep(SEC_IN_HOUR)
    await begin()

if __name__ == '__main__':
    asyncio.run(main())
