import copy
from typing import Dict

from sqlalchemy import Table, select, func

from core.connectors.db_connector import DBConnector
from core.entity_configs.entity_config import EntityConfig
from core.tables.base_columns import BaseColumns
from features.print.print import Print


class BaseTable:

    @property
    def table(self):
        return self.__table

    @property
    def is_exist(self):
        return self.__table.exists(bind = self.__engine)

    @property
    def is_empty(self):
        query = select(self.__table)
        return self.__engine.execute(query).fetchall().__len__() == 0

    @property
    def _tablename(self):
        return self.__tablename__

    def __init__(self, connector: DBConnector, ent_conf: EntityConfig, is_static: bool):
        self.__metadata = connector.metadata
        self.__engine = connector.engine
        self.__connection = connector.connection

        self.__ent_conf = ent_conf
        self.__columns = BaseColumns(self.__ent_conf).column_list
        self.__tablename__ = self.__ent_conf.entity_name.replace('.', '_')
        self.__table = Table(self._tablename, self.__metadata, *self.__columns)

        self.__is_static = is_static
        self.__old_recs_len = self.__get_count_query() if self.__is_static and self.is_exist else 0

    # DEPRECATED
    def _drop_and_create(self):
        self._drop()
        self._create()

    def _add_data(self, data: Dict[str, any]):
        Print().print_info(f'Добавление данных в таблицу {self._tablename}...')
        for element in data:
            try:
                element_copy = copy.deepcopy(element)

                for k, v in element_copy.items():
                    if isinstance(v, dict):
                        json = element[k]
                        element[f'{k}_id'] = json['valueId']
                        element[f'{k}_value'] = json['value']
                        del element[k]

                self.__connection.execute(self.__table.insert().values(**element))

            except Exception as error:
                Print().print_error(f'Не удалось добавить запись в таблицу {self._tablename}. Ошибка: {error}')

            if self.__is_static:
                Print().print_info(f'Таблица {self._tablename} обновлена')

    def _create(self):
        if self.is_exist:
            self._drop()
        try:
            self.__metadata.create_all(bind = self.__engine)
            Print().print_success(f'Таблица {self._tablename} успешно создана')
        except Exception as error:
            Print().print_error(error)

    def _drop(self):
        self.__metadata.drop_all(bind = self.__engine)
        Print().print_success(f'Таблица {self._tablename} успешно удалена')

    def _check_add_status(self, records_len: int):
        now_count_recs = self.__get_count_query()
        self.__print_add_status(now_count_recs, records_len)

    def __get_count_query(self):
        query = select([func.count()]).select_from(self.__table)
        count: int = self.__connection.execute(query).scalar()
        return count

    def __print_add_status(self, now_count: int, records_len: int):
        if records_len == 0:
            Print().print_info(f'Нечего обновлять в таблице {self._tablename}')
        elif now_count == records_len or now_count - self.__old_recs_len == records_len:
            Print().print_success(f'Все записи успешно добавлены в таблицу {self._tablename} - {records_len}')
        else:
            Print().print_error(f'Не все записи добавлены в таблицу {self._tablename}. Добавлено {now_count}, а пришло {records_len}')