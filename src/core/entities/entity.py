from core.entities.config.types import T_ENTITY, T_ENTITY_METHOD, T_ENTITY_PARAMS, T_ENTITY_DELIVERED_FIELDS
from core.entities.config.utils import _invalid_conf


class Entity:
    """
    Класс для типизации конфига сущности.

    Параметры:
    `entity: T_ENTITY` -> Конфиг сущности
    """
    
    def __init__(self, entity: T_ENTITY):
        if not _invalid_conf(entity):
            self.__entity_conf = entity

    @property
    def method(self) -> T_ENTITY_METHOD:
        return self.__entity_conf.get('method')
    
    @property
    def params(self) -> T_ENTITY_PARAMS:
        return self.__entity_conf.get('params')

    @property
    def delivered_fields(self) -> T_ENTITY_DELIVERED_FIELDS:
        return self.__entity_conf.get('delivered_fields')
