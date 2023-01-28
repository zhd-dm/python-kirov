from typing import Dict

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float, Text, Date
from sqlalchemy.dialects.postgresql import ENUM

# Local imports
from utils.utils import print_error, print_success

#
# ==== Обязательно ====
#

Base = declarative_base()

# =====================

class BaseTable(Base):
    __tablename__ = 'deal'
    __uf_crm_1668857275565_enum = ENUM('211', '209', name='uf_crm_1668857275565_enum')

    id = Column(Integer, primary_key = True)
    title = Column(Text)
    stage_id = Column(Text)
    currency_id = Column(Text)
    opportunity = Column(Float)
    closedate = Column(Date)
    closed = Column(String)
    uf_crm_1668857275565 = Column(__uf_crm_1668857275565_enum)

    @property
    def tablename(self):
        return self.__tablename__

    @property
    def column_list(self):
        return [column.name for column in self.__table__.columns]

    def __init__(self, engine: Engine, **kwarg):
        self.__engine = engine
        self.__Session = sessionmaker(bind = engine)
        self.__session = self.__Session()

        # self.__data_count = d_len
        # self.__count_in_db = self.__session.query(BaseTable).filter().count()
        # self.__counter = 0

        if kwarg:
            self.__set_attributes(kwarg)

    def _drop_and_create(self):
        self.__drop()
        self.__create()

    def _add_data(self, data: Dict[str, any]):
        try:
            # self.__counter += 1
            new_rec = self.__class__(self.__engine, **data)
            self.__session.add(new_rec)
            self.__session.commit()
            print_success(f'Запись успешно добавлена в таблицу {self.__tablename__}')

            # if self.__counter is not self.__data_count:
            #     print_error('Не все записи добавлены в таблицу')
            
        except Exception as error:
            print_error(error)
            self.__session.rollback()
        finally:
            self.__session.close()

    def __create(self):
        try:
            Base.metadata.create_all(bind = self.__engine)
            print_success(f'Таблица {self.__tablename__} успешно создана')
        except Exception as error:
            print_error(error)

    def __drop(self):
        Base.metadata.drop_all(bind = self.__engine)

    def __set_attributes(self, data: Dict[str, any]):
        data = { key.lower(): value for key, value in data.items() }
        self.__empty_str_to_none(data)
        for key, value in data.items():
            setattr(self, key, value)

    def __empty_str_to_none(self, data: Dict[str, any]):
        #
        # Для сделок
        if (data['closedate'] == ''):
            (data['closedate']) = None