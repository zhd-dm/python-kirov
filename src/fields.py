import datetime

class DbDataTypes():
    def __init__(
        self,
        int: str,
        text: str,
        char: str,
        double: float,
        date: datetime.date,
        datetime: datetime.datetime,
        boolean: bool,
        # enum: ?,
        # money: ?,
        # json: ?
    ):
        self.int = int
        self.text = text
        self.char = char
        self.double = double
        self.date = date
        self.datetime = datetime
        self.boolean = boolean


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

class FieldParams():
    def __init__(
        self,
        param_obj: dict
    ):
        self.param_obj = param_obj

class EntityConfig():
    def __init__(
        self,
        parent_name: str,
        entity_name: str,
        type_method: str,
        params: FieldParams,
        columns: dict
    ):
        self.parent_name = parent_name
        self.entity_name = entity_name
        self.type_method = type_method
        self.params = params
        self.columns = columns

# class test(EntityConfig):
#     pass

# test(
#     'crm',
#     'deal',
#     'list',
#     { 'select': ['*', 'UF_*'] },
#     {
#         'ID': 'int',
#         'TITLE': 'text',
#         'STAGE_ID': 'text',
#         'CURRENCY_ID': 'text',
#         'OPPORTUNITY': 'double',
#         'CLOSEDATE': 'date',
#         'CLOSED': 'char',
#         'UF_CRM_1668857275565': 'enum'
#     }
# )

CrmDealList = EntityConfig(
    'crm',
    'deal',
    'list',
    { 'select': ['*', 'UF_*'] },
    {
        'ID': 'int',
        'TITLE': 'text',
        'STAGE_ID': 'text',
        'CURRENCY_ID': 'text',
        'OPPORTUNITY': 'double',
        'CLOSEDATE': 'date',
        'CLOSED': 'char',
        'UF_CRM_1668857275565': 'enum'
    }
)

CatalogDocumentElementList = EntityConfig(
    'catalog',
    'document.element',
    'list',
    { 'select': ['*', 'UF_*'] },
    {
        'ID': 'int',
        'TITLE': 'text',
        'STAGE_ID': 'text',
        'CURRENCY_ID': 'text',
        'OPPORTUNITY': 'double',
        'CLOSEDATE': 'date',
        'CLOSED': 'char',
        'UF_CRM_1668857275565': 'enum'
    }
)

CatalogDocumentList = EntityConfig(
    'catalog',
    'document',
    'list',
    { 'select': ['*', 'UF_*'] },
    {
        'id': 'int'
    }
)

CatalogStoreproductList = EntityConfig(
    'catalog',
    'storeproduct',
    'list',
    { 'select': ['*', 'UF_*'] },
    {
        'amount': 'double',
        'productId': 'int',
        'quantityReserved': 'double',
        'storeId': 'int'
    }
)

CatalogStoreList = EntityConfig(
    'catalog',
    'store',
    'list',
    { 'select': ['*', 'UF_*'] },
    {
        'id': 'int',
        'title': 'text'
    }
)

CatalogCatalogList = EntityConfig(
    'catalog',
    'catalog',
    'list',
    { 'select': ['*', 'UF_*'] },
    {
        'NAME': 'text'
    }
)

def CrmProductrowList(deals: list):
    return EntityConfig(
        'crm',
        'productrow',
        'list',
        { 'filter': {'OWNER_TYPE': 'D', 'OWNER_ID': [deal['ID'] for deal in deals]} },
        {
            'ID': 'int',
            'OWNER_ID': 'int',
            'PRODUCT_ID': 'int',
            'PRODUCT_NAME': 'text',
            'QUANTITY': 'double'
        }
)

CrmProductList = EntityConfig(
    'crm',
    'product',
    'list',
    { 'select': ['*', 'UF_*'] },
    {
        'ID': 'int',
        'NAME': 'text',
        'PROPERTY_119': 'int',
        'PROPERTY_119_VALUE': 'char'
    }
)

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
    'amount': 'double',
    'productId': 'int',
    'quantityReserved': 'double',
    'storeId': 'int'
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

def crm_productrow_list(deals: list) -> dict[str, str | dict[str, str]]:
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
