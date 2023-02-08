import asyncio
from typing import Union, List


from utils import Settings
from data_importer import DataImporter

class GenerateEntities:
    """
    Класс асинхронных вызовов обращения к DataImporter

    Аргументы:
    - `settings: Settings` - класс для подключения к БД
    - `bitrix_methods: List[str]` - метод(-ы) на который(-е) отправляется запрос
    """

    def __init__(self, bitrix_methods: List[str]):
        self.__settings = Settings()
        self.__bitrix_methods = bitrix_methods

        self.__call_counter = 0

        asyncio.run(self.__generate_entities())

    async def __generate_entities(self):
        for bitrix_method in self.__bitrix_methods:
            data_importer = DataImporter(self.__settings, bitrix_method)
            await data_importer._get_generate_and_set_entity()
            self.__call_counter += 1

            if self.__call_counter == self.__bitrix_methods.__len__():
                self.__settings._engine_dispose()

            await asyncio.sleep(1)

    