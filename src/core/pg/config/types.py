from typing import Union, List, Dict

# ================== Базовые типы для конфига PG таблицы ==================

T_PG_PRIMARY_KEY = str
T_PG_FIELDS = Dict[str, str]
T_PG_ENUMS = Dict[str, List[any]]

T_PG_TABLE = Dict[str, Union[T_PG_PRIMARY_KEY, T_PG_FIELDS, T_PG_ENUMS]]

