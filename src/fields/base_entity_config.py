from fields.base_fields import DEFAULT_ENTITY_CONFIG, DEFAULT_CALL_METHOD, DEFAULT_PARAMS, DEFAULT_KEYS, DEFAULT_FIELDS
from fields.base_types import T_ENTITY_CONFIG_WITH_FIELDS, T_ENTITY_CONFIG, T_CALL_METHOD, T_PARAMS, T_KEYS, T_FIELDS

# @deprecated
class OldFieldParams():
    def __init__(
        self,
        param_obj: dict
    ):
        self.param_obj = param_obj

# @deprecated
class OldEntityConfig():
    def __init__(
        self,
        parent_name: str,
        entity_name: str,
        type_method: str,
        params: OldFieldParams,
        columns: dict
    ):
        self.parent_name = parent_name
        self.entity_name = entity_name
        self.type_method = type_method
        self.params = params
        self.columns = columns

class Config:
    def __init__(self, config: T_ENTITY_CONFIG_WITH_FIELDS):
        self.__config: T_ENTITY_CONFIG_WITH_FIELDS = config
        self.__entity_config: T_ENTITY_CONFIG = self.__config.get('entity_config', None)
        self.__check_error()

    @property
    def config(self):
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
        self.__params = v

    @property
    def keys(self):
        return self.__keys

    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, v: T_FIELDS):
        self.__fields = v


    def __check_error(self):
        if self.__entity_config is None:
            self.__is_none_value('entity_config')
        else:
            self.__generate_dict_config()

    def __generate_dict_config(self):
        self.__parent_name: str = self.__entity_config.get('parent_name', None)
        if self.__parent_name is None:
            self.__is_none_value('parent_name')
        
        self.__entity_name: str = self.__entity_config.get('entity_name', None)
        if self.__entity_name is None:
            self.__is_none_value('entity_name')

        self.__type_method: str = self.__entity_config.get('type_method', None)
        if self.__entity_name is None:
            self.__is_none_value('type_method')

        self.__params: T_PARAMS = self.__entity_config.get('params', None)
        if self.__entity_name is None:
            self.__is_none_value('params')

        self.__keys: T_KEYS = self.__entity_config.get('keys', None)
        if self.__entity_name is None:
            self.__is_none_value('keys')

        self.__fields: T_FIELDS = self.__config.get('fields', None)
        if self.__entity_name is None:
            self.__is_none_value('fields')

    def __is_none_value(self, str: str) -> str:
        print('Not found value in field ' + str)

        if str == 'entity_config':
            return DEFAULT_ENTITY_CONFIG
        if str == 'parent_name':
            return DEFAULT_CALL_METHOD[0]
        if str == 'entity_name':
            return DEFAULT_CALL_METHOD[1]
        if str == 'type_method':
            return DEFAULT_CALL_METHOD[2]
        if str == 'params':
            return DEFAULT_PARAMS
        if str == 'keys':
            return DEFAULT_KEYS
        if str == 'fields':
            return DEFAULT_FIELDS
