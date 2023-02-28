# __Module fields__

## <b> Core: </b>
- ### <b> Modules: </b> 
    - `DBConnector`
    - `BxCall`
    - `BaseEntity`
    - `PGTable`
    - `BaseTable`
    - `BaseColumns`
    - `DataImporter`
    - `EntitiesGenerator`

<hr>

## ... Need update ...

## `class BaseConfig(config: T_ENTITY_CONFIG_WITH_FIELDS)`

### __Types:__
- `T_PARENT_NAME = str`
- `T_ENTITY_NAME = str`
- `T_CALL_METHOD = str`
- `T_PARAMS = Dict[str, List[str]]`
- `T_KEYS = List[str]`
- `T_ENUMS = Dict[str, List[any]]`
- `T_PRIMARY_KEY = str`
- `T_FIELDS = Dict[str, str]`
- `T_ENTITY_CONFIG = Dict[str, Union[ T_PARENT_NAME, T_ENTITY_NAME, T_CALL_METHOD, T_PARAMS, T_KEYS, T_ENUMS, T_PRIMARY_KEY ]]`
- `T_ENTITY_CONFIG_WITH_FIELDS = Dict[str, Union[ T_ENTITY_CONFIG, T_FIELDS ]]`

__getters:__ 
- `entity_config -> T_ENTITY_CONFIG`
- `parent_name -> str`
- `entity_name -> str`
- `type_method -> str`
- `params -> T_PARAMS`
- `keys -> T_KEYS`
- `enums -> T_ENUMS`
- `primary_key_field -> T_PRIMARY_KEY`
- `fields -> T_FIELDS`

__setters:__
- `params.setter: self.__params = v`
- `keys.setter: self.__keys.append(v)`
- `fields.setter: self.__fields = v`

## __Constants:__
- `ENTITY_BASE_KEYS: T_KEYS`
- `BASE_FIELDS_TO_DB_TYPES: Dict[str, str]`
- `DEFAULT_PARAMS: T_PARAMS`
- `DEFAULT_KEYS: T_KEYS`
- `DEFAULT_ENUMS: T_ENUMS`
- `DEFAULT_FIELDS: T_FIELDS`
- `DEFAULT_CALL_METHOD: List[T_CALL_METHOD]`
- `DEFAULT_PRIMARY_KEY: T_PRIMARY_KEY`
- `DEFAULT_ENTITY_CONFIG: T_ENTITY_CONFIG`
- `DEFAULT_ENTITY_CONFIG_WITH_FIELDS: T_ENTITY_CONFIG_WITH_FIELDS`

<br>

# __Module tables__

## `class BaseTable(engine: Engine, entity_config: BaseConfig)`

__getters:__ 
- `tablename -> str`

__methods:__
- `_drop_and_create(): __drop(), __create()`
- `_add_data(data: Dict[str, any]): .. __connection.execute(**element), ..`

## `class BaseColumns()`

__getters:__ 
- `column_list -> List[Column]`

<br>

# __Module utils__

### __Types:__
- `T_SETTINGS = Dict[str, Union[str, int]]`

## `class Utils()`

__getters:__ 
- `db_url -> str: Settings().db_url`
- `engine -> Engine`

__methods:__
- `key_dict_to_lower(dict: Dict[str, any]) -> Dict[str, any]`
- `props_list_to_lower(list: List[str]) -> List[str]`
- `print_success(message: str): print(""" """) `
- `print_error(error: Exception): print(""" """) `

## `class Settings(settings: T_SETTINGS = DEFAULT_settings)`

__getters:__ 
- `db_url -> str`

## ... Need update ...

<hr>

### __Run Core tests__ 
#### `pg.utils => $ python -m unittest core.pg.tests.test_utils_methods.TestPGUtils`
#### `pg.entities => $ python -m unittest core.entities.tests.test_utils_methods.TestEntitiesUtils`

<hr>

## *__Install core libraries:__*

1. `pip install fast_bitrix24==1.5.14`
2. `pip install psycopg2==2.9.5`
3. `pip install SQLAlchemy==1.4.46`
4. `pip install SQLAlchemy-Utils==0.39.0`
5. `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
6. `pip install termcolor==2.2.0`

## *__Install feature libraries:__*

1. `pip install xmltodict==0.13.0`