import asyncio
import time
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import close_all_sessions

# Local imports
from config import settings
from tables_const import TABLES
from utils import get_engine, get_data, get_entity_config, get_entity_name
from queries import truncate_table_query, data_insert_loop

from fields import crm_deal_list, catalog_document_element_list, catalog_document_list, catalog_storeproduct_list
from fields import catalog_store_list, catalog_catalog_list, crm_productrow_fields, crm_product_list

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
    # После добавления новой сущности - добавить в массив эту сущность
    truncate_table_query(session, TABLES)

    try:
        data = []

        # async def get_data_loop(entities, fields):
        #     for entity in entities:
        #         entity = await get_data(get_entity_config(fields))
        #         data_insert_loop(deals, get_entity_name(fields))
        #         data.append(entity)
        #         time.sleep(1)

        # ============================================================ #
        #
        # deals
        #
        deals = await get_data(get_entity_config(crm_deal_list))
        data_insert_loop(session, deals, get_entity_name(crm_deal_list))
        data.append(deals)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # document_elements
        #
        document_elements = await get_data(get_entity_config(catalog_document_element_list))
        data_insert_loop(session, document_elements, get_entity_name(catalog_document_element_list))
        data.append(document_elements)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # documents
        #
        documents = await get_data(get_entity_config(catalog_document_list))
        data_insert_loop(session, documents, get_entity_name(catalog_document_list))
        data.append(documents)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # storeproduct
        #
        storeproducts = await get_data(get_entity_config(catalog_storeproduct_list))
        data_insert_loop(session, storeproducts, get_entity_name(catalog_storeproduct_list))
        data.append(storeproducts)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # store
        #
        stores = await get_data(get_entity_config(catalog_store_list))
        data_insert_loop(session, stores, get_entity_name(catalog_store_list))
        data.append(stores)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # catalog
        #
        catalogs = await get_data(get_entity_config(catalog_catalog_list))
        data_insert_loop(session, catalogs, get_entity_name(catalog_catalog_list))
        data.append(catalogs)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # productrow
        #
        productrows = await get_data(get_entity_config(crm_productrow_fields(data[0])))
        data_insert_loop(session, productrows, get_entity_name(crm_productrow_fields(data[0])))
        data.append(productrows)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # product
        #
        products = await get_data(get_entity_config(crm_product_list))
        data_insert_loop(session, products, get_entity_name(crm_product_list))
        data.append(products)
        time.sleep(1)
        #
        # ============================================================ #

    except Exception as error:
        print(error)

    finally:
        session.commit()
        session.close()
        close_all_sessions()

asyncio.run(main())