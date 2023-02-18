import asyncio
from typing import List, Union

from env import DATALENS_SERVER_CONNECTION
from connectors.db_connector import DBConnector
from google_sheets.google_sheet import GoogleSheet
from google_sheets.config.constants import RANGE_METHODS_NAMES
from data_generators.generate_entities import GenerateEntities
from utils.mapping import get_list_by_index_of_matrix


#
# REFACTOR:
# Глобальный рефакторинг:
# Продумать структуру генерации БД и схем
# Продумать разделение на роли
#

async def main():

    connector = DBConnector()
    bitrix_methods = get_list_by_index_of_matrix(0, GoogleSheet()._get_range_values(RANGE_METHODS_NAMES))
    await GenerateEntities(connector, bitrix_methods)._generate_entities()
    connector.engine.pool.dispose()

if __name__ == '__main__':
    asyncio.run(main())
