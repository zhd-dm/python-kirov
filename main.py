import asyncio
import time
from typing import List

from data_importer import DataImporter
from utils import Settings


#
# REFACTOR:
# Глобальный рефакторинг:
# Продумать структуру генерации БД и схем
# Продумать разделение на роли
#

def get_settings():
    return Settings()

async def generate_entity(settings: Settings, bitrix_method: str):
    if not settings:
        settings = get_settings()

    data_importer = DataImporter(settings, bitrix_method)
    await data_importer._get_generate_and_set_entity()
    settings.engine.pool.dispose()

async def generate_entities(bitrix_methods: List[str]):
    settings = get_settings()

    for bitrix_method in bitrix_methods:
        await generate_entity(settings, bitrix_method)
        time.sleep(1)

async def main():

    await generate_entity(None, 'crm.productrow.list')



if __name__ == '__main__':
    asyncio.run(main())
