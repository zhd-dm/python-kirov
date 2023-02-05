import copy
from typing import Dict

from sqlalchemy.engine import Engine
from sqlalchemy import MetaData, Table


from utils import print_error, print_success, key_dict_to_lower
from fields.base_config import BaseConfig
from tables.base_columns import BaseColumns


class BaseTable:

    @property
    def tablename(self):
        return self.__tablename__

    def __init__(self, engine: Engine, entity_config: BaseConfig):
        self.__metadata = MetaData()
        self.__engine = engine
        self.__connection = engine.connect()

        self.__entity_config = entity_config

        self.__columns = BaseColumns(self.__entity_config).column_list
        self.__tablename__ = self.__entity_config.entity_name.replace('.', '_')

        self.__table = Table(self.tablename, self.__metadata, *self.__columns)

    def _drop_and_create(self):
        self.__drop()
        self.__create()

    def _add_data(self, data: Dict[str, any]):
        for element in data:
            element = self.__empty_str_to_none(key_dict_to_lower(element))
            
            try:
                # DEPRECATED
                element = { k: v for k, v in element.items() if k in self.__entity_config.keys_lower }
                element_copy = copy.deepcopy(element)

                for k, v in element_copy.items():
                    if isinstance(v, dict):
                        json = element[k]
                        element[f'{k}_id'] = json['valueId']
                        element[f'{k}_value'] = json['value']
                        del element[k]

                self.__connection.execute(self.__table.insert().values(**element))
        
            except Exception as error:
                print_error(f'Не удалось добавить запись в таблицу {self.tablename}. Ошибка: {error}')
        
        # self.__check_is_all_values_added_to_table(data)
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

    def __empty_str_to_none(self, element: Dict[str, any]):
        #
        # Для crm.deal.list
        if self.tablename == 'deal':
            if element['closedate'] == '':
                element['closedate'] = None
            if element['uf_crm_1667025237906'] == '':
                element['uf_crm_1667025237906'] = None

        #
        # Для crm.product.list
        if (self.tablename == 'product' and element['property_119'] == None):
            element['property_119'] = {
                'valueId': None,
                'value': None
            }

        #
        # Для catalog.product.sku.list
        if (self.tablename == 'product_sku' and element['property119'] == None):
            element['property119'] = {
                'valueId': None,
                'value': None
            }

        return element

    # def __check_is_all_values_added_to_table(self, data):
    #     query = "SELECT count(*) FROM " + self.tablename
    #     result = self.__connection.execute(query).scalar()

    #     if result != data.__len__():
    #         print_error(f'{data.__len__() - self.__count_records} записи не было занесено в таблицу {self.tablename}')
    #     else:
    #         print_success(f'OK Все записи были успешно добавлены в таблицу {self.tablename}')