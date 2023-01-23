import asyncio
import time
from sqlalchemy.orm import sessionmaker

# Local imports
from config import settings
from utils import get_engine, get_entities, get_data
from queries import insert_data_to_tables, truncate_table_query
from models import DocumentElement, Document, Deal

engine = get_engine(
    settings['user'],
    settings['password'],
    settings['host'],
    settings['port'],
    settings['db']
)

SessionLocal = sessionmaker(bind = engine)
session = SessionLocal()

async def main():
    # Костыль для очистки таблиц поочередно
    # После добавления новой сущности - добавить очистку ниже
    truncate_table_query(session, DocumentElement)
    truncate_table_query(session, Document)
    truncate_table_query(session, Deal)

    try:
        for fields in get_entities():
            field_config: dict[str, str] = fields['entity_config']
            data = await get_data(field_config)
            
            for entity in data:
                # Костыль для сделок
                if (field_config['entity_name'] == 'deal' and entity['CLOSEDATE']) == '':
                    (entity['CLOSEDATE']) = None

                insert_data_to_tables(session, entity, field_config['entity_name'])

            time.sleep(1)

    except Exception as error:
        print(error)

    finally:
        session.commit()
        session.close()


asyncio.run(main())