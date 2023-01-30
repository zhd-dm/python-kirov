from typing import List

from fields.base_fields import DEFAULT_ENTITY_CONFIG, DEFAULT_CALL_METHOD, DEFAULT_PARAMS, DEFAULT_KEYS, DEFAULT_FIELDS, ENTITY_BASE_KEYS, BASE_FIELDS_TO_DB_TYPES
from fields.base_types import T_ENTITY_CONFIG_WITH_FIELDS, T_ENTITY_CONFIG, T_CALL_METHOD, T_PARAMS, T_KEYS, T_FIELDS


# fields
from fields.catalog_catalog_list_fields import CATALOG_CATALOG_LIST_CONFIG
from fields.catalog_document_element_list_fields import CATALOG_DOCUMENT_ELEMENT_LIST_CONFIG
from fields.catalog_document_list_fields import CATALOG_DOCUMENT_LIST_CONFIG
from fields.catalog_store_list import CATALOG_STORE_LIST_CONFIG
from fields.catalog_storeproduct_list_fields import CATALOG_STOREPRODUCT_LIST_CONFIG
from fields.crm_deal_list_fields import CRM_DEAL_LIST_CONFIG
from fields.crm_product_list_fields import CRM_PRODUCT_LIST_CONFIG
from fields.crm_productrow_list_fields import CRM_PRODUCTROW_LIST_CONFIG


LIST_OF_ENTITIES_CONFIG: List[T_ENTITY_CONFIG_WITH_FIELDS] = [
    CATALOG_CATALOG_LIST_CONFIG,
    CATALOG_DOCUMENT_ELEMENT_LIST_CONFIG,
    CATALOG_DOCUMENT_LIST_CONFIG,
    CATALOG_STORE_LIST_CONFIG,
    CATALOG_STOREPRODUCT_LIST_CONFIG,
    CRM_DEAL_LIST_CONFIG,
    CRM_PRODUCT_LIST_CONFIG,
    CRM_PRODUCTROW_LIST_CONFIG
]
