import asyncio
from typing import List


from utils.mapping import print_error, print_info
from connectors.db_connector import DBConnector

from data_generators.data_importer import DataImporter


class GenerateEntities:
    """
    Класс асинхронных вызовов обращения к DataImporter

    Аргументы:
    - `connector: DBConnector` - класс для подключения к БД
    - `bitrix_methods: List[str]` - метод(-ы) на который(-е) отправляется запрос
    """

    def __init__(self, connector: DBConnector, bitrix_methods: List[str]):
        self.__connector = connector
        self.__bitrix_methods = bitrix_methods
        self.__call_counter = 0

    async def _generate_entities(self):
        for bitrix_method in self.__bitrix_methods:
            data_importer = DataImporter(self.__connector, bitrix_method)
            await data_importer._try_update_table()
            self.__call_counter += 1

            await asyncio.sleep(1)
        
        if self.__call_counter != self.__bitrix_methods.__len__():
            print_error('Не все таблицы были корректно обновлены')
        else:
            print_info('Все таблицы успешно обновлены')