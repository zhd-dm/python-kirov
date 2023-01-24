from types import FunctionType
import sqlalchemy
from sqlalchemy.orm import sessionmaker, close_all_sessions

# Local imports
from config import settings
from tables_const import TABLES
from utils import get_engine

def a():
    return

b = 'hi'

c = 1

# print(isinstance(a, FunctionType))

# print(type(a) == "function")
# print(type(b))
# print(type(c))

engine = get_engine(
    settings['user'],
    settings['password'],
    settings['host'],
    settings['port'],
    settings['db']
)

SessionLocal = sessionmaker(bind = engine)
session = SessionLocal()

def is_empty_table(table) -> bool:
    return session.query(table).count() == 0

def is_exist_table(tablename: str) -> bool:
    return sqlalchemy.inspect(engine).has_table(tablename)

try:
    for table in TABLES:
        tablename = table.__tablename__
        print(tablename, is_exist_table(tablename))

except Exception as error:
    print(error)

finally:
    session.commit()
    session.close()
    close_all_sessions()