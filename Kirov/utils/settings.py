from env import DEFAULT_settings

from utils.types import T_SETTINGS


class Settings:
    def __init__(self, settings: T_SETTINGS = DEFAULT_settings):
        self.__host = settings['host']
        self.__port = settings['port']
        self.__db = settings['db']
        self.__user = settings['user']
        self.__password = settings['password']

    @property
    def db_url(self):
        return f'postgresql://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__db}'