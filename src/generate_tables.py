# При добавлении новой сущности нужно создать класс этой сущности

from sqlalchemy.orm import close_all_sessions
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine
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

    def __init__(self, engine: Engine):
        self.__engine = engine
        self.__create()

    @property
    def tablename(self):
        return self.__tablename__

    @property
    def column_list(self):
        return [column.name for column in self.__table__.columns]

    def __create(self):
        try:
            Base.metadata.create_all(bind = self.__engine)
            print_success(f'Таблица {self.__tablename__} успешно создана')
        except Exception as error:
            print_error(error)


    # def __init__(self, engine: Engine):
    #     self.__Base = declarative_base()
    #     self.__engine = engine

    # def create(self):
    #     self.__Base.metadata.create_all(bind = self.__engine)



# class DocumentElement(Base):
#     __tablename__ = 'document_element'
#     temp_id = Column(Integer, primary_key = True)
#     amount = Column(Float)
#     elementId = Column(Integer)
#     storeTo = Column(Integer)

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
