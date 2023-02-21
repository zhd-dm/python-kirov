from typing import Dict, List, Union


from core.connectors.db_connector import DBConnector
from core.api_calls.bx_api import BXApi
from google_sheets.google_sheet import GoogleSheet
from google_sheets.config.constants import RANGE_BITRIX_FIELDS_TO_DB_TYPES, SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX
from tables.base_table import BaseTable
from utils.mapping import get_dict_by_indexes_of_matrix, print_error
from entity_configs.entity_config import EntityConfig
from entity_configs.entity_config_with_fields import EntityConfigWithFields

from data_generators.config.constants import ENTITIES_WITH_CUSTOM_PARAMS


class DataImporter:
    """
    Связующий класс, выполняющий основную логику, связанную с получением конфига из Google Sheets,
    генерацией по нему колонок и таблиц, получением данных из битрикса и записью в них данными

    Параметры:
    - `connector: DBConnector` - класс для подключения к БД
    - `bitrix_method: str` - метод, на который отправляется запрос в битрикс
    
    Геттеры:
    - `config -> EntityConfig` - конфиг сущности
    - `fields_from_sheets -> Dict[str, Any]` - словарь запрашиваемых полей из Google Sheets
    """

    def __init__(self, connector: DBConnector, bitrix_method: str, field_to_py_type: Dict[str, str]):
        self.__connector = connector
        self.__connection = connector.connection

        self.__ecwf = EntityConfigWithFields(entity_key = bitrix_method, bitrix_fields_to_db_types = field_to_py_type)
        self.__config = EntityConfig(self.__ecwf.entity_config_with_fields)

        if self.__config.full_method in ENTITIES_WITH_CUSTOM_PARAMS():
            self.__replace_custom_params(ENTITIES_WITH_CUSTOM_PARAMS(self.__connection))

    async def _try_update_table(self):
        data: List[Dict[str, any]] = None

        try:
            data = await BXApi()._get_bx_data(self.__config)
        except Exception as error:
            print_error(error)
        
        if data is not None:
            self.__drop_and_insert_table(data)

    def __drop_and_insert_table(self, data):
        table = BaseTable(self.__connector, self.__config)
        table._drop_and_create()
        table._add_data(data)

    def __replace_custom_params(self, entities_with_custom_params: Dict):
        self.__config._replace_custom_params(entities_with_custom_params.get(self.__config.full_method))