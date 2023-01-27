from typing import Dict
import copy

class OldFieldParams():
    def __init__(
        self,
        param_obj: dict
    ):
        self.param_obj = param_obj

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

class EntityConfig:
    # protected _config
    # private __entity_config

    def __init__(self, config: Dict[str, any]):
        self.__config = config
        self.__entity_config: Dict[str, any] = self.__config['entity_config']
        self.generate_fields()

    def generate_fields(self):
        self.__parent_name = self.__entity_config['parent_name']
        self.__entity_name = self.__entity_config['entity_name']
        self.__type_method = self.__entity_config['type_method']
        self.__params = self.__entity_config['params']
        self.__fields = copy.deepcopy(self.__config)
        del self.__fields['entity_config']

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, v):
        self.__config = v

    @property
    def parent_name(self):
        return self.__parent_name

    @parent_name.setter
    def parent_name(self, v):
        self.__parent_name = v

    @property
    def entity_name(self):
        return self.__entity_name

    @entity_name.setter
    def entity_name(self, v):
        self.__entity_name = v

    @property
    def type_method(self):
        return self.__type_method
    
    @type_method.setter
    def type_method(self, v):
        self.__type_method = v

    @property
    def params(self):
        return self.__params

    @params.setter
    def params(self, v):
        self.__params = v

    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, v):
        self.__fields = v
