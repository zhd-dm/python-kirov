from typing import Dict, List, Union

#
# ================== Базовые типы для конфига ==================
#

T_PARENT_NAME = str
T_ENTITY_NAME = str
T_CALL_METHOD = str
T_PARAMS = Dict[str, List[str]]
# DEPRECATED
T_KEYS = List[str]
T_ENUMS = Dict[str, List[any]]
T_PRIMARY_KEY = str
T_FIELDS = Dict[str, str]
T_ENTITY_CONFIG = Dict[str, Union[ T_PARENT_NAME, T_ENTITY_NAME, T_CALL_METHOD, T_PARAMS, T_KEYS, T_ENUMS, T_PRIMARY_KEY ]]
T_ENTITY_CONFIG_WITH_FIELDS = Dict[str, Union[ T_ENTITY_CONFIG, T_FIELDS ]]