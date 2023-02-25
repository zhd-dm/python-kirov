#
# Модуль утилит должен быть без зависимостей от других модулей приложения !!!
#

import json
import copy
from typing import Union, List, Dict

from features.print.print import Print


def key_and_value_dict_to_lower(dict: Dict[str, str]) -> Dict[str, str]:
    return { key.lower(): v.lower() for key, v in dict.items() if isinstance(key, str) and isinstance(v, str) }

def key_dict_to_lower(dict: Dict[str, any]) -> Dict[str, any]:
    return { key.lower(): value for key, value in dict.items() if isinstance(key, str) }

def props_list_to_lower(list: List[str]) -> List[str]:
    return [ value.lower() for value in list if isinstance(value, str) ]

def key_dict_in_list_to_lower(list: List[Dict[str, any]]) -> List[Dict[str, any]]:
    new_list = []

    for dict in list:
        dict = key_dict_to_lower(dict)
        new_list.append(dict)

    return new_list

def get_field_from_list_of_dicts_by_keys(list_of_dicts: List[Dict[str, any]], keys_to_include: List[str]) -> List[Dict[str, any]]:
    clone_list = copy.deepcopy(list_of_dicts)
    result = []
    
    for d in clone_list:
        result.append({ k: v for k, v in d.items() if k in list(keys_to_include) })

    return result

def get_dicts_from_list_of_dicts_by_codes(list_of_dicts: List[Dict[str, any]], field_key: str, codes_to_include: List[str]) -> List[Dict[str, any]]:
    result: List[Dict[str, any]] = []

    for d in list_of_dicts:
        if d[field_key] in codes_to_include:
            result.append(d)

    return result

def get_dict_keys_from_list(dict: Dict[str, any]) -> List[str]:
    return list(dict.keys())

def try_set_int_in_list_of_dicts(list: List[Dict[str, str]]) -> List[Dict[str, Union[str, int, float]]]:
    result: List[Dict[str, Union[str, int, float]]] = []
    
    for dict in list:
        output_dict: Dict[str, Union[str, int, float]] = {}
        for key, value in dict.items():
            try:
                output_dict[key] = int(value)
            except ValueError:
                try:
                    output_dict[key] = float(value.replace(',', '.'))
                except ValueError:
                    output_dict[key] = value

        result.append(output_dict)

    return result

def get_list_keys_from_dict_of_condition(dict: Dict[str, any], condition: str) -> List[str]:
    """
    Метод получения списка ключей из словаря по условию

    Аргументы:
    - `dict: Dict[str, any]` - входной словарь
    - `condition: str` - условие, которому должно быть равно значение
    """

    return [ key for key, value in dict.items() if value == condition ]
    
def get_list_by_index_of_matrix(index: int, matrix: List[List[any]]) -> List[any]:
    """
    Метод генерации списка элементов по индексу из матрицы

    Аргументы:
    - `index: int` - индекс, по которому будут доставаться элементы
    - `matrix: List[List[any]]` - входная матрица
    """

    if not isinstance(matrix, list):
        Print().print_error(f'get_list_by_index_of_matrix() => Тип матрицы должен быть list')
        return matrix

    if index > matrix[0].__len__():
        Print().print_error(f'get_list_by_index_of_matrix() => Индекс не может быть больше чем длина списка внутри матрицы')
        return matrix

    if not all(len(list) == len(matrix[0]) for list in matrix):
        Print().print_error(f'get_list_by_index_of_matrix() => Не все списки в матрице равной длины')
        return matrix

    return [list[index] for list in matrix]

def get_dict_by_indexes_of_matrix(key_i: int, key_v: int, matrix: List[List[any]]) -> Dict[str, any]:
    """
    Метод генерации словаря из матрицы

    Аргументы:
    - `key_i: int` - ключ, который будет ключом в словаре
    - `key_v: int` - ключ, который будет значением в словаре
    - `matrix: List[List[any]]` - входная матрица

    Пример:

    Если key_i = 1, а key_v = 2, и на вход получаем такую матрицу:

    [['a', 'b', 'c'], [1, 2, 3], ['d', 2, 0]] -> { 'a': 'b', 1: 2, 'd': 2 }
    """
    return { i[key_i]: i[key_v] for i in matrix }

def find_list_of_matrix(from_index: int, condition: str, matrix: List[List[any]]) -> List[any]:
    """
    Метод поиска списка из матрицы

    Аргументы:
    - `from_index: int` - индекс, по которому будем сравнивать
    - `condition: int` - чему должно быть равно значение этого индекса
    - `matrix: List[List[any]]` - входная матрица

    Пример:

    Если from_index = 0, а condition = 'd', и на вход получаем такую матрицу:

    [['a', 'b', 'c'], [1, 2, 3], ['d', 2, 0]] -> ['d', 2, 0]
    """

    if from_index >= matrix[0].__len__():
        Print().print_error('find_list_of_matrix() => Индекс поиска не может быть больше или равен длине списков в матрице')

    try:
        return next(item for item in matrix if item[from_index] == condition)
    except Exception as error:
        Print().print_error(f'find_list_of_matrix() => Ничего не найдено. Ошибка при передаче {condition}')

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

    if keys.__len__() != list.__len__():
        Print().print_error('convert_list_to_dict() => длина списка ключей должна совпадать длине списка значений')
        return {}

    for v in keys:
        if isinstance(v, dict):
            Print().print_error('convert_list_to_dict() => ключом не может быть словарь')
            return {}

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

    if isinstance(string, str):
        if string.startswith('{'):
            try:
                dict = json.loads(string.replace("'", '"'))
                return dict
            except json.decoder.JSONDecodeError as error:
                Print().print_error(f'convert_str_to_dict_or_list() => {error}')

        elif string.startswith('['):
            return list(map(str, string[1:-1].replace(' ', '').split(', ')))
        elif ',' in string:
            return string.replace(' ', '').split(",")
    else:
        Print().print_error('convert_str_to_dict_or_list() => Передаваемый аргумент должен быть строкой')

    return string

def replace_custom_value(d: Dict[str, any], find_key: str, new_value: any):
    """
    Рекурсивный метод подмены значения в словаре новым значением

    Аргументы:
    - `d: Dict[str, any]` - входной словарь
    - `find_key: str` - по какому ключу будет замена
    - `new_value: any` - новое значение
    """

    for k, v in d.items():
        if isinstance(v, dict):
            replace_custom_value(v, find_key, new_value)
        elif v == find_key:
            d[k] = new_value
