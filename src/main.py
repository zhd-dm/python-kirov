import asyncio
import time
from typing import List, Union, Dict


from env import PROD_CONNECTION, TEST_CONNECTION
from config.constants import HOUR
from utils.mapping import print_now_date, get_dict_by_indexes_of_matrix, print_info, print_error
from core.connectors.db_connector import DBConnector
from core.data_handlers.table_generator import TableGenerator
from core.data_handlers.bx_data_importer import BXDataImporter
from core.entity_configs.entity_config import EntityConfig
from features.google_sheets.gs_entity_config_wrapper import GSEntityConfigWrapper
from features.google_sheets.google_sheet import GoogleSheet
from features.google_sheets.config.constants import RANGE_ENTITIES_CONFIG, SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX, RANGE_BITRIX_FIELDS_TO_DB_TYPES
from features.currencies.currencies import Currencies


#
# REFACTOR:
# Глобальный рефакторинг:
# Продумать структуру генерации БД и схем
# Продумать разделение на роли
#

async def begin():
    print_now_date('Текущее время сервера')

    table_type = 'gs_table'

    connector = DBConnector()
    gsheet = GoogleSheet()

    match table_type:
        case 'gs_table':
            await generate_table_from_gs(connector, gsheet)
        case 'currencies':
            generate_currencies_table(connector)

    connector.engine.pool.dispose()

async def generate_table_from_gs(connector: DBConnector, gsheet: GoogleSheet):
    # RANGE_ENTITIES_CONFIG
    table_gen = TableGenerator(connector)
    field_to_py_type = get_dict_by_indexes_of_matrix(SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX, gsheet._get_range_values(RANGE_BITRIX_FIELDS_TO_DB_TYPES))
    bx_entity_configs = gsheet._get_range_values('G12:K12')


    call_counter = 0
    for bx_entity_conf in bx_entity_configs:
        gs_en_conf = GSEntityConfigWrapper(field_to_py_type, bx_entity_conf)
        en_conf = EntityConfig(gs_en_conf.entity_config_with_fields)
        data_importer = BXDataImporter(connector, en_conf)
        data = await data_importer._get_data()
        await table_gen._generate(en_conf, data)
        call_counter += 1

    if call_counter != bx_entity_configs.__len__():
        print_error('Не все таблицы были корректно обновлены')
    else:
        print_info('Все таблицы успешно обновлены')

def generate_currencies_table(connector: DBConnector):
    table_gen = TableGenerator(connector)
    curr = Currencies()

async def main():
    while True:
        await begin()
        time.sleep(HOUR)
    pass

if __name__ == '__main__':
    asyncio.run(main())
