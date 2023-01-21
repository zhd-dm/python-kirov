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
        print('Очистка таблицы {}'.format(field_config['entity_name']))
        truncate_deal_table_query(engine)

        try:
            for entity in data:
                print('ID вносимой записи - {}'.format(entity['ID']))
                if (entity['CLOSEDATE']) == '':
                    (entity['CLOSEDATE']) = None
                
                insert_data_to_deal_table(engine, entity)

            print('Записи в количестве {} успешно внесены!'.format(data.__len__()))

        except Exception as error:
            print(error)


asyncio.run(main())