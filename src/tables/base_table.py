import copy
from typing import Dict

from sqlalchemy import Table, select, func

from core.connectors.db_connector import DBConnector
from core.entity_configs.entity_config import EntityConfig
from tables.base_columns import BaseColumns
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
    def tablename(self):
        return self.__tablename__

    def __init__(self, connector: DBConnector, entity_config: EntityConfig):
        self.__metadata = connector.metadata
        self.__engine = connector.engine
        self.__connection = connector.connection

        self.__entity_config = entity_config

        self.__columns = BaseColumns(self.__entity_config).column_list
        self.__tablename__ = self.__entity_config.entity_name.replace('.', '_')

        self.__table = Table(self.tablename, self.__metadata, *self.__columns)

    def _drop_and_create(self):
        self.__drop()
        self.__create()

    def _add_data(self, data: Dict[str, any]):
        print_success(f'Добавление данных в таблицу {self.tablename}...')
        call_counter = 0
        for element in data:
            element = self.__prepare_incorrect_values(key_dict_to_lower(element))
            
            try:
                element = { k: v for k, v in element.items() if k in self.__entity_config.keys_lower }
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
                print_error(f'Не удалось добавить запись в таблицу {self.tablename}. Ошибка: {error}')

        query = select([func.count()]).select_from(self.__table)
        count_query = self.__connection.execute(query).scalar()

        if call_counter == count_query:
            # TelegramBot._send_success_message(f'Все записи успешно добавлены в таблицу {self.tablename} - {count_query}')
            print_success(f'Все записи успешно добавлены в таблицу {self.tablename} - {count_query}')
        else:
            print_error(f'Не все записи добавлены в таблицу {self.tablename}. Добавлено {count_query}, а пришло {call_counter}')
            # TelegramBot._send_error_message(f'Не все записи добавлены в таблицу {self.tablename}. Добавлено {count_query}, а пришло {call_counter}')

        self.__connection.close()

    def __create(self):
        try:
            self.__metadata.create_all(bind = self.__engine)
            print_success(f'Таблица {self.tablename} успешно создана')
        except Exception as error:
            print_error(error)

    def __drop(self):
        self.__metadata.drop_all(bind = self.__engine)
        print_success(f'Таблица {self.tablename} успешно удалена')

    def __prepare_incorrect_values(self, element: Dict[str, any]):
        self.__separate_json_fields(element)
        self.__set_empty_str_to_none(element)

        return element

    def __set_empty_str_to_none(self, element: Dict[str, any]):
        """
        Если появляется тип, отличный от char / text, нужно добавить его сюда
        """
        str_field_keys = get_list_keys_from_dict_of_condition(self.__entity_config.field_keys_and_values_lower, 'int') \
            + get_list_keys_from_dict_of_condition(self.__entity_config.field_keys_and_values_lower, 'double') \
            + get_list_keys_from_dict_of_condition(self.__entity_config.field_keys_and_values_lower, 'date') \
            + get_list_keys_from_dict_of_condition(self.__entity_config.field_keys_and_values_lower, 'enum')

        for key in str_field_keys:
            if element[key] == '':
                element[key] = None

    def __separate_json_fields(self, element: Dict[str, any]):
        json_field_keys = get_list_keys_from_dict_of_condition(self.__entity_config.field_keys_and_values_lower, 'json')

        for key in json_field_keys:
            if element[key] == None:
                element[key] = {
                    'valueId': None,
                    'value': None
                }
