def get_columns(parent_entity: str, entity_name: str) -> list:
    str = '{}.{}'.format(parent_entity, entity_name)
    match str:
        case 'crm.deal':
            return ['ID', 'TITLE', 'TYPE_ID', 'STAGE_ID', 'PROBABILITY', 'CURRENCY_ID', 'OPPORTUNITY', 'IS_MANUAL_OPPORTUNITY']
        case 'crm.invoice':
            return []
        case 'crm.product':
            return []
        case 'crm.company':
            return []
        case 'crm.contact':
            return []
        case 'catalog.document':
            return []
        case 'catalog.document.element':
            return []
        case _:
            return []