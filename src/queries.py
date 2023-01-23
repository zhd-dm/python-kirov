# При добавлении новых сущностей, нужно создать новую функцию для INSERT данных этой сущности
# Также нужно в match..case добавить вызов этой функции 

from models import DocumentElement, Document, Deal

def insert_data_to_tables(session, data, entity_name: str) -> None:
    match entity_name:
        case 'document.element':
            insert_data_to_document_element_table(session, data)
        case 'document':
            insert_data_to_document_table(session, data)
        case 'deal':
            insert_data_to_deal_table(session, data)

def insert_data_to_document_element_table(session, data: list | dict) -> None:
    data = DocumentElement(
        amount = data['amount'],
        elementId = data['elementId'],
        storeTo = data['storeTo']
    )
    session.add(data)

def insert_data_to_document_table(session, data: list | dict) -> None:
    data = Document(
        id = data['id']
    )
    session.add(data)

def insert_data_to_deal_table(session, data: list | dict) -> None:
    deal = Deal(
        id = data['ID'],
        title = data['TITLE'],
        stage_id = data['STAGE_ID'],
        currency_id = data['CURRENCY_ID'],
        opportunity = data['OPPORTUNITY'],
        closedate = data['CLOSEDATE'],
        closed = data['CLOSED'],
        uf_crm_1668857275565 = data['UF_CRM_1668857275565']
    )
    session.add(deal)

def truncate_table_query(session, entity) -> None:
    session.query(entity).delete()
