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
        print(is_exist_db(get_db_url()))

except Exception as error:
    print(error)

finally:
    session.commit()
    session.close()
    close_all_sessions()