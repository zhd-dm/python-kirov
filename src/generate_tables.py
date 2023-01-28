# При добавлении новой сущности нужно создать класс этой сущности

from typing import Dict, Union

from sqlalchemy.orm import close_all_sessions
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, Float, Text, Date, Enum
from sqlalchemy.dialects.postgresql import ENUM

# Local imports
from utils import get_engine, print_success, print_error
from env import Settings
from old_fields import CrmDealList, CatalogDocumentElementList, CatalogDocumentList, CatalogStoreproductList
from old_fields import CatalogStoreList, CatalogCatalogList, CrmProductrowList, CrmProductList

#
# ==== Обязательно ====
#

Base = declarative_base()

# =====================

class DealTable(Base):
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
        # self.__count_in_db = self.__session.query(DealTable).filter().count()
        # self.__counter = 0

        if kwarg:
            self.__set_attributes(kwarg)

    def _drop_and_create(self):
        self.__drop()
        self.__create()

    def _add_data(self, data: Dict[str, any]):
        try:
            # self.__counter += 1
            new_deal = self.__class__(self.__engine, **data)
            self.__session.add(new_deal)
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

class DocumentElement(Base):
    __tablename__ = 'document_element'
    temp_id = Column(Integer, primary_key = True)
    amount = Column(Float)
    elementId = Column(Integer)
    storeTo = Column(Integer)

# class Document(Base):
#     __tablename__ = 'document'
#     id = Column(Integer, primary_key = True)

# class StoreProduct(Base):
#     __tablename__ = 'store_product'
#     temp_id = Column(Integer, primary_key = True)
#     amount = Column(Float)
#     productId = Column(Integer)
#     quantityReserved = Column(Float)
#     storeId = Column(Integer)

# class Store(Base):
#     __tablename__ = 'store'
#     id = Column(Integer, primary_key = True)
#     title = Column(Text)

# class Catalog(Base):
#     __tablename__ = 'catalog'
#     temp_id = Column(Integer, primary_key = True)
#     name = Column(Text)

# class ProductRow(Base):
#     __tablename__ = 'productrow'
#     id = Column(Integer, primary_key = True)
#     owner_id = Column(Integer)
#     product_id = Column(Integer)
#     product_name = Column(Text)
#     quantity = Column(Float)

# class Product(Base):
#     __tablename__ = 'product'
#     id = Column(Integer, primary_key = True)
#     name = Column(Text)
#     property_119_id = Column(Integer)
#     property_119_value = Column(String)

# Base.metadata.create_all(bind = engine)

# close_all_sessions()
