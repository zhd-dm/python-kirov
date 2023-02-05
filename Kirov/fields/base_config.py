from utils import key_dict_to_lower, props_list_to_lower, print_error
from fields.types import T_ENTITY_CONFIG_WITH_FIELDS, T_ENTITY_CONFIG, T_PARENT_NAME, T_ENTITY_NAME, T_CALL_METHOD, T_PARAMS, T_KEYS, T_ENUMS, T_PRIMARY_KEY, T_FIELDS


class BaseConfig:

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
    def params(self):
        return self.__params

    @params.setter
    def params(self, v: T_PARAMS):
        if isinstance(v, dict):
            self.__params = v
        else:
            print_error('params должен быть словарем')

    # DEPRECATED
    @property
    def keys(self):
        return self.__keys
    
    # DEPRECATED
    @property
    def keys_lower(self):
        return props_list_to_lower(self.__keys)

    # DEPRECATED
    @keys.setter
    def keys(self, v: str):
        if isinstance(v, str):
            self.__keys.append(v)
        else:
            print_error('Элемент списка keys должен быть строкой')
        if v == '':
            print_error('Элемент списка keys не должен быть пустой строкой')

    @property
    def enums(self):
        return self.__enums

    @property
    def enums_lower(self):
        return key_dict_to_lower(self.__enums)

    @property
    def primary_key_field(self):
        return self.__primary_key_field

    @property
    def primary_key_field_lower(self):
        return self.__primary_key_field.lower()

    @property
    def fields(self):
        return self.__fields

    # DEPRECATED
    @fields.setter
    def fields(self, v: T_FIELDS):
        if isinstance(v, T_FIELDS):
            self.__fields = v
        else:
            print_error('Поле должно соответствовать типу T_FIELDS')

    @property
    def fields_lower(self):
        return key_dict_to_lower(self.__fields)

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
        self.__type_method: T_CALL_METHOD = self.__entity_config.get('type_method')
        self.__params: T_PARAMS = self.__entity_config.get('params')
        # DEPRECATED
        self.__keys: T_KEYS = self.__entity_config.get('keys')
        self.__enums: T_ENUMS = self.__entity_config.get('enums')
        self.__primary_key_field: T_PRIMARY_KEY = self.__entity_config.get('primary_key')
        self.__fields: T_FIELDS = self.__config.get('fields')
