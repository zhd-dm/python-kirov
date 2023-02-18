from utils.mapping import print_error


from core.pg.config.types import T_PG_TABLE, T_PG_FIELDS, T_PG_ENUMS


def _invalid_conf(conf: T_PG_TABLE) -> bool:
    return _invalid_name(conf.get('name')) \
        or _invalid_primary_key(conf.get('primary_key')) \
        or _invalid_fields(conf.get('fields')) \
        or _invalid_enums(conf.get('enums'))

def _invalid_name(name: str) -> bool:
    if not isinstance(name, str) or name.__len__ == 0:
        print_error('Некорректно указано поле name')
        return True
    return False

def _invalid_primary_key(primary_key: str) -> bool:
    if not isinstance(primary_key, str) or primary_key.__len__ == 0:
        print_error('Некорректно указано поле primary_key')
        return True
    return False

def _invalid_fields(fields: T_PG_FIELDS) -> bool:
    if \
    not isinstance(fields, dict) \
    or not all(isinstance(key, str) for key in fields.keys()) \
    or not all(isinstance(value, str) for value in fields.values()):
        print_error('Некорректно указано поле fields')
        return True
    return False

def _invalid_enums(enums: T_PG_ENUMS) -> bool:
    if \
    not isinstance(enums, dict) \
    or not all(isinstance(value, list) for value in enums.values()):
        print_error('Некорректно указано поле enums')
        return True
    return False