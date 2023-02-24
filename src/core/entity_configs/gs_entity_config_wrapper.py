from typing import Dict, List


from features.google_sheets.google_sheet import GoogleSheet
from features.google_sheets.config.constants import RANGE_ENTITIES_CONFIG
from utils.mapping import find_list_of_matrix, convert_list_to_dict, convert_str_to_dict_or_list, print_error, key_and_value_dict_to_lower, props_list_to_lower

from core.data_handlers.config.types import T_ENTITY_CONFIG, T_FIELDS, T_ENTITY_CONFIG_WITH_FIELDS
from core.data_handlers.config.constants import ENTITY_CONFIG_KEYS


class GSEntityConfigWrapper:

    @property
    def entity_config_with_fields(self):
        return self.__entity_config_with_fields

    def __init__(self, field_to_py_type: Dict[str, any], entity_conf: List[str]):
        field_to_py_type = key_and_value_dict_to_lower(field_to_py_type)
        self.__entity_config = self.__get_entity(entity_conf)

        self.__entity_config_with_fields = self.__get_entity_config_with_fields(field_to_py_type)

    def __get_entity_config_with_fields(self, field_to_py_type: Dict[str, any]):
        entity_config_with_fields: T_ENTITY_CONFIG_WITH_FIELDS = {
            'entity_config': self.__entity_config,
            'field_to_py_type': self.__get_field_to_py_type(field_to_py_type)
        }

        return entity_config_with_fields

    def __get_entity(self, entity_conf: List[str]) -> T_ENTITY_CONFIG:   
        target_list = props_list_to_lower(entity_conf)
        target_dict = convert_list_to_dict(ENTITY_CONFIG_KEYS, target_list)

        entity_config = {}
        for k in target_dict:
            entity_config[k] = convert_str_to_dict_or_list(target_dict[k])

        return entity_config
    
    def __get_field_to_py_type(self, field_to_py_type: Dict[str, any]) -> T_FIELDS:
        list_of_fields = self.__entity_config.get('field_names')

        list_of_fields_to_py_type = [field_to_py_type[i] for i in filter(lambda x: x in field_to_py_type, list_of_fields)]

        if list_of_fields.__len__() != list_of_fields_to_py_type.__len__():
            print_error('Не указан py_type для некоторых полей')

        entity_fields = {
            list_of_fields[i]: list_of_fields_to_py_type[i] for i in range(len(list_of_fields))
        }

        return key_and_value_dict_to_lower(entity_fields)
