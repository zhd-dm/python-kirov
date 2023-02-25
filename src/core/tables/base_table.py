import copy
from typing import Dict

from sqlalchemy import Table, select, func

from core.connectors.db_connector import DBConnector
from core.entity_configs.entity_config import EntityConfig
from core.tables.base_columns import BaseColumns
from utils.mapping import print_error, print_success, key_dict_to_lower, get_list_keys_from_dict_of_condition


class BaseTable:
    """
    Класс генерации таблицы в БД по переданному EntityConfig

    Параметры:
    - `connector: DBConnector` - класс для подключения к БД
    - `entity_config: EntityConfig` - entity_config
    
    Геттеры:
    - `tablename -> str` - название таблицы
    """

    @property
    def _tablename(self):
        return self.__tablename__

    def __init__(self, connector: DBConnector, ent_conf: EntityConfig):
        self.__metadata = connector.metadata
        self.__engine = connector.engine
        self.__connection = connector.connection

        self.__ent_conf = ent_conf

        self.__columns = BaseColumns(self.__ent_conf).column_list

        self.__tablename__ = self.__ent_conf.entity_name.replace('.', '_')

        self.__table = Table(self._tablename, self.__metadata, *self.__columns)

    def _drop_and_create(self):
        self.__drop()
        self.__create()

    def _add_data(self, data: Dict[str, any]):
        print_success(f'Добавление данных в таблицу {self._tablename}...')
        call_counter = 0
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
                call_counter += 1

            except Exception as error:
                print_error(f'Не удалось добавить запись в таблицу {self._tablename}. Ошибка: {error}')

        query = select([func.count()]).select_from(self.__table)
        count_query = self.__connection.execute(query).scalar()

        if call_counter == count_query:
            # TelegramBot._send_success_message(f'Все записи успешно добавлены в таблицу {self.tablename} - {count_query}')
            print_success(f'Все записи успешно добавлены в таблицу {self._tablename} - {count_query}')
        else:
            print_error(f'Не все записи добавлены в таблицу {self._tablename}. Добавлено {count_query}, а пришло {call_counter}')
            # TelegramBot._send_error_message(f'Не все записи добавлены в таблицу {self.tablename}. Добавлено {count_query}, а пришло {call_counter}')

        self.__connection.close()

    def __create(self):
        try:
            self.__metadata.create_all(bind = self.__engine)
            print_success(f'Таблица {self._tablename} успешно создана')
        except Exception as error:
            print_error(error)

    def __drop(self):
        self.__metadata.drop_all(bind = self.__engine)
        print_success(f'Таблица {self._tablename} успешно удалена')
