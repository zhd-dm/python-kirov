from sqlalchemy import Column, String, Integer
from tests import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    username = Column(String)
    email = Column(String)