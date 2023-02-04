from typing import Dict, List


from google_sheets.google_sheet import GoogleSheet

from utils import find_list_of_list_of_lists, convert_list_to_dict

from fields.base_fields_types import T_ENTITY_CONFIG, T_FIELDS, T_ENTITY_CONFIG_WITH_FIELDS
from fields.base_fields_constants import ENTITY_CONFIG_KEYS

from fields.base_fields_constants import RANGE_ENTITIES_CONFIG
from fields.base_fields_types import T_ENTITY_CONFIG_WITH_FIELDS
from fields.base_fields_constants import ENTITY_BASE_KEYS, BASE_FIELDS_TO_DB_TYPES


T_CATALOG_CATALOG_LIST_FIELDS_KEYS = ['NAME']
T_CATALOG_CATALOG_LIST_FIELDS_VALUES = [BASE_FIELDS_TO_DB_TYPES[i] for i in filter(lambda x: x in BASE_FIELDS_TO_DB_TYPES, T_CATALOG_CATALOG_LIST_FIELDS_KEYS)]

DICT_FIELD_AND_DB_TYPE = { T_CATALOG_CATALOG_LIST_FIELDS_KEYS[i]: T_CATALOG_CATALOG_LIST_FIELDS_VALUES[i] for i in range(len(T_CATALOG_CATALOG_LIST_FIELDS_KEYS)) }

CATALOG_CATALOG_LIST_CONFIG: T_ENTITY_CONFIG_WITH_FIELDS = {
    'entity_config': {
        'parent_name': 'catalog',
        'entity_name': 'catalog',
        'type_method': 'list',
        'params': {
            'select': ['*', 'UF_*']
        },
        'keys': [item for sublist in (ENTITY_BASE_KEYS, T_CATALOG_CATALOG_LIST_FIELDS_KEYS) for item in sublist],
        'enums': {},
        'primary_key': ''
    },
    'fields': DICT_FIELD_AND_DB_TYPE
}

class EntityConfigWithFields:
    """
    Класс генерации entity_config_with_fields

    Параметры:
    - `entity_key` - ключ по которому будут доставаться поля из Google Sheets (прим. crm.deal.list)

    Геттеры:
    - `entity_config_with_fields` - словарь конфига сущности с его полями и типами данных
    """
    @property
    def entity_config_with_fields(self):
        return self.__get_entity_config_with_fields()


    def __init__(self, entity_key: str = ''):
        self.__entity_key = entity_key
        #
        self.__entity_key = 'crm.deal.list'
        #
        self.__google_sheet = GoogleSheet()
        self.__entities_config_list = self.__google_sheet._get_range_values(RANGE_ENTITIES_CONFIG)
        #
        self.__get_entity_config_with_fields()
        #
        pass

    def __get_entity_config_with_fields(self):
        entity_config: T_ENTITY_CONFIG_WITH_FIELDS = {
            'entity_config': self.__get_current_entity_config(),
            'fields': self.__get_current_fields()
        }
        return entity_config

    def __get_current_entity_config(self) -> T_ENTITY_CONFIG:
        """
        Метод получения словаря T_ENTITY_CONFIG
        """

        config_without_keys = self.__prepare_current_entity_config()
        entity_config = config_without_keys
        entity_config['keys'] = ['test']
        
        return entity_config

    def __get_current_fields(self) -> T_FIELDS:
        """
        Метод генерации словаря fields по entity_key
        """

        fields = {

        }
        return fields

    def __prepare_current_entity_config(self) -> T_ENTITY_CONFIG:
        """
        Метод маппинга конфига из таблицы в словарь T_ENTITY_CONFIG (без списка keys)

        - `from_index` в `find_list_of_list_of_lists()` должен быть равен нулю, потому что это первый столбец из таблицы
        - индекс извлечения названия метода тоже равен 0
        """

        target_list = find_list_of_list_of_lists(0, self.__entity_key, self.__entities_config_list)
        split_item: List[str] = target_list[0].split('.')
        target_list.pop(0)
        target_list.insert(0, split_item[2])
        target_list.insert(0, split_item[1])
        target_list.insert(0, split_item[0])
        target_dict = convert_list_to_dict(ENTITY_CONFIG_KEYS, target_list)
        
        return target_dict