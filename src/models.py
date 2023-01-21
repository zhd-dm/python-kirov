from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Float, Text, Date, Enum
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import sessionmaker

# Local imports
from utils import get_engine
from config import settings

engine = get_engine(
    settings['user'],
    settings['password'],
    settings['host'],
    settings['port'],
    settings['db']
)

SessionLocal = sessionmaker()
Base = declarative_base()

class Deal(Base):
    uf_crm_1668857275565_enum = ENUM('211', '209', name='uf_crm_1668857275565_enum')
    __tablename__ = 'deal'
    id = Column(Integer, primary_key = True)
    title = Column(Text)
    stage_id = Column(Text)
    currency_id = Column(Text)
    opportunity = Column(Float)
    closedate = Column(Date)
    closed = Column(String)
    uf_crm_1668857275565 = Column(uf_crm_1668857275565_enum)

Base.metadata.create_all(bind = engine)
