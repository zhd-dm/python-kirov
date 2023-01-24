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

catalog_storeproduct_list: dict[str, str | dict[str, str]] = {
    'entity_config': {
        'parent_name': 'catalog',
        'entity_name': 'storeproduct',
        'type_method': 'list',
        'params': {
            'select': ['*', 'UF_*']
        }
    },
    'storeProduct': {
        'amount': 'double',
        'productId': 'int',
        'quantityReserved': 'double',
        'storeId': 'int'
    }
}

catalog_store_list: dict[str, str | dict[str, str]] = {
    'entity_config': {
        'parent_name': 'catalog',
        'entity_name': 'store',
        'type_method': 'list',
        'params': {
            'select': ['*', 'UF_*']
        }
    },
    'id': 'int',
    'title': 'text'
}

catalog_catalog_list: dict[str, str | dict[str, str]] = {
    'entity_config': {
        'parent_name': 'catalog',
        'entity_name': 'catalog',
        'type_method': 'list',
        'params': {
            'select': ['*', 'UF_*']
        }
    },
    'NAME': 'text'
}

def crm_productrow_fields(deals: list) -> dict[str, str | dict[str, str]]:
    return {
        'entity_config': {
            'parent_name': 'crm',
            'entity_name': 'productrow',
            'type_method': 'list',
            'params': {
                'filter': {'OWNER_TYPE': 'D', 'OWNER_ID': [deal['ID'] for deal in deals]}
            }
        },
        'ID': 'int',
        'OWNER_ID': 'int',
        'PRODUCT_ID': 'int',
        'PRODUCT_NAME': 'text',
        'QUANTITY': 'double'
    }

crm_product_list: dict[str, str | dict[str, str]] = {
    'entity_config': {
        'parent_name': 'crm',
        'entity_name': 'product',
        'type_method': 'list',
        'params': {
            'select': ['*', 'UF_*']
        }
    },
    'ID': 'int',
    'NAME': 'text',
    # 'PROPERTY_119': 'json' {'valueId': '123', 'value': 'aaa'}
    'PROPERTY_119': 'int', # valueId
    'PROPERTY_119_VALUE': 'char' # value 
}
