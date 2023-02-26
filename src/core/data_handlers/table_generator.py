import asyncio
from typing import List, Dict


from utils.mapping import get_list_keys_from_dict_of_condition

from core.connectors.db_connector import DBConnector
from core.tables.base_table import BaseTable
from core.entity_configs.entity_config import EntityConfig
from features.print.print import Print


class TableGenerator:

    def __init__(self, connector: DBConnector, is_first = False, is_static = False):
        self.__connector = connector
        self.__is_first = is_first
        self.__is_static = is_static

    async def _generate(self, ent_conf: EntityConfig, data: List[Dict[str, any]]):
        self.__prepare_incorrect_values(data, ent_conf)
        self.__drop_and_insert_table(data, ent_conf)

    def __drop_and_insert_table(self, data: List[Dict[str,any]], ent_conf: EntityConfig):
        table = BaseTable(self.__connector, ent_conf)
        if not self.__is_static:
            table._drop_and_create()
        elif self.__is_first:
            self.__is_first = False
            table._create()
        table._add_data(data)

    def __prepare_incorrect_values(self, data: List[Dict[str, any]], ent_conf: EntityConfig):
        for element in data:
            self.__separate_json_fields(element, ent_conf)
            self.__set_empty_str_to_none(element, ent_conf)

        return element

    def __set_empty_str_to_none(self, element: Dict[str, any], ent_conf: EntityConfig):
        str_field_keys = \
            get_list_keys_from_dict_of_condition(ent_conf.field_to_py_type, 'int') \
            + get_list_keys_from_dict_of_condition(ent_conf.field_to_py_type, 'double') \
            + get_list_keys_from_dict_of_condition(ent_conf.field_to_py_type, 'date') \
            + get_list_keys_from_dict_of_condition(ent_conf.field_to_py_type, 'enum')

        for key in str_field_keys:
            try:
                if element[key] == '':
                    element[key] = None
            except Exception as error:
                Print().print_error(f'BaseTable.__set_empty_str_to_none() {error}')

    def __separate_json_fields(self, element: Dict[str, any], ent_conf: EntityConfig):
        json_field_keys = get_list_keys_from_dict_of_condition(ent_conf.field_to_py_type, 'json')

        for key in json_field_keys:
            if element[key] == None:
                element[key] = {
                    'valueId': None,
                    'value': None
                }