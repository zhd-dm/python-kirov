from types import FunctionType
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import close_all_sessions

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

try:
    for table in TABLES:
        print(table.__tablename__, session.query(table).count())

except Exception as error:
    print(error)

finally:
    session.commit()
    session.close()
    close_all_sessions()