from typing import Union, List, Dict

# ================== Базовые типы для конфига сущности ==================

T_ENTITY_METHOD = str
T_ENTITY_PARAMS = Dict[str, any]
T_ENTITY_DELIVERED_FIELDS = List[str]

T_ENTITY = Dict[str, Union[T_ENTITY_METHOD, T_ENTITY_PARAMS, T_ENTITY_DELIVERED_FIELDS]]