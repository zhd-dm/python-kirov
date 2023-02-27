from typing import Dict, List, Union


from utils.mapping import key_dict_in_list_to_lower, get_field_from_list_of_dicts_by_keys, get_dict_keys_from_list

from core.connectors.db_connector import DBConnector
from features.bitrix.bx_api import BXApi
from core.entity_configs.entity_config import EntityConfig
from core.data_handlers.config.constants import ENTITIES_WITH_CUSTOM_PARAMS

from features.print.print import Print


class EntityDataImporter:

    def __init__(self, connector: DBConnector, ent_conf: EntityConfig):
        self.__connection = connector.connection
        self.__ent_conf = ent_conf

        if ent_conf.params != '':
            Print().print_info('Генерация динамической таблицы...')
        else:
            Print().print_info('Генерация статической таблицы...')

        if ent_conf.entity_name in ENTITIES_WITH_CUSTOM_PARAMS():
            self.__replace_custom_params(ENTITIES_WITH_CUSTOM_PARAMS(self.__connection))

    async def _get_bx_data(self) -> List[Dict[str, any]]:
        data: List[Dict[str, any]] = None

        try:
            data = get_field_from_list_of_dicts_by_keys(
                key_dict_in_list_to_lower(await BXApi()._get_bx_data(self.__ent_conf)),
                get_dict_keys_from_list(self.__ent_conf.field_to_py_type)
            )
        except Exception as error:
            Print().print_error(f'EntityDataImporter._get_bx_data() {error}')

        return data

    # def _get_currencies_data(self, day: datetime = None) -> List[Dict[str, any]]:
    #     data: List[Dict[str, any]] = None
    #     curr = Currencies(day)
    #     curr_conn = CurrenciesConnector()
    #     try:
    #         data = get_dicts_from_list_of_dicts_by_codes(
    #             try_set_int_in_list_of_dicts(key_dict_in_list_to_lower(curr.currencies)),
    #             'charcode',
    #             curr_conn.includes_corr_codes
    #         )
    #     except Exception as error:
    #         Print().print_error(f'EntityDataImporter._get_curr_data() {error}')

    #     return data

    def __replace_custom_params(self, entities_with_custom_params: Dict):
        self.__ent_conf._replace_custom_params(entities_with_custom_params.get(self.__ent_conf.entity_name))