from typing import List

from sqlalchemy import Column, Integer, String, Float, Text, Date
from sqlalchemy.dialects.postgresql import ENUM


from fields.base_entity_config import BaseConfig


class BaseColumns:

    @property
    def column_list(self):
        columns = [value for key, value in self.__dict__.items()]
        del columns[0]
        return columns
    
    def __init__(self, config: BaseConfig):
        self.__config = config
        self.__generate_columns()
        pass

    def __generate_columns(self):
        if self.__config.primary_key_field_lower == '':
            self.__config.keys('pk_tech_field')

        for key, value in self.__config.fields_lower.items():
            self.__set_column_to_class(key, value)

    def __set_column_to_class(self, key: str, python_type: str):

            if self.__config.primary_key_field_lower == '':
                setattr(self, 'pk_tech_field', self.__get_column_with_props('pk_tech_field', python_type))

            setattr(self, key, self.__get_column_with_props(key, python_type))

    def __get_column_with_props(self, key: str, python_type: str) -> Column:

        if key == 'id' or key == 'pk_tech_field':
            pass
            return Column(Integer, primary_key = True, name = key)
            
        match python_type:
            case 'int':
                return Column(Integer, name = key)
            case 'text':
                return Column(Text, name = key)
            case 'double':
                return Column(Float, name = key)
            case 'date':
                return Column(Date, name = key)
            case 'char':
                return Column(String, name = key)
            case 'enum':
                return Column(
                    ENUM(*self.__config.enums_lower[next(iter(self.__config.enums_lower))], name = f'enum_{key}'),
                    name = key
                )
