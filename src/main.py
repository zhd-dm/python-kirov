import asyncio
import time
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import close_all_sessions

# Local imports
from fields.base_entity_config import BaseConfig
from fields._exports import LIST_OF_ENTITIES_CONFIG
from fields.crm_deal_list_fields import CRM_DEAL_LIST_CONFIG
from tables_const import TABLES
from utils import get_engine, old_get_data, get_data, get_entity_config, get_entity_name
from utils import prepare_db_table, insert_data_to_table, print_error, print_success
from queries import truncate_table_query, data_insert_loop

from old_fields import crm_deal_list, catalog_document_element_list, catalog_document_list, catalog_storeproduct_list
from old_fields import catalog_store_list, catalog_catalog_list, crm_productrow_list, crm_product_list, CrmDealList

# engine = get_engine()

# SessionLocal = sessionmaker(bind = engine)
# session = SessionLocal()

async def main():
    # Костыль для очистки таблиц поочередно
    # После добавления новой сущности - добавить в массив эту сущность
    # truncate_table_query(session, TABLES)

    try:
        data = []

        # async def old_get_data_loop(entities, fields):
        #     for entity in entities:
        #         entity = await old_get_data(get_entity_config(fields))
        #         data_insert_loop(deals, get_entity_name(fields))
        #         data.append(entity)
        #         time.sleep(1)

        for entity in LIST_OF_ENTITIES_CONFIG:
            ent_config = BaseConfig(entity)
            data = await get_data(ent_config)
            if prepare_db_table():
                if insert_data_to_table():
                    print_success(f'Сущность {ent_config.entity_name} занесена в таблицу {ent_config.entity_name}')
                    time.sleep(1)



        # ============================================================ #
        #
        # deals
        #
        # deals = await old_get_data(get_entity_config(crm_deal_list))
        # data_insert_loop(session, deals, get_entity_name(crm_deal_list))
        # data.append(deals)
        # time.sleep(1)
        #
        # ============================================================ #
        #
        # document_elements
        #
        # document_elements = await old_get_data(get_entity_config(catalog_document_element_list))
        # data_insert_loop(session, document_elements, get_entity_name(catalog_document_element_list))
        # data.append(document_elements)
        # time.sleep(1)
        #
        # ============================================================ #
        #
        # documents
        #
        # documents = await old_get_data(get_entity_config(catalog_document_list))
        # data_insert_loop(session, documents, get_entity_name(catalog_document_list))
        # data.append(documents)
        # time.sleep(1)
        #
        # ============================================================ #
        #
        # storeproduct
        #
        # storeproducts = await old_get_data(get_entity_config(catalog_storeproduct_list))
        # data_insert_loop(session, storeproducts, get_entity_name(catalog_storeproduct_list))
        # data.append(storeproducts)
        # time.sleep(1)
        #
        # ============================================================ #
        #
        # store
        #
        # stores = await old_get_data(get_entity_config(catalog_store_list))
        # data_insert_loop(session, stores, get_entity_name(catalog_store_list))
        # data.append(stores)
        # time.sleep(1)
        #
        # ============================================================ #
        #
        # catalog
        #
        # catalogs = await old_get_data(get_entity_config(catalog_catalog_list))
        # data_insert_loop(session, catalogs, get_entity_name(catalog_catalog_list))
        # data.append(catalogs)
        # time.sleep(1)
        #
        # ============================================================ #
        #
        # productrow
        #
        # productrows = await old_get_data(get_entity_config(crm_productrow_list(data[0])))
        # data_insert_loop(session, productrows, get_entity_name(crm_productrow_list(data[0])))
        # data.append(productrows)
        # time.sleep(1)
        #
        # ============================================================ #
        #
        # product
        #
        # products = await old_get_data(get_entity_config(crm_product_list))
        # data_insert_loop(session, products, get_entity_name(crm_product_list))
        # data.append(products)
        # time.sleep(1)
        #
        # ============================================================ #

    except Exception as error:
        print_error(error)

    finally:
        print()
        print('finally')
        # session.commit()
        # session.close()
        # close_all_sessions()

asyncio.run(main())