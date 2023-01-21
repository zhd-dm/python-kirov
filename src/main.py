import asyncio
import time
from sqlalchemy import create_engine

# Local imports
from config import settings
from utils import get_engine, get_entities, get_data
from queries import insert_data_to_deal_table, truncate_deal_table_query

engine = get_engine(
    settings['user'],
    settings['password'],
    settings['host'],
    settings['port'],
    settings['db']
)

async def main():
    for fields in get_entities():
        field_config: dict[str, str] = fields['entity_config']
        data = await get_data(field_config)
        print('Truncate {} table'.format(field_config['entity_name']))
        truncate_deal_table_query(engine)

        # for entity in data:
        #     try:
        #         print('Insert data to {}...'.format(field_config['entity_name']))
        #         insert_data_to_deal_table(engine, entity)
        #         print('Data inserted!')

        #     except Exception as error:
        #         print(error)
    
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