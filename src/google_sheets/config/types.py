from typing import List, Union


#
# Тип values который возвращается из Google Sheets
#
T_SHEET_VALUES_RETURN = List[List[str]]

#
# Тип values который передаем в Google Sheets
#
T_SHEET_VALUES_SEND = List[Union[str, int, List[Union[str, int]]]]

#
# Тип base_fields_to_db_types который приходит из Google Sheets
#
T_SHEET_BASE_FIELDS_TO_DB_TYPES = List[List[str]]