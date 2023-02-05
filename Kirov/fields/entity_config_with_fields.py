from typing import Dict, List


from google_sheets.google_sheet import GoogleSheet
from google_sheets import RANGE_BASE_FIELDS_TO_DB_TYPES, SHEET_BITRIX_FIELD_INDEX, SHEET_PYTHON_TYPE_INDEX

from utils import find_list_of_matrix, convert_list_to_dict, convert_str_to_dict_or_list, get_dict_by_indexes_of_matrix, print_error

from fields.base_fields_types import T_ENTITY_CONFIG, T_FIELDS, T_ENTITY_CONFIG_WITH_FIELDS
from fields.base_fields_constants import ENTITY_CONFIG_KEYS, RANGE_ENTITIES_CONFIG


class EntityConfigWithFields:
    """
    Класс генерации entity_config_with_fields

    Параметры:
    - `entity_key` - ключ по которому будут доставаться поля из Google Sheets (прим. crm.deal.list)

    Геттеры:
    - `entity_config_with_fields` - словарь конфига сущности с полями и их типами
    - `entity_config` - словарь конфига сущности
    - `fields_config` - словарь конфига полей сущности с их типами данных
    - `bitrix_fields_to_db_types` - словарь полей битрикса, приведенных к python_types 
    """

    @property
    def entity_config_with_fields(self):
        return self.__entity_config_with_fields

    @property
    def entity_config(self):
        return self.__entity_config

    @property
    def fields_config(self):
        return self.__fields_config

    @property
    def bitrix_fields_to_db_types(self):
        return self.__bitrix_fields_to_db_types


    def __init__(self, entity_key):
        self.__entity_key = entity_key
        self.__google_sheet = GoogleSheet()
        self.__entities_config_lists = self.__google_sheet._get_range_values(RANGE_ENTITIES_CONFIG)

        self.__bitrix_fields_to_db_types = get_dict_by_indexes_of_matrix(
            SHEET_BITRIX_FIELD_INDEX,
            SHEET_PYTHON_TYPE_INDEX,
            self.__google_sheet._get_range_values(RANGE_BASE_FIELDS_TO_DB_TYPES)
        )
        self.__entity_config = self.__prepare_current_entity()
        self.__fields_config = self.__generate_current_fields()
        self.__entity_config_with_fields = self.__get_entity_config_with_fields()

    def __get_entity_config_with_fields(self):
        entity_config_with_fields: T_ENTITY_CONFIG_WITH_FIELDS = {
            'entity_config': self.entity_config,
            'fields': self.fields_config
        }

        return entity_config_with_fields

    def __generate_current_fields(self) -> T_FIELDS:
        """
        Метод генерации словаря T_FIELDS
        """

        list_of_bitrix_fields = self.entity_config.get('keys')
        list_of_entity_fields = [self.bitrix_fields_to_db_types[i] for i in filter(lambda x: x in self.bitrix_fields_to_db_types, list_of_bitrix_fields)]

        fields_config = {
            list_of_bitrix_fields[i]: list_of_entity_fields[i] for i in range(len(list_of_bitrix_fields))
        }

        return fields_config

    def __prepare_current_entity(self) -> T_ENTITY_CONFIG:
        """
        Метод маппинга конфига из таблицы в словарь T_ENTITY_CONFIG (без списка keys)

        - `from_index` в `find_list_of_list_of_lists()` должен быть равен нулю, потому что это первый столбец из таблицы
        - индекс извлечения названия метода тоже равен 0
        """
        
        try:
            target_list = find_list_of_matrix(0, self.__entity_key, self.__entities_config_lists)
            split_item: List[str] = target_list[0].split('.')
            target_list.pop(0)
            target_list.insert(0, split_item[2])
            target_list.insert(0, split_item[1])
            target_list.insert(0, split_item[0])
            target_dict = convert_list_to_dict(ENTITY_CONFIG_KEYS, target_list)

            entity_config = {}
            for k in target_dict:
                entity_config[k] = convert_str_to_dict_or_list(target_dict[k])

            # DEPRECATED
            # entity_config['keys'].extend(ENTITY_BASE_KEYS)

            return entity_config

        except Exception:
            print_error('Произошла ошибка при поиске конфига метода из Google Sheets')
