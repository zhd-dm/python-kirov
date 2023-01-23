import datetime

# словарь типов данных БД и к какому типу Python они относятся
# ключ = тип данных БД
# значение = тип данных Python

db_data_types = {
    'int': int,
    'text': str,
    'char': str,
    'double': float,
    'date': datetime.date,
    'datetime': datetime.datetime,
    'boolean': bool,
    'enum': '?',
    'money': '?',
    'json': '?'
}

# словарь полей, где entity_config - конфиг запрашиваемой сущности
#
# entity_config {
#   parent_name - имя родительского метода
#   entity_name - имя сущности
#   type_method - тип метода сущности
#   params - params которые будут отправлены с запросом
# }
#
# остальные поля:
# ключ = имя поля
# значение = тип данных в БД

catalog_document_element_list: dict[str, str | dict[str, str]] = {
    'entity_config': {
        'parent_name': 'catalog',
        'entity_name': 'document.element',
        'type_method': 'list',
        'params': {
            'select': ['*', 'UF_*']
        }
    },
    'amount': 'double',
    'elementId': 'int',
    'storeTo': 'int'
}

catalog_document_list: dict[str, str | dict[str, str]] = {
    'entity_config': {
        'parent_name': 'catalog',
        'entity_name': 'document',
        'type_method': 'list',
        'params': {
            'select': ['*', 'UF_*']
        }
    },
    'id': 'int'
}

catalog_storeProduct_getFields: dict[str, str | dict[str, str]] = {
    'entity_config': {
        'parent_name': 'catalog',
        'entity_name': 'storeProduct',
        'type_method': 'getFields'
    },
    'storeProduct': {
        'amount': 'double',
        'productId': 'int',
        'quantityReserved': 'double',
        'storeId': 'int'
    }
}

catalog_store_getFields: dict[str, str | dict[str, str]] = {
    'entity_config': {
        'parent_name': 'catalog',
        'entity_name': 'store',
        'type_method': 'getFields'
    },
    'id': 'int',
    'title': 'text'
}

crm_catalog_fields: dict[str, str | dict[str, str]] = {
    'entity_config': {
        'parent_name': 'crm',
        'entity_name': 'catalog',
        'type_method': 'fields'
    },
    'NAME': 'text'
}

crm_productrow_fields: dict[str, str | dict[str, str]] = {
    'entity_config': {
        'parent_name': 'crm',
        'entity_name': 'productrow',
        'type_method': 'fields'
    },
    'ID': 'int',
    'OWNER_ID': 'int',
    'PRODUCT_ID': 'int',
    'PRODUCT_NAME': 'text',
    'QUANTITY': 'double'
}

crm_deal_list: dict[str, str | dict[str, str]] = {
    'entity_config': {
        'parent_name': 'crm',
        'entity_name': 'deal',
        'type_method': 'list',
        'params': {
            'select': ['*', 'UF_*']
        }
    },
    'ID': 'int',
    'TITLE': 'text',
    'STAGE_ID': 'text',
    'CURRENCY_ID': 'text',
    'OPPORTUNITY': 'double',
    'CLOSEDATE': 'date',
    'CLOSED': 'char',
    'UF_CRM_1668857275565': 'enum'
}

crm_product_list: dict[str, str | dict[str, str]] = {
    'entity_config': {
        'parent_name': 'crm',
        'entity_name': 'product',
        'type_method': 'list'
    },
    'ID': 'int',
    'NAME': 'text',
    # 'PROPERTY_119': 'json' {'valueId': '123', 'value': 'aaa'}
    'PROPERTY_119': 'int', # valueId
    'PROPERTY_119_VALUE': 'char' # value 
}
