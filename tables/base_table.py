import copy
from typing import Dict

from sqlalchemy import Table, select, func


from utils import Settings, print_error, print_success, key_dict_to_lower
from fields.base_config import BaseConfig
from tables.base_columns import BaseColumns


class BaseTable:
    """
    Класс генерации таблицы в БД по переданному BaseConfig

    Параметры:
    - `settings: Settings` - класс для подключения к БД
    - `entity_config: BaseConfig` - entity_config
    
    Геттеры:
    - `tablename -> str` - название таблицы
    """

    @property
    def tablename(self):
        return self.__tablename__

    def __init__(self, settings: Settings, entity_config: BaseConfig):
        self.__metadata = settings.metadata
        self.__engine = settings.engine
        self.__connection = settings.connection

        self.__entity_config = entity_config

        self.__columns = BaseColumns(self.__entity_config).column_list
        self.__tablename__ = self.__entity_config.entity_name.replace('.', '_')

        self.__table = Table(self.tablename, self.__metadata, *self.__columns)

    def _drop_and_create(self):
        self.__drop()
        self.__create()

    def _add_data(self, data: Dict[str, any]):
        call_counter = 0
        for element in data:
            element = self.__empty_str_to_none(key_dict_to_lower(element))
            
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

    def __empty_str_to_none(self, element: Dict[str, any]):

        #
        # REFACTOR:
        # Продумать более лаконичную обработку невалидных значений и json
        #

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