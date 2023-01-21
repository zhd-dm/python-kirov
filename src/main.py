import asyncio
import time
from sqlalchemy import create_engine,  MetaData, Table, Column, Integer, Text, Float, Date, String, Enum
from sqlalchemy.dialects.postgresql import ENUM

# Local imports
from config import settings
from utils import get_engine, connect_db, get_entities, get_data
from queries import create_all_tables_query

conn = None
cursor = None

engine = get_engine(
    settings['user'],
    settings['password'],
    settings['host'],
    settings['port'],
    settings['db']
)

connection = engine.connect()
metadata = MetaData()

async def main():
    create_all_tables_query(metadata)

    metadata.create_all(engine)

    # for entity in get_entities():
    #     data = await get_data(entity['entity_config'])
    #     time.sleep(1)
    #     print(data)
    

    # try:
        # for entity in get_entities():
        #     entity_config: dict[str, str] = entity['entity_config']
        #     # data = await get_data(entity_config)
        #     table_name = entity_config['entity_name']
        #     entity.pop('entity_config')
        #     table = create_table_query(metadata, table_name, entity)
        #     metadata.create_all()

    # except Exception as error:
    #     print(error)

asyncio.run(main())