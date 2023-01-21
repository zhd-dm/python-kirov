from sqlalchemy import MetaData, Table, Column, String, Integer, Float, Text, Date, DateTime, Boolean, Enum
from sqlalchemy.dialects.postgresql import ENUM

def create_all_tables_query(metadata: MetaData) -> None:
    create_deal_table_query(metadata)

def create_deal_table_query(metadata: MetaData) -> None:
    uf_crm_1668857275565_enum = ENUM('211', '209', name='uf_crm_1668857275565_enum')
    Table(
        'deal',
        metadata,
        Column('id', Integer),
        Column('title', Text),
        Column('stage_id', Text),
        Column('currency_id', Text),
        Column('opportunity', Float),
        Column('closedate', Date),
        Column('closed', String),
        Column('uf_crm_1668857275565', uf_crm_1668857275565_enum)
    )


def get_clear_table_query(table_name: str) -> str:
    return 'TRUNCATE TABLE {}'.format(table_name)

def insert_data_query(table_name: str, id: str, title: str, type_id: str, stage_id: str, probability: str, currency_id: str, opportunity: str, is_manual_opportunity: str) -> str:
    return """
        INSERT INTO {0} ({1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    """.format(table_name, id, title, type_id, stage_id, probability, currency_id, opportunity, is_manual_opportunity)