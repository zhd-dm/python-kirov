from types import FunctionType
import sqlalchemy
from sqlalchemy_utils import database_exists
from sqlalchemy.orm import sessionmaker, close_all_sessions

# Local imports
from tables_const import TABLES
from utils import get_engine, get_db_url, is_exist_db

def a():
    return

b = 'hi'

c = 1

# print(isinstance(a, FunctionType))

# print(type(a) == "function")
# print(type(b))
# print(type(c))

engine = get_engine()

SessionLocal = sessionmaker(bind = engine)
session = SessionLocal()

class FieldParams():
    def __init__(
        self,
        param_obj: dict
    ):
        self.param_obj = param_obj

class EntityConfig():
    def __init__(
        self, parent_name: str,
        entity_name: str,
        type_method: str,
        params: FieldParams,
        columns: dict
    ):
        self.parent_name = parent_name
        self.entity_name = entity_name
        self.type_method = type_method
        self.params = params
        self.columns = columns

def is_empty_table(table) -> bool:
    return session.query(table).count() == 0

def is_exist_table(tablename: str) -> bool:
    return sqlalchemy.inspect(engine).has_table(tablename)

def in_full_record_table(table, number_of_records: int) -> bool:
    return session.query(table).count() == number_of_records

def records_in_table(table) -> int:
    return session.query(table).count()

try:
    for table in TABLES:
        tablename = table.__tablename__
        # print(is_exist_table(tablename), tablename)
        # print(is_empty_table(table), tablename)
        # print(in_full_record_table(table, 113))
        # print(records_in_table(table))
        # print(is_exist_db(get_db_url()))

    deal = EntityConfig(
        'crm',
        'deal',
        'list',
        { 'select': ['*', 'UF_*'] },
        {
            'ID': 'int',
            'TITLE': 'text',
            'STAGE_ID': 'text',
            'CURRENCY_ID': 'text',
            'OPPORTUNITY': 'double',
            'CLOSEDATE': 'date',
            'CLOSED': 'char',
            'UF_CRM_1668857275565': 'enum'
        }
    )

    print(deal.type_method)
    print(deal.params)
    print(deal.columns)
    

except Exception as error:
    print(error)

finally:
    session.commit()
    session.close()
    close_all_sessions()