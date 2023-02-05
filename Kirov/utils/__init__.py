from sqlalchemy import create_engine

from env import SERVER_settings
from utils.settings import Settings
from utils.types import T_SETTINGS
from utils.utils import print_success, print_error, key_dict_to_lower, props_list_to_lower, get_dict_by_indexes_of_list_of_lists, find_list_of_list_of_lists, convert_list_to_dict, convert_str_to_dict_or_list

class Utils:

    def __init__(self):
        self.__db_url = Settings(
            #SERVER_settings
        ).db_url

    @property
    def db_url():
        return Settings(
            #SERVER_settings
        ).db_url

    @property
    def engine(self):
        return create_engine(self.__db_url)
