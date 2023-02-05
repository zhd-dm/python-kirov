#
# Файл утилит должен быть без зависимостей от других модулей приложения !!!
#

import json
from typing import Union, List, Dict


def key_dict_to_lower(dict: Dict[str, any]) -> Dict[str, any]:
    return { key.lower(): value for key, value in dict.items() }

def props_list_to_lower(list: List[str]) -> List[str]:
    return [ value.lower() for value in list ]

def get_dict_by_indexes_of_matrix(key_i: int, key_v: int, list: List[List[any]]) -> Dict[str, any]:
    """
    Метод генерации словаря из матрицы

    Аргументы:
    - `key_i: int` - ключ, который будет ключом в словаре
    - `key_v: int` - ключ, который будет значением в словаре
    - `list: List[List[any]]` - входящая матрица

    Пример:

    Если key_i = 1, а key_v = 2, и на вход получаем такую матрицу:

    [['a', 'b', 'c'], [1, 2, 3], ['d', 2, 0]] -> { 'a': 'b', 1: 2, 'd': 2 }
    """
    return { i[key_i]: i[key_v] for i in list }

def find_list_of_matrix(from_index: int, condition: str, list: List[List[any]]) -> List[any]:
    """
    Метод поиска списка из матрицы

    Аргументы:
    - `from_index: int` - индекс, по которому будем сравнивать
    - `condition: int` - чему должно быть равно значение этого индекса
    - `list: List[List[any]]` - входящая матрица

    Пример:

    Если from_index = 0, а condition = 'd', и на вход получаем такую матрицу:

    [['a', 'b', 'c'], [1, 2, 3], ['d', 2, 0]] -> ['d', 2, 0]
    """
    return next(item for item in list if item[from_index] == condition)

def convert_list_to_dict(keys: List[str], list: List[any]) -> Dict[str, any]:
    """
    Метод преобразования списка в словарь с заданными ключами

    Аргументы:
    - `keys: List[str]` - список ключей, которые будут заданы полям словаря
    - `list: List[any]` - исходный список

    Пример:

    Если keys = ['a', 'b', 'c'], и на вход получаем такой список:

    ['super', 1, None] -> { 'a': 'super', 'b': 1, 'c': None }
    """
    return dict(zip(keys, list))

def convert_str_to_dict_or_list(string: str) -> Union[List[any], Dict[str, any]]:
    """
    Метод преобразования строки в список или словарь если это возможно

    Аргументы:
    - `string: str` - входная строка

    Пример:

    Если string = "['a', b, 'c']"

    string -> ['a', 'b', 'c'], аналогично со словарем
    """

    if string.startswith('{'):
        return json.loads(string.replace("'", '"'))
    if string.startswith('['):
        return list(map(str, string[1:-1].split(', ')))
    if ',' in string:
        return string.replace(' ', '').split(",")

    return string

def print_success(message: str):
    print(f"""
        ------ SUCCESS----------------------------------------------------------- SUCCESS ------
            {message}
        ----------------------------------------------------------------------------------------
        """
    )

def print_error(error: Exception):
    print(f"""
        ------ ERROR----------------------------------------------------------- ERROR ------
            {error}
        ------------------------------------------------------------------------------------
        """
    )



# def is_exist_db(db_url: str) -> bool:
#     return database_exists(db_url)

# def is_empty_table(session: Session, table) -> bool:
#     return session.query(table).count() == 0

# def is_exist_table(engine: Engine, tablename: str) -> bool:
#     return sqlalchemy.inspect(engine).has_table(tablename)

# def in_full_record_table(session: Session, table, number_of_records: int) -> bool:
#     return session.query(table).count() == number_of_records

# def records_in_table(session: Session, table) -> int:
#     return session.query(table).count()
