import asyncio
from typing import List, Dict


from utils.mapping import get_list_keys_from_dict_of_condition

from core.connectors.db_connector import DBConnector
from core.tables.base_table import BaseTable
from core.entity_configs.entity_config import EntityConfig
from features.print.print import Print


class TableGenerator:

    @property
    def orm_table(self):
        return self.__table.table

    @property
    def is_exist(self):
        return self.__table.is_exist

    @property
    def is_empty(self):
        return self.__table.is_empty

    def __init__(self, connector: DBConnector, en_conf: EntityConfig, is_static = False):
        self.__table = BaseTable(connector, en_conf, is_static)
        self.__en_conf = en_conf

    # DEPRECATED
    def _gen_dynamic(self, data: List[Dict[str, any]]):
        self.__prepare_incorrect_values(data)
        self.__drop_and_insert_table(data)

    def _create(self):
        self.__table._create()

    def _add_data(self, data: List[Dict[str,any]]):
        self.__prepare_incorrect_values(data)
        self.__table._add_data(data)

    def _check_add_status(self, records_len: int):
        self.__table._check_add_status(records_len)

    # DEPRECATED
    def __drop_and_insert_table(self, data: List[Dict[str,any]]):
        self.__table._drop_and_create()
        self._add_data(data)

    def __prepare_incorrect_values(self, data: List[Dict[str, any]]):
        for element in data:
            self.__separate_json_fields(element)
            self.__set_empty_str_to_none(element)

    def __set_empty_str_to_none(self, element: Dict[str, any]):
        en_conf = self.__en_conf
        str_field_keys = \
            get_list_keys_from_dict_of_condition(en_conf.field_to_py_type, 'int') \
            + get_list_keys_from_dict_of_condition(en_conf.field_to_py_type, 'double') \
            + get_list_keys_from_dict_of_condition(en_conf.field_to_py_type, 'date') \
            + get_list_keys_from_dict_of_condition(en_conf.field_to_py_type, 'enum')

        for key in str_field_keys:
            try:
                if element[key] == '':
                    element[key] = None
            except Exception as error:
                Print().print_error(f'TableGenerator.__set_empty_str_to_none() {error}')

    def __separate_json_fields(self, element: Dict[str, any]):
        en_conf = self.__en_conf
        json_field_keys = get_list_keys_from_dict_of_condition(en_conf.field_to_py_type, 'json')

        for key in json_field_keys:
            if element[key] == None:
                element[key] = {
                    'valueId': None,
                    'value': None
                }