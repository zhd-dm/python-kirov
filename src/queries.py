from models import DocumentElement, Deal

def insert_data_to_tables(session, data, entity_name: str) -> None:
    match entity_name:
        case 'document.element':
            insert_data_to_document_element_table(session, data)
        case 'deal':
            insert_data_to_deal_table(session, data)

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

def insert_data_to_document_element_table(session, data: list | dict) -> None:
    data = DocumentElement(
        amount = data['amount'],
        elementId = data['elementId'],
        storeTo = data['storeTo']
    )
    session.add(data)


def truncate_table_query(session, entity) -> None:
    session.query(entity).delete()
