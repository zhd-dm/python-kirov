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
        self._config = config
        self.__entity_config: Dict[str, any] = self.config['entity_config']
        self.generate_fields()

    def generate_fields(self):
        self._parent_name = self.__entity_config['parent_name']
        self._entity_name = self.__entity_config['entity_name']
        self._type_method = self.__entity_config['type_method']
        self._params = self.__entity_config['params']
        self._fields = copy.deepcopy(self._config)
        del self.fields['entity_config']

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, v):
        self._config = v

    @property
    def parent_name(self):
        return self._parent_name

    @parent_name.setter
    def parent_name(self, v):
        self._parent_name = v

    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, v):
        self._entity_name = v

    @property
    def type_method(self):
        return self._type_method
    
    @type_method.setter
    def type_method(self, v):
        self._type_method = v

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, v):
        self._params = v

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, v):
        self._fields = v
