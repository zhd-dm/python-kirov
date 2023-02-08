from typing import List, Union

from generate_entities import GenerateEntities

from fields.constants import BITRIX_METHODS


#
# REFACTOR:
# Глобальный рефакторинг:
# Продумать структуру генерации БД и схем
# Продумать разделение на роли
#

def main():

    GenerateEntities(['crm.deal.list', 'catalog.catalog.list'])

if __name__ == '__main__':
    main()
