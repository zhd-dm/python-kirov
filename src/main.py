import asyncio
import time
from typing import List, Union

from env import PROD_CONNECTION, TEST_CONNECTION
from core.connectors.db_connector import DBConnector
from google_sheets.google_sheet import GoogleSheet
from google_sheets.config.constants import RANGE_METHODS_NAMES, SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX, RANGE_BITRIX_FIELDS_TO_DB_TYPES
from data_generators.generate_entities import GenerateEntities
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
    
    field_to_py_type = get_dict_by_indexes_of_matrix(SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX, GoogleSheet()._get_range_values(RANGE_BITRIX_FIELDS_TO_DB_TYPES))
    bitrix_methods = get_list_by_index_of_matrix(0, GoogleSheet()._get_range_values(RANGE_METHODS_NAMES))

    await GenerateEntities(connector, bitrix_methods, field_to_py_type)._generate_entities()
    connector.engine.pool.dispose()

async def main():
    while True:
        await begin()
        time.sleep(HOUR)

if __name__ == '__main__':
    asyncio.run(main())
