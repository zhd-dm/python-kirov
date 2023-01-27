from typing import Dict, List, Union
import copy

from fields.base_fields import DEFAULT_CALL_METHOD, DEFAULT_PARAMS, DEFAULT_FIELDS

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

# {
#     'entity_config': {
#         'parent_name': 'crm',
#         'entity_name': 'deal',
#         'type_method': 'list',
#         'params': {
#             'select': ['*', 'UF_*']
#         },
#         'keys': [item for sublist in (ENTITY_BASE_KEYS, T_CRM_DEAL_LIST_FIELDS_KEYS) for item in sublist]
#     },
#     'fields': {
#         'id': 'int',
#         'name': 'char'
#     }
# }

class ParamsConfig:
    def __init__(self, params: Dict[str, List[str]]):
        self.__params = params

    @property
    def params(self) -> Dict[str, List[str]]:
        return self.__params

    @params.setter
    def params(self, v: Dict[str, List[str]]):
        self.__params = v

class FieldsConfig:
    def __init__(self, fields: Dict[str, str]):
        self.__fields = fields

    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, v: Dict[str, str]):
        self.__fields = v

class EntityConfig:
    def __init__(self, entity_config: Dict[str, Union[str, ParamsConfig, List[str]]]):
        self.__entity_config = entity_config

    @property
    def entity_config(self) -> Dict[str, Union[str, ParamsConfig, List[str]]]:
        return self.__entity_config

    @property
    def parent_name(self) -> str:
        return self.__entity_config.get('parent_name', DEFAULT_CALL_METHOD[0])

    @property
    def entity_name(self) -> str:
        return self.__entity_config.get('entity_name', DEFAULT_CALL_METHOD[1])

    @property
    def type_method(self) -> str:
        return self.__entity_config.get('type_method', DEFAULT_CALL_METHOD[2])

    @property
    def params(self) -> ParamsConfig:
        return ParamsConfig(self.entity_config.get('params', DEFAULT_PARAMS))

    @property
    def fields(self) -> FieldsConfig:
        return FieldsConfig(self.entity_config.get('fields', DEFAULT_FIELDS))

class Config:
    def __init__(self, config: Dict[str, Union[EntityConfig, FieldsConfig]]):
        self.__entity_config = config
        self.__generate_dict_config()

    def __generate_dict_config(self):
        self.__entity_config = EntityConfig(self.__entity_config)
        self.__parent_name = self.__entity_config.parent_name
        self.__entity_name = self.__entity_config.entity_name
        self.__type_method = self.__entity_config.type_method
        self.__params = ParamsConfig(self.__entity_config.params)
        self.__fields = FieldsConfig(self.__entity_config.fields)

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
    def params(self, v: ParamsConfig):
        self.__params = v

    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, v: FieldsConfig):
        self.__fields = v
