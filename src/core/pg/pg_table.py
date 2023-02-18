from core.pg.config.types import T_PG_TABLE, T_PG_FIELDS, T_PG_ENUMS
from core.pg.config.utils import _invalid_conf


class PGTable:
    """
    Класс для типизации конфига PG таблицы.

    В нем указан минимальный набор полей, необходимых для генерации таблицы.

    Обязательно оборачивать конфиг любой таблицы (динамической, статической) в этот класс.

    Параметры:
    `table_conf: T_PG_TABLE` -> Конфиг таблицы
    """

    def __init__(self, table_conf: T_PG_TABLE):
        if not _invalid_conf(table_conf):
            self.__table_conf = table_conf

    @property
    def name(self) -> str:
        return self.__table_conf.get('name')
    
    @property
    def primary_key(self) -> str:
        return self.__table_conf.get('primary_key')

    @property
    def fields(self) -> T_PG_FIELDS:
        return self.__table_conf.get('fields')

    @property
    def enums(self) -> T_PG_ENUMS:
        return self.__table_conf.get('enums')