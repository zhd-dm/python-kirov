from sqlalchemy import Table


from connectors.db_connector import DBConnector
from tables.base_columns import BaseColumns
from entity_configs.entity_config import EntityConfig


from core.tech_tables.config.constants import FIELDS_WITH_TYPES_TABLE_CONFIG

from utils.mapping import print_success, print_error


class FieldsWithTypes:
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

    def __init__(self, connector: DBConnector):
        self.__metadata = connector.metadata
        self.__engine = connector.engine

        self.__tablename__ = 'fields_with_types'
        self.__table_config = EntityConfig(FIELDS_WITH_TYPES_TABLE_CONFIG)
        self.__columns = BaseColumns(self.__table_config).column_list
        self.__table = Table(self.tablename, self.__metadata, *self.__columns)

    def _drop_and_create(self):
        self.__drop()
        self.__create()

    def __create(self):
        try:
            self.__metadata.create_all(bind = self.__engine)
            print_success(f'Таблица {self.tablename} успешно создана')
        except Exception as error:
            print_error(error)

    def __drop(self):
        self.__metadata.drop_all(bind = self.__engine)
        print_success(f'Таблица {self.tablename} успешно удалена')