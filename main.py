import asyncio
from utils import connect_db, get_data, get_columns, get_list_columns, get_clear_table_query, insert_data_query
from config import host, db, username, password

entity_name = 'deal'
parent_name = 'crm'
type_method = 'list'

columns = get_columns(parent_name, entity_name)

conn = None
cursor = None

table_name = entity_name + 's'

async def main():
    try:
        conn = connect_db(host, db, username, password)
        cursor = conn.cursor()
        cursor.execute(get_clear_table_query(table_name))                

        for entity in await get_data(parent_name, entity_name, type_method):
            cursor.execute(insert_data_query(table_name, columns), (get_list_columns(entity, columns)))

    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.commit()
            conn.close()
        if cursor is not None:
            cursor.close()

asyncio.run(main())