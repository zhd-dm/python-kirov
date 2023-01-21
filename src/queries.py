from sqlalchemy import MetaData, Table, Column, String, Integer, Float, Text, Date, DateTime, Boolean, Enum
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import sessionmaker

from models import Deal

def insert_data_to_deal_table(engine, data: list | dict) -> None:
    SessionLocal = sessionmaker(bind = engine)
    session = SessionLocal()
    deal = Deal(
        id = data['ID'],
        title = data['TITLE'],
        stage_id = data['STAGE_ID'],
        currency_id = data['CURRENCY_ID'],
        opportunity = data['OPPORTUNITY'],
        closedate = data['CLOSEDATE'],
        closed = data['CLOSED'],
        uf_crm_1668857275565 = data['UF_CRM_1668857275565']
    )

    session.add(deal)
    session.commit()
    session.close()


def truncate_deal_table_query(engine) -> None:
    SessionLocal = sessionmaker(bind = engine)
    session = SessionLocal()
    session.query(Deal).delete()
    session.commit()
    session.close()
