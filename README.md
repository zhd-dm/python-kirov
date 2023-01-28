# __Module fields__

## `class BaseConfig(config: T_ENTITY_CONFIG_WITH_FIELDS)`

### __Types:__
- `T_PARAMS = Dict[str, List[str]]`
- `T_KEYS = List[str]`
- `T_FIELDS = Dict[str, str]`
- `T_CALL_METHOD = str`
- `T_ENTITY_CONFIG = Dict[str, Union[ T_CALL_METHOD, T_PARAMS, T_KEYS ]]`
- `T_ENTITY_CONFIG_WITH_FIELDS = Dict[str, Union[ T_ENTITY_CONFIG, T_FIELDS ]]`

__getters:__ 
- `entity_config -> T_ENTITY_CONFIG`
- `parent_name -> str`
- `entity_name -> str`
- `type_method -> str`
- `params -> T_PARAMS`
- `keys -> T_KEYS`
- `fields -> T_FIELDS`

__setters:__
- `params.setter: self.__params = v`
- `fields.setter: self.__fields = v`

## __Constants:__
- `ENTITY_BASE_KEYS: T_KEYS`
- `BASE_FIELDS_TO_DB_TYPES: Dict[str, str]`
- `DEFAULT_PARAMS: T_PARAMS`
- `DEFAULT_KEYS: T_KEYS`
- `DEFAULT_FIELDS: T_FIELDS`
- `DEFAULT_CALL_METHOD: List[T_CALL_METHOD]`
- `DEFAULT_ENTITY_CONFIG: T_ENTITY_CONFIG`

<br>

# __Module tables__

## `class BaseTable(engine: Engine, **kwarg)`

__getters:__ 
- `tablename -> str`
- `column_list -> List[str]`

__methods:__
- `_drop_and_create(): __drop(), __create()`
- `_add_data(data: Dict[str, any]): .. __session.add(data), ..`

<br>

# __Module utils__

### __Types:__
- `T_SETTINGS = Dict[str, Union[str, int]]`

## `class Utils()`

__getters:__ 
- `db_url -> str: Settings().db_url`
- `engine -> Engine`

__methods:__
- `async get_data(config: BaseConfig) -> Union[List, Dict]`
- `print_success(message: str): print(""" """) `
- `print_error(error: Exception): print(""" """) `

## `class Settings(settings: T_SETTINGS = DEFAULT_settings)`

__getters:__ 
- `db_url -> str`


<hr>

### __Run tests__ -> `$ python -m unittest || python -m unittest models.user.test_user_model.TestUserModel`

<hr>

## *__Used libraries:__*

1. `BitrixAsync`
2. `psycopg2`
3. `sqlalchemy`

