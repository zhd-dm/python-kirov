import asyncio
import time
from typing import List

from sqlalchemy.engine import Engine

from data_importer import DataImporter
from utils import Utils


#
# REFACTOR:
# Глобальный рефакторинг:
# Продумать структуру генерации БД и схем
# Продумать разделение на роли
#

def get_engine():
    utils = Utils()
    return utils.engine

async def generate_entity(engine: Engine, bitrix_method: str):
    if not engine:
        engine = get_engine()

    data_importer = DataImporter(engine, bitrix_method)
    await data_importer._get_generate_and_set_entity()
    engine.pool.dispose()

async def generate_entities(bitrix_methods: List[str]):
    engine = get_engine()

    for bitrix_method in bitrix_methods:
        await generate_entity(engine, bitrix_method)
        time.sleep(1)

async def main():

    await generate_entity(None, 'crm.deal.list')



if __name__ == '__main__':
    asyncio.run(main())
