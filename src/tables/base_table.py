from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine
from sqlalchemy import Table, Column, Integer, String, Float, Text, Date, Enum

from fields.base_entity_config import BaseConfig

class BaseTable:
    def __init__(self, engine: Engine):
        self.__Base = declarative_base()
        self.__engine = engine
        self.table_args = {'extend_existing': True}

    def create_table(self, table_class: any):
        table_class.__table__ = Table(
            table_class.__tablename__,
            self.__Base.metadata,
            *table_class.__table_args__,
            extend_existing = self.table_args['extend_existing']
        )

    def create_all(self):
        self.__Base.metadata.create_all(bind = self.__engine)

class Catalog():
    __tablename__ = 'catalog'
    temp_id = Column(Integer, primary_key = True)
    name = Column(Text)

# class BaseTable:
#     def __init__(self, engine: Engine, config: BaseConfig):
#         self.__Base = declarative_base()
#         self.__engine = engine

#         self.__tablename__ = config.entity_name
#         self.temp_id = Column(Integer, primary_key = True)
#         self.name = Column(Text)

#         self.__table_args__ = { 'extend_existing': True }
#         self._create_all()

    # def __generate_columns(self):
    #     self.temp_id = Column(Integer, primary_key = True)
    #     self.name = Column(Text)

#     def _create_all(self):
#         self.__Base.metadata.create_all(bind = self.__engine)

#     @property
#     def tablename(self):
#         return self.__tablename__
