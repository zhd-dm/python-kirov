from sqlalchemy import Column, Integer, String, Float, Text, Date
from sqlalchemy.dialects.postgresql import ENUM


from fields.base_entity_config import BaseConfig


class CrmDealList:
    
    def __init__(self, config: BaseConfig):
        self.__config = config
        self.__tablename__ = self.__config.entity_name

        self.__generate_columns()

    def __generate_columns(self):
        for key, value in self.__config.fields_lower.items():
            setattr(self, key, self.__get_column_with_props(key, value))

    def __get_column_with_props(self, key: str, python_type: str) -> Column:
        match python_type:
            case 'int':
                return Column(Integer)
            case 'text':
                return Column(Text)
            case 'double':
                return Column(Float)
            case 'date':
                return Column(Date)
            case 'char':
                return Column(String)
            case 'enum':
                return Column(ENUM(*self.__config.enums_lower[next(iter(self.__config.enums_lower))], name = f'enum_{key}'))

            