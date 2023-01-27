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
    def __init__(self, config: Dict[str, any]):
        self.config = config
        self.generate_fields()

    def generate_fields(self):
        self.entity_config = self.config['entity_config']
        self.parent_name = self.entity_config['parent_name']
        self.entity_name = self.entity_config['entity_name']
        self.type_method = self.entity_config['type_method']
        self.params = self.entity_config['params']
        self.fields = copy.deepcopy(self.config)
        del self.fields['entity_config']

    def get_config(self):
        return self.config

    def get_parent_name(self):
        return self.parent_name

    def get_entity_name(self):
        return self.entity_name

    def get_type_method(self):
        return self.type_method
    
    def get_params(self):
        return self.params

    def get_fields(self):
        return self.fields
