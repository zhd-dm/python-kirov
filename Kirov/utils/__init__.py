from sqlalchemy import create_engine
from utils.settings import Settings


class Utils:

    def __init__(self):
        self.__db_url = Settings().db_url

    @property
    def db_url():
        return Settings().db_url

    @property
    def engine(self):
        return create_engine(self.__db_url)