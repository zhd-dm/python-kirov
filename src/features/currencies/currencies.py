import asyncio
import datetime
from datetime import datetime
from typing import Dict, List

from utils.mapping import get_dicts_from_list_of_dicts_by_codes, try_set_int_in_list_of_dicts, key_dict_in_list_to_lower
from core.connectors.db_connector import DBConnector
from core.data_handlers.table_generator import TableGenerator
from core.entity_configs.entity_config import EntityConfig
from core.entity_configs.entity_config_wrapper import EntityConfigWrapper

from features.date_transformer.date_transformer import DateTransformer
from features.date_transformer.config.constants import DAYS_IN_HALF_YEAR, DAYS_IN_WEEK
from features.currencies.currencies_api import CurrenciesApi
from features.currencies.currencies_connector import CurrenciesConnector
from features.print.print import Print


class Currencies:

    def __init__(self):
        self.__curr_conn = CurrenciesConnector()
        self.__curr_api = CurrenciesApi()

    async def _generate_currencies_table(self, db_conn: DBConnector, is_first: bool):
        curr_conn = self.__curr_conn
        field_to_py_type = curr_conn.field_to_py_type
        curr_entity_conf = curr_conn.entity_conf_list

        match is_first:
            case False:
                pass
            case True:
                await self.__create_currencies_table(db_conn, curr_conn, field_to_py_type, curr_entity_conf)

    async def __create_currencies_table(self,
        db_conn: DBConnector,
        curr_conn: CurrenciesConnector,
        field_to_py_type: Dict[str, str],
        curr_entity_conf: List[str]
    ):
        table_gen = TableGenerator(db_conn, is_first = True, is_static = True)
        list_of_dates: List[datetime] = DateTransformer()._get_list_of_dates(DAYS_IN_HALF_YEAR)

        for day in list_of_dates:
            en_conf_with_fields = EntityConfigWrapper(field_to_py_type, curr_entity_conf).entity_config_with_fields
            en_conf = EntityConfig(en_conf_with_fields)
            data = self.__get_currencies_data_by_day(curr_conn, day)

            await table_gen._generate(en_conf, data)
            await asyncio.sleep(0.3)

        Print().print_info('Таблица currency обновлена')

    def __get_currencies_data_by_day(self, curr_conn: CurrenciesConnector, day: datetime = None) -> List[Dict[str, any]]:
        data: List[Dict[str, any]] = None
        try:
            data = get_dicts_from_list_of_dicts_by_codes(
                try_set_int_in_list_of_dicts(key_dict_in_list_to_lower(self.__curr_api._get_currencies(day))),
                'charcode',
                curr_conn.includes_corr_codes
            )
        except Exception as error:
            Print().print_error(f'Currencies._get_curr_data() {error}')

        return data