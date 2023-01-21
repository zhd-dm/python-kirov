import asyncio
from utils import connect_db, get_entities, get_data
from config import host, db, username, password

conn = None
cursor = None

async def main():
    try:
        conn = connect_db(host, db, username, password)
        print('=== DB Connected ===')
        cursor = conn.cursor()

        # cursor.execute(create_table_query(table_name))
        # cursor.execute(get_clear_table_query(table_name))

        for entity in get_entities():
            data = await get_data(entity['entity_config'])

    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.commit()
            conn.close()
        if cursor is not None:
            cursor.close()
        
        print('=== DB Disconnected ===')

asyncio.run(main())