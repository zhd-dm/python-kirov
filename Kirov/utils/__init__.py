from sqlalchemy import create_engine

from utils.settings import Settings
from utils.types import T_SETTINGS
from utils.utils import get_data, print_success, print_error

class Utils:

    def __init__(self):
        self.__db_url = Settings().db_url

    @property
    def db_url():
        return Settings().db_url

    @property
    def engine(self):
        return create_engine(self.__db_url)
