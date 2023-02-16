import asyncio
from typing import List, Union

from env import DATALENS_SERVER_SETTINGS
from google_sheets.google_sheet import GoogleSheet
from google_sheets.constants import RANGE_METHODS_NAMES
from generate_entities import GenerateEntities
from utils import Settings, get_list_by_index_of_matrix


#
# REFACTOR:
# Глобальный рефакторинг:
# Продумать структуру генерации БД и схем
# Продумать разделение на роли
#

async def main():

    settings = Settings()
    bitrix_methods = get_list_by_index_of_matrix(0, GoogleSheet()._get_range_values(RANGE_METHODS_NAMES))
    await GenerateEntities(settings, bitrix_methods)._generate_entities()
    settings.engine.pool.dispose()

    # settings = Settings(SERVER_SETTINGS)
    # connection = settings.connection
    # settings.engine.pool.dispose()

if __name__ == '__main__':
    asyncio.run(main())
