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

def main():

    settings = Settings()
    GenerateEntities(settings, ['crm.deal.list', 'catalog.catalog.list'])

if __name__ == '__main__':
    main()
