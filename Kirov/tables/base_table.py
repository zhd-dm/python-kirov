from typing import Dict

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table, Column, Integer, String, Float, Text, Date
from sqlalchemy.dialects.postgresql import ENUM

# Local imports
from fields.base_entity_config import BaseConfig
from tables.base_columns import BaseColumns
from utils import print_error, print_success, key_dict_to_lower


class BaseTable:

    @property
    def tablename(self):
        return self.__tablename__

    def __init__(self, engine: Engine, entity_config: BaseConfig, **kwarg):
        self.__engine = engine
        self.__entity_config = entity_config
        self.__columns = BaseColumns(self.__entity_config).column_list
        
        self.__metadata = MetaData()

        self.__tablename__ = self.__entity_config.entity_name
        self.__table = Table(self.tablename, self.__metadata, *self.__columns)
        
        # self.__Session = sessionmaker(bind = self.__engine)
        # self.__session = self.__Session()

        self.__connection = engine.connect()

        # if kwarg:
        #     self.__set_attributes(kwarg)

        if not kwarg:
            pass

        # if kwarg:
        #     self.__add_data(kwarg)

    def _drop_and_create(self):
        self.__drop()
        self.__create()

    def _add_data(self, data: Dict[str, any]):
        for obj in data:
            obj = self.__empty_str_to_none(key_dict_to_lower(obj))
            
            try:
                # new_entry = self.__table(**obj)
                
                obj = { k: v for k, v in obj.items() if k in self.__entity_config.keys }
                self.__connection.execute(self.__table.insert().values(**obj))
                # self.__session.add(new_entry)
                # self.__session.commit()
                print_success(f'Запись успешно добавлена в таблицу {self.tablename}')
        
            except Exception as error:
                print_error(f'Не удалось добавить запись в таблицу {self.tablename}. Ошибка: {str(error)}')
                # self.__session.rollback()
            finally:
                pass
                # self.__session.close()

    def __create(self):
        try:
            self.__metadata.create_all(bind = self.__engine)
            print_success(f'Таблица {self.tablename} успешно создана')
        except Exception as error:
            print_error(error)

    def __drop(self):
        self.__metadata.drop_all(bind = self.__engine)

    # def __set_attributes(self, data: Dict[str, any]):
    #     self.__empty_str_to_none(key_dict_to_lower(data))
        
    #     for key, value in data.items():
    #         setattr(self, key, value)

    def __empty_str_to_none(self, data: Dict[str, any]):
        #
        # Для crm.deal.list
        if (data['closedate'] == ''):
            data['closedate'] = None

        return data