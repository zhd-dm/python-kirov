import asyncio
from typing import List, Union

from generate_entities import GenerateEntities
from utils import Settings

from fields.constants import BITRIX_METHODS


#
# REFACTOR:
# Глобальный рефакторинг:
# Продумать структуру генерации БД и схем
# Продумать разделение на роли
#

async def main():

    settings = Settings()
    await GenerateEntities(settings, BITRIX_METHODS)._generate_entities()
    settings.engine.pool.dispose()


if __name__ == '__main__':
    asyncio.run(main())
