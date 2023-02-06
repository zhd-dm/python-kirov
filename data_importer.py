from typing import Dict, List, Union

from fast_bitrix24 import BitrixAsync
from sqlalchemy.engine import Engine


from env import webhook
from fields.base_config import BaseConfig
from fields.entity_config_with_fields import EntityConfigWithFields
from google_sheets.google_sheet import GoogleSheet
from google_sheets.constants import RANGE_BITRIX_FIELDS_TO_DB_TYPES, SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX
from tables.base_table import BaseTable
from utils import get_dict_by_indexes_of_matrix, replace_custom_value


class DataImporter:
    """
    Связующий класс, выполняющий основную логику, связанную с получением конфига из Google Sheets,
    генерацией по нему колонок и таблиц, получением данных из битрикса и записью в них данными

    Параметры:
    - `engine: Engine` - Engine
    - `bitrix_method: str` - метод, на который отправляется запрос в битрикс
    
    Геттеры:
    - `config -> BaseConfig` - конфиг сущности
    - `fields_from_sheets -> Dict[str, Any]` - словарь запрашиваемых полей из Google Sheets
    - `deal_ids -> List` - список айдишников сделок (нужны для вызова crm.productrow.list)

    Сеттеры:
    - `deal_ids` - предназначен для записи айдишников сделок
    """

    @property
    def config(self):
        return self.__config

    @property
    def fields_from_sheets(self):
        return self.__fields_from_sheets

    @property
    def deal_ids(self):
        return self.__deal_ids

    @deal_ids.setter
    def deal_ids(self, v: List):
        self.__deal_ids = v

    def __init__(self, engine: Engine, bitrix_method: str, deal_ids: List):
        self.__engine = engine
        self.__fields_from_sheets = self.__get_fields_from_sheet()

        self.__ecwf = EntityConfigWithFields(entity_key = bitrix_method, bitrix_fields_to_db_types = self.fields_from_sheets)
        self.__config = BaseConfig(self.__ecwf.entity_config_with_fields)

        self.__deal_ids: List = []

    async def _get_generate_and_set_entity(self):
        
        #
        # REFACTOR: сделать проверку на то, существует ли метод в списке кастомных методов
        # 
        replace_custom_value(self.config.params, 'custom', self.deal_ids)

        data: List[Dict[str, any]] = await self.__get_data(self.config)

        if self.config.entity_name == 'deal':
            self.deal_ids = [deal['ID'] for deal in data]

        table = BaseTable(self.__engine, self.config)
        table._drop_and_create()
        table._add_data(data)

    def __get_fields_from_sheet(self):
        return get_dict_by_indexes_of_matrix(
            SHEET_BITRIX_FIELD_INDEX,
            SHEET_PYTHON_TYPE_INDEX,
            GoogleSheet()._get_range_values(RANGE_BITRIX_FIELDS_TO_DB_TYPES)
        )

    async def __get_data(self, config: BaseConfig) -> Union[List, Dict]:
        bx = BitrixAsync(webhook)
        method = f'{config.parent_name}.{config.entity_name}.{config.type_method}' if config.parent_name else f'{config.entity_name}.{config.type_method}'
        print(f'Method name -> {method}')

        return await bx.get_all(
            method,
            params = config.params
        )