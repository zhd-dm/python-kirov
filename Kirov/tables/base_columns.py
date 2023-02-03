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
        self.__entity_config = config
        self.__generate_columns()

    def __generate_columns(self):
        for key, value in self.__entity_config.fields_lower.items():
            self.__set_column_to_class(key, value)

    def __set_column_to_class(self, key: str, python_type: str):

            if self.__entity_config.primary_key_field_lower == '':
                self.__entity_config.keys = 'pk_tech_field'
                setattr(self, 'pk_tech_field', self.__get_column_with_props('pk_tech_field', python_type))
            elif python_type == 'json':
                setattr(self, f'{key}_id', self.__get_column_with_props(f'{key}_id', python_type))
                setattr(self, f'{key}_value', self.__get_column_with_props(f'{key}_value', python_type))
            else:
                setattr(self, key, self.__get_column_with_props(key, python_type))

    def __get_column_with_props(self, key: str, python_type: str) -> Column:

        if key == 'id' or key == 'pk_tech_field':
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
                    ENUM(*self.__entity_config.enums_lower[next(iter(self.__entity_config.enums_lower))], name = f'enum_{key}'),
                    name = key
                )
            case 'json':
                if '_id' in key:
                    return Column(Integer, name = key)
                if '_value' in key:
                    return Column(String, name = key)
