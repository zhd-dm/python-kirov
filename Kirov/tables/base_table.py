from typing import Dict

from sqlalchemy.engine import Engine
from sqlalchemy import MetaData, Table

# Local imports
from fields.base_entity_config import BaseConfig
from tables.base_columns import BaseColumns
from utils import print_error, print_success, key_dict_to_lower


class BaseTable:

    @property
    def tablename(self):
        return self.__tablename__

    def __init__(self, engine: Engine, metadata: MetaData, entity_config: BaseConfig):
        self.__metadata = metadata
        self.__engine = engine
        self.__connection = engine.connect()

        self.__entity_config = entity_config

        self.__columns = BaseColumns(self.__entity_config).column_list
        self.__tablename__ = self.__entity_config.entity_name
        self.__table = Table(self.tablename, self.__metadata, *self.__columns)

        self.__count_records = 0

    def _drop_and_create(self):
        self.__drop()
        self.__create()

    def _add_data(self, data: Dict[str, any]):
        for element in data:
            element = self.__empty_str_to_none(key_dict_to_lower(element))
            
            try:
                element = { k: v for k, v in element .items() if k in self.__entity_config.keys_lower }
                self.__connection.execute(self.__table.insert().values(**element))
                self.__count_records += 1
                print_success(f'Запись успешно добавлена в таблицу {self.tablename}')
        
            except Exception as error:
                print_error(f'Не удалось добавить запись в таблицу {self.tablename}. Ошибка: {error}')
        
        self.__check_all_data_added_to_table(data)
        self.__connection.close()

    def __create(self):
        try:
            self.__metadata.create_all(bind = self.__engine)
            print_success(f'Таблица {self.tablename} успешно создана')
        except Exception as error:
            print_error(error)

    def __drop(self):
        self.__metadata.drop_all(bind = self.__engine)

    def __empty_str_to_none(self, data: Dict[str, any]):
        #
        # Для crm.deal.list
        if (data['closedate'] == ''):
            data['closedate'] = None

        return data

    def __check_all_data_added_to_table(self, data):
        if self.__count_records != data.__len__():
            print_error(f'{data.__len__() - self.__count_records} записи не было занесено в таблицу')
        else:
            print_success(f'OK Все записи были успешно добавлены в таблицу {self.tablename}')