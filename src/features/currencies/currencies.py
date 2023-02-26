import asyncio
from datetime import datetime
from typing import Dict, List

from sqlalchemy import select, func

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

    @property
    def is_first(self):
        return not self.__table_gen.is_exist or self.__table_gen.is_empty

    def __init__(self, db_conn: DBConnector):
        self.__db_conn = db_conn
        self.__curr_conn = CurrenciesConnector()
        self.__curr_api = CurrenciesApi()
        self.__table_gen = TableGenerator(self.__db_conn, self.__get_en_conf())

    async def _generate(self):
        dates_interval = DAYS_IN_WEEK
        count_dates = dates_interval if self.is_first else self.__get_count_of_missing_days()
        list_of_dates: List[datetime] = DateTransformer()._get_list_of_dates(count_dates) 

        for day in list_of_dates:
            if not self.is_first:
                self.__update_table(day)
            else:
                self.__create_table()
                self.__update_table(day)

            await asyncio.sleep(0.3)

        if list_of_dates.__len__() == 0:
            Print().print_info(f'Нечего обновлять в таблице {self.__table_gen.orm_table.name}')
    
    def __get_en_conf(self):
        curr_conn = self.__curr_conn
        field_to_py_type = curr_conn.field_to_py_type
        curr_entity_conf = curr_conn.entity_conf_list
        en_conf_with_fields = EntityConfigWrapper(field_to_py_type, curr_entity_conf).entity_config_with_fields
        return EntityConfig(en_conf_with_fields)

    def __create_table(self):
        self.__table_gen._create()

    def __update_table(self, day: datetime):
        data = self.__get_currencies_data_by_day(day)
        self.__table_gen._add_data(data)
        Print().print_info(f'Таблица {self.__table_gen.orm_table.name} обновлена')

    def __get_count_of_missing_days(self) -> int:
        orm_table = self.__table_gen.orm_table
        query = select([func.max(orm_table.columns.date)]).select_from(orm_table)
        max_date: datetime = self.__db_conn.connection.execute(query).scalar()
        now = datetime.now()
        orm_last_date = datetime.combine(max_date, datetime.min.time())
        return DateTransformer()._get_count_difference_days(now, orm_last_date)

    def __get_currencies_data_by_day(self, day: datetime = None) -> List[Dict[str, any]]:
        pure_data: List[Dict[str, any]] = None

        try:
            data = self.__curr_api._get_currencies(day)
            pure_data = get_dicts_from_list_of_dicts_by_codes(
                try_set_int_in_list_of_dicts(key_dict_in_list_to_lower(data)),
                'charcode',
                self.__curr_conn.includes_corr_codes
            )
        except Exception as error:
            Print().print_error(f'Currencies.__get_currencies_data_by_day() {error}')

        return pure_data