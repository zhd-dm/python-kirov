from utils.mapping import replace_custom_value

from core.data_handlers.config.types import T_ENTITY_CONFIG_WITH_FIELDS


class EntityConfig:

    @property
    def entity_name(self):
        return self.__entity_config.get('entity_name')

    @property
    def params(self):
        return self.__entity_config.get('params')

    @property
    def enums(self):
        return self.__entity_config.get('enums')

    @property
    def primary_key(self):
        return self.__entity_config.get('primary_key')

    @property
    def field_to_py_type(self):
        return self.__field_to_py_type

    def __init__(self, en_conf_with_fields: T_ENTITY_CONFIG_WITH_FIELDS):
        self.__en_conf = en_conf_with_fields
        self.__entity_config = self.__en_conf.get('entity_config')
        self.__field_to_py_type = self.__en_conf.get('field_to_py_type')

    def _replace_custom_params(self, custom_value: any):
        replace_custom_value(self.params, 'custom', custom_value)
