from typing import List

from sqlalchemy import Column, Integer, String, Float, Text, Date
from sqlalchemy.dialects.postgresql import ENUM


from core.entity_configs.entity_config import EntityConfig


class BaseColumns:

    @property
    def column_list(self) -> List[Column]:
        columns = [value for key, value in self.__dict__.items()]
        del columns[0]
        return columns
    
    def __init__(self, ent_conf: EntityConfig):
        self.__ent_conf = ent_conf
        self.__generate_columns()

    def __generate_columns(self):
        for key, value in self.__ent_conf.field_to_py_type.items():
            self.__set_column_to_class(key, value)

    def __set_column_to_class(self, key: str, python_type: str):

        #
        # REFACTOR:
        # Подумать над переработкой этого метода
        #

        if self.__ent_conf.primary_key == '':
            setattr(self, 'pk_tech_field', self.__get_column('pk_tech_field', python_type))

        if python_type == 'json':
            setattr(self, f'{key}_id', self.__get_column(f'{key}_id', python_type))
            setattr(self, f'{key}_value', self.__get_column(f'{key}_value', python_type))
        else:
            setattr(self, key, self.__get_column(key, python_type))

    def __get_column(self, key: str, python_type: str) -> Column:

        #
        # REFACTOR:
        # Подумать над переработкой этого метода
        #

        if key == self.__ent_conf.primary_key or key == 'pk_tech_field':
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
                    ENUM(*self.__ent_conf.enums[next(iter(self.__ent_conf.enums))], name = f'enum_{key}'),
                    name = key
                )
            case 'json':
                if self.__ent_conf.entity_name == 'catalog.product.offer.list':
                    if '_id' in key:
                        return Column(Integer, name = key)
                    if '_value' in key:
                        return Column(Integer, name = key)
                else:
                    if '_id' in key:
                        return Column(Integer, name = key)
                    if '_value' in key:
                        return Column(String, name = key)
