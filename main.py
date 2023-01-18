import asyncio
from utils import connect_db, get_data, get_columns
from config import host, db, username, password

entity_name = 'deal'
parent_name = 'crm'
type_method = 'list'

columns = get_columns(parent_name, entity_name)

conn = None
cursor = None

table_name = entity_name + 's'

clear_table_query = 'TRUNCATE TABLE {}'.format(table_name)
insert_data_query = 'INSERT INTO {} ({}, {}, {}) VALUES(%s, %s, %s)'.format(table_name, columns[0], columns[1], columns[2])

async def main():
    try:
        conn = connect_db(host, db, username, password)
        cursor = conn.cursor()
        cursor.execute(clear_table_query)

        for entity in await get_data(parent_name, entity_name, type_method):
            cursor.execute(insert_data_query, (entity['ID'], entity['TITLE'], entity['STAGE_ID']))

    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.commit()
            conn.close()
        if cursor is not None:
            cursor.close()

asyncio.run(main())