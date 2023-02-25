from typing import Dict, List, Union


from utils.mapping import print_error, print_info, key_dict_in_list_to_lower, get_pure_list_of_dicts, get_dict_keys_from_list, try_set_int_in_list_of_dicts

from core.connectors.db_connector import DBConnector
from core.api_calls.bx_api import BXApi
from core.entity_configs.entity_config import EntityConfig
from core.data_handlers.config.constants import ENTITIES_WITH_CUSTOM_PARAMS

from features.currencies.currencies import Currencies



class EntityDataImporter:

    def __init__(self, connector: DBConnector, ent_conf: EntityConfig):
        self.__connection = connector.connection
        self.__ent_conf = ent_conf

        if ent_conf.params != '':
            print_info('Генерация динамической таблицы...')
        else:
            print_info('Генерация статической таблицы...')

        if ent_conf.entity_name in ENTITIES_WITH_CUSTOM_PARAMS():
            self.__replace_custom_params(ENTITIES_WITH_CUSTOM_PARAMS(self.__connection))

    async def _get_bx_data(self) -> List[Dict[str, any]]:
        data: List[Dict[str, any]] = None

        try:
            data = get_pure_list_of_dicts(
                key_dict_in_list_to_lower(await BXApi()._get_bx_data(self.__ent_conf)),
                get_dict_keys_from_list(self.__ent_conf.field_to_py_type)
            )
        except Exception as error:
            print_error(f'DataImporter._get_bx_data() {error}')

        return data

    def _get_currencies_data(self) -> List[Dict[str, any]]:
        data: List[Dict[str, any]] = None

        try:
            data = try_set_int_in_list_of_dicts(
                key_dict_in_list_to_lower(Currencies().currencies)
            )
        except Exception as error:
            print_error(f'DataImporter._get_curr_data() {error}')

        return data

    def __replace_custom_params(self, entities_with_custom_params: Dict):
        self.__ent_conf._replace_custom_params(entities_with_custom_params.get(self.__ent_conf.entity_name))