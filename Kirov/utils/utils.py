#
# Файл утилит должен быть без зависимостей от других модулей системы !!!
#


from typing import Union, List, Dict


def key_dict_to_lower(dict: Dict[str, any]) -> Dict[str, any]:
    return { key.lower(): value for key, value in dict.items() }

def props_list_to_lower(list: List[str]) -> List[str]:
    return [ value.lower() for value in list ]

def print_success(message: str):
    print(f"""
        ------ SUCCESS----------------------------------------------------------- SUCCESS ------
            {message}
        ----------------------------------------------------------------------------------------
        """
    )

def print_error(error: Exception):
    print(f"""
        ------ ERROR----------------------------------------------------------- ERROR ------
            {error}
        ------------------------------------------------------------------------------------
        """
    )



# def is_exist_db(db_url: str) -> bool:
#     return database_exists(db_url)

# def is_empty_table(session: Session, table) -> bool:
#     return session.query(table).count() == 0

# def is_exist_table(engine: Engine, tablename: str) -> bool:
#     return sqlalchemy.inspect(engine).has_table(tablename)

# def in_full_record_table(session: Session, table, number_of_records: int) -> bool:
#     return session.query(table).count() == number_of_records

# def records_in_table(session: Session, table) -> int:
#     return session.query(table).count()
