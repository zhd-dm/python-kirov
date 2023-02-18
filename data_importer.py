from typing import Dict, List, Union

from fast_bitrix24 import BitrixAsync


from env import webhook
from fields.base_config import BaseConfig
from fields.entity_config_with_fields import EntityConfigWithFields
from fields.constants import ENTITIES_WITH_CUSTOM_PARAMS
from google_sheets.google_sheet import GoogleSheet
from google_sheets.constants import RANGE_BITRIX_FIELDS_TO_DB_TYPES, SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX
from tables.base_table import BaseTable
from utils import Settings, get_dict_by_indexes_of_matrix, print_error


class DataImporter:
    """
    Связующий класс, выполняющий основную логику, связанную с получением конфига из Google Sheets,
    генерацией по нему колонок и таблиц, получением данных из битрикса и записью в них данными

    Параметры:
    - `settings: Settings` - класс для подключения к БД
    - `bitrix_method: str` - метод, на который отправляется запрос в битрикс
    
    Геттеры:
    - `config -> BaseConfig` - конфиг сущности
    - `fields_from_sheets -> Dict[str, Any]` - словарь запрашиваемых полей из Google Sheets
    """

    @property
    def config(self):
        return self.__config

    @property
    def fields_from_sheets(self):
        return self.__fields_from_sheets

    def __init__(self, settings: Settings, bitrix_method: str):
        self.__settings = settings
        self.__connection = settings.connection

        self.__fields_from_sheets = self.__get_fields_from_sheet()

        self.__ecwf = EntityConfigWithFields(entity_key = bitrix_method, bitrix_fields_to_db_types = self.fields_from_sheets)
        self.__config = BaseConfig(self.__ecwf.entity_config_with_fields)

        if self.config.full_method in ENTITIES_WITH_CUSTOM_PARAMS():
            self.__replace_custom_params(ENTITIES_WITH_CUSTOM_PARAMS(self.__connection))

    async def _try_update_table(self):
        data: List[Dict[str, any]] = None

        try:
            data = await self.__get_bx_data(self.config)
        except Exception as error:
            print_error(error)
        
        if data is not None:
            self.__drop_and_insert_table(data)

    def __get_fields_from_sheet(self):
        return get_dict_by_indexes_of_matrix(
            SHEET_BITRIX_FIELD_INDEX,
            SHEET_PYTHON_TYPE_INDEX,
            GoogleSheet()._get_range_values(RANGE_BITRIX_FIELDS_TO_DB_TYPES)
        )

    async def __get_bx_data(self, config: BaseConfig) -> Union[List, Dict]:
        bx = BitrixAsync(webhook, False)
        method = f'{config.parent_name}.{config.entity_name}.{config.type_method}' if config.parent_name else f'{config.entity_name}.{config.type_method}'
        print(f'Method name -> {method}')

        return await bx.get_all(
            method,
            params = config.params
        )

    def __drop_and_insert_table(self, data):
        table = BaseTable(self.__settings, self.config)
        table._drop_and_create()
        table._add_data(data)

    def __replace_custom_params(self, entities_with_custom_params: Dict):
        self.config._replace_custom_params(entities_with_custom_params.get(self.config.full_method))