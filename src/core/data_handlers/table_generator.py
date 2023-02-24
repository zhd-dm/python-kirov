import asyncio
from typing import List, Dict


from utils.mapping import print_error
from core.connectors.db_connector import DBConnector

from core.data_handlers.data_importer import DataImporter

from features.google_sheets.config.types import T_SHEET_VALUES_RETURN


class TableGenerator:
    """
    Класс асинхронных вызовов обращения к DataImporter

    Аргументы:
    - `connector: DBConnector` - класс для подключения к БД
    - `bitrix_methods: List[str]` - метод(-ы) на который(-е) отправляется запрос
    """

    def __init__(self, connector: DBConnector):
        self.__connector = connector
        # self.__call_counter = 0

    async def _generate(self, field_to_py_type: Dict[str, str], entity_conf):
        
        data_importer = DataImporter(self.__connector, field_to_py_type, entity_conf)
        await data_importer._try_update_table()
        # self.__call_counter += 1

        await asyncio.sleep(1)
        
        # if self.__call_counter != db_table_name.__len__():
        #     print_error('Не все таблицы были корректно обновлены')