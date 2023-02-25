import asyncio
from typing import List, Dict


from utils.mapping import get_list_keys_from_dict_of_condition, print_error
from core.connectors.db_connector import DBConnector
from core.tables.base_table import BaseTable
from core.entity_configs.entity_config import EntityConfig

from core.data_handlers.bx_data_importer import BXDataImporter

from features.google_sheets.config.types import T_SHEET_VALUES_RETURN


class TableGenerator:

    def __init__(self, connector: DBConnector):
        self.__connector = connector

    async def _generate(self, ent_conf: EntityConfig):
        data_importer = BXDataImporter(self.__connector, ent_conf)
        data = await data_importer._get_data()

        self.__prepare_incorrect_values(data, ent_conf)
        self.__drop_and_insert_table(data, ent_conf)

        await asyncio.sleep(1)

    def __drop_and_insert_table(self, data: List[Dict[str,any]], ent_conf: EntityConfig):
        table = BaseTable(self.__connector, ent_conf)
        table._drop_and_create()
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
                print_error(f'BaseTable.__set_empty_str_to_none() {error}')

    def __separate_json_fields(self, element: Dict[str, any], ent_conf: EntityConfig):
        json_field_keys = get_list_keys_from_dict_of_condition(ent_conf.field_to_py_type, 'json')

        for key in json_field_keys:
            if element[key] == None:
                element[key] = {
                    'valueId': None,
                    'value': None
                }