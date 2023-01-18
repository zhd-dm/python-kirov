import psycopg2
from fast_bitrix24 import BitrixAsync
import asyncio
from config import host, db, username, password, webhook

bx = BitrixAsync(webhook)

entity_name = 'deal'
parent_entity = 'crm'
type_method = 'list'
column_names = ['id', 'title', 'type_id']

async def get_data():
    return await bx.get_all(
        '{}.{}.{}'.format(parent_entity, entity_name, type_method),
        params={
            'select': ['*', 'UF_*']
    })

conn = None
cursor = None

table_name = entity_name + 's'

clear_table_query = 'TRUNCATE TABLE {}'.format(table_name)
insert_data_query = 'INSERT INTO {} ({}, {}, {}) VALUES(%s, %s, %s)'.format(table_name, column_names[0], column_names[1], column_names[2])

async def main():
    try:
        conn = psycopg2.connect(
            host = host,
            dbname = db,
            user = username,
            password = password
        )

        cursor = conn.cursor()
        cursor.execute(clear_table_query)

        for entity in await get_data():
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