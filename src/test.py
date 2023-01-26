from types import FunctionType
from typing import Dict
import sqlalchemy
from sqlalchemy_utils import database_exists
from sqlalchemy.orm import sessionmaker, close_all_sessions

# Local imports
from tables_const import TABLES
from utils import get_engine, get_db_url, is_exist_db
from fields.base_fields import ENTITY_BASE_KEYS
from fields.catalog_storeproduct_list_fields import T_CATALOG_STOREPRODUCT_LIST_FIELDS_VALUES
from fields.catalog_store_list import T_CATALOG_STORE_LIST_FIELDS_VALUES


def a():
    return

b = 'hi'

c = 1

# print(isinstance(a, FunctionType))

# print(type(a) == "function")
# print(type(b))
# print(type(c))

# engine = get_engine()

# SessionLocal = sessionmaker(bind = engine)
# session = SessionLocal()

print(T_CATALOG_STOREPRODUCT_LIST_FIELDS_VALUES)

try:
    # my_dict = {keys[i]: values[i] for i in range(len(keys))}
    # print(my_dict)
    print()
    

except Exception as error:
    print(error)

finally:
    # session.commit()
    # session.close()
    close_all_sessions()