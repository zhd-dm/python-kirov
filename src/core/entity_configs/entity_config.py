from utils.mapping import key_dict_to_lower, props_list_to_lower, print_error, replace_custom_value, key_and_value_dict_to_lower

from core.data_handlers.config.types import T_ENTITY_CONFIG_WITH_FIELDS, T_ENTITY_CONFIG, T_PARENT_NAME, T_ENTITY_NAME, T_TYPE_METHOD, T_FULL_METHOD, T_PARAMS, T_KEYS, T_ENUMS, T_PRIMARY_KEY, T_FIELDS


class EntityConfig:
    """
    Класс - обертка над EntityConfigWithFields для типизации и доступа к полям

    Параметры:
    - `config: T_ENTITY_CONFIG_WITH_FIELDS`

    Геттеры:
    - `entity_config -> T_ENTITY_CONFIG` - словарь конфига сущности с полями и их типами
    - `parent_name -> T_PARENT_NAME` - имя родительской сущности вызываемого метода
    - `entity_name -> T_ENTITY_NAME` - имя сущности вызываемого метода
    - `type_method -> T_TYPE_METHOD` - тип вызываемого метода
    - `full_method -> T_FULL_METHOD` - полное наименование вызываемого метода
    - `params -> T_PARAMS` - словарь который передается в запрос в качестве объекта params
    - `keys -> T_KEYS` - список ключей словаря entity_config
    - `keys_lower -> T_KEYS` - список ключей словаря entity_config в нижнем регистре
    - `enums_lower -> T_ENUMS` - список словарей енумов (если они есть)
    - `primary_key_lower -> T_PRIMARY_KEY` - имя поля, которое будет PK в БД
    - `fields -> T_FIELDS` - словарь полей сущности
    - `field_keys_lower -> T_FIELDS` - словарь ключей полей сущности в нижнем регистре
    - `field_keys_and_values_lower -> T_FIELDS` - словарь ключей и значений полей сущности в нижнем регистре

    Сеттеры:
    - `params(v: T_PARAMS)` - изменяет объект params перед отправкой запроса
    - `keys(v: str)` - добавляет ключ в список ключей
    """

    def __init__(self, config: T_ENTITY_CONFIG_WITH_FIELDS):
        self.__config: T_ENTITY_CONFIG_WITH_FIELDS = config
        self.__entity_config: T_ENTITY_CONFIG = self.__config.get('entity_config', None)
        
        # Вызвать по-другому, например if self.__is_valid_config(): self.__generate_dict_config()
        self.__check_error()

    @property
    def entity_config(self):
        return self.__entity_config

    @property
    def parent_name(self):
        return self.__parent_name

    @property
    def entity_name(self):
        return self.__entity_name

    @property
    def type_method(self):
        return self.__type_method

    @property
    def full_method(self) -> T_FULL_METHOD:
        return f'{self.parent_name}.{self.entity_name}.{self.type_method}'

    @property
    def params(self):
        return self.__params

    @params.setter
    def params(self, v: T_PARAMS):
        if isinstance(v, dict):
            self.__params = v
        else:
            print_error('params должен быть словарем')

    @property
    def keys(self):
        return self.__keys
    
    @property
    def keys_lower(self):
        return props_list_to_lower(self.__keys)

    @keys.setter
    def keys(self, v: str):
        if isinstance(v, str):
            self.__keys.append(v)
        else:
            print_error('Элемент списка keys должен быть строкой')
        if v == '':
            print_error('Элемент списка keys не должен быть пустой строкой')

    @property
    def enums_lower(self):
        return key_dict_to_lower(self.__enums)

    @property
    def primary_key_lower(self):
        return self.__primary_key.lower()

    @property
    def fields(self):
        return self.__fields

    @property
    def field_keys_lower(self):
        return key_dict_to_lower(self.__fields)

    @property
    def field_keys_and_values_lower(self):
        return key_and_value_dict_to_lower(self.__fields)

    def _replace_custom_params(self, custom_value: any):
        replace_custom_value(self.__params, 'custom', custom_value)

    def __check_error(self):
        if self.__entity_config is None:
            print_error('Ошибка! Пустой entity_config')
        else:
            self.__generate_dict_config()

    def __generate_dict_config(self):
        # DEPRECATED
        self.__parent_name: T_PARENT_NAME = self.__entity_config.get('parent_name')
        # DEPRECATED
        self.__entity_name: T_ENTITY_NAME = self.__entity_config.get('entity_name')
        # DEPRECATED
        self.__type_method: T_TYPE_METHOD = self.__entity_config.get('type_method')
        self.__params: T_PARAMS = self.__entity_config.get('params')
        self.__keys: T_KEYS = self.__entity_config.get('keys')
        self.__enums: T_ENUMS = self.__entity_config.get('enums')
        self.__primary_key: T_PRIMARY_KEY = self.__entity_config.get('primary_key')
        self.__fields: T_FIELDS = self.__config.get('fields')

class EntityConfig2:

    def entity_name(self):
        self.__entity_config.get('entity_name')

    def params(self):
        self.__entity_config.get('params')

    def enums(self):
        self.__entity_config.get('enums')

    def primary_key(self):
        self.__entity_config.get('primary_key')

    def field_to_py_type(self):
        return self.__field_to_py_type

    def __init__(self, en_conf: T_ENTITY_CONFIG_WITH_FIELDS):
        self.__en_conf = en_conf
        self.__entity_config = self.__en_conf.get('entity_config')
        self.__field_to_py_type = self.__en_conf.get('field_to_py_type')
