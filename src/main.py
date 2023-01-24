import asyncio
import time
from sqlalchemy.orm import sessionmaker

# Local imports
from config import settings
from utils import get_engine, get_data
from queries import insert_data_to_tables, truncate_table_query
from models import Deal, DocumentElement, Document, StoreProduct, Store, Catalog, ProductRow, Product

from fields import crm_deal_list, catalog_document_element_list, catalog_document_list, catalog_storeProduct_list
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
    # После добавления новой сущности - добавить очистку ниже
    truncate_table_query(session, Deal)
    truncate_table_query(session, DocumentElement)
    truncate_table_query(session, Document)
    truncate_table_query(session, StoreProduct)
    truncate_table_query(session, Store)
    truncate_table_query(session, Catalog)
    truncate_table_query(session, ProductRow)
    truncate_table_query(session, Product)

    try:
        data = []
        # ============================================================ #
        #
        # deals
        #
        entity_config = crm_deal_list['entity_config']
        deals = await get_data(crm_deal_list['entity_config'])
        for deal in deals:
            if (deal['CLOSEDATE'] == ''):
                (deal['CLOSEDATE']) = None
            insert_data_to_tables(session, deal, entity_config['entity_name'])
        data.append(deals)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # document_elements
        #
        entity_config = catalog_document_element_list['entity_config']
        document_elements = await get_data(catalog_document_element_list['entity_config'])
        for document_element in document_elements:
            insert_data_to_tables(session, document_element, entity_config['entity_name'])
        data.append(document_elements)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # documents
        #
        entity_config = catalog_document_list['entity_config']
        documents = await get_data(entity_config)
        for document in documents:
            insert_data_to_tables(session, document, entity_config['entity_name'])
        data.append(documents)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # storeproduct
        #
        entity_config = catalog_storeProduct_list['entity_config']
        storeproducts = await get_data(entity_config)
        for storeproduct in storeproducts:
            insert_data_to_tables(session, storeproduct, entity_config['entity_name'])
        data.append(storeproducts)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # store
        #
        entity_config = catalog_store_list['entity_config']
        stores = await get_data(entity_config)
        for store in stores:
            insert_data_to_tables(session, store, entity_config['entity_name'])
        data.append(stores)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # catalog
        #
        entity_config = catalog_catalog_list['entity_config']
        catalogs = await get_data(entity_config)
        for catalog in catalogs:
            insert_data_to_tables(session, catalog, entity_config['entity_name'])
        data.append(catalogs)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # productrow
        #
        entity_config = crm_productrow_fields(data[0])['entity_config']
        productrows = await get_data(entity_config)
        for pruductrow in productrows:
            insert_data_to_tables(session, pruductrow, entity_config['entity_name'])
        data.append(productrows)
        time.sleep(1)
        #
        # ============================================================ #
        #
        # product
        #
        entity_config = crm_product_list['entity_config']
        products = await get_data(entity_config)
        for product in products:
            if (product['PROPERTY_119'] == None):
                product['PROPERTY_119'] = {
                    'valueId': None,
                    'value': None
                }
            insert_data_to_tables(session, product, entity_config['entity_name'])
        data.append(products)
        time.sleep(1)
        #
        # ============================================================ #

    except Exception as error:
        print(error)

    finally:
        session.commit()
        session.close()


asyncio.run(main())