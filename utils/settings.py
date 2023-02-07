from sqlalchemy import create_engine, MetaData


from env import DEFAULT_settings, SPREADSHEET_ID

from utils.types import T_SETTINGS


class Settings:
    def __init__(self, settings: T_SETTINGS = DEFAULT_settings):
        self.__host = settings['host']
        self.__port = settings['port']
        self.__db = settings['db']
        self.__user = settings['user']
        self.__password = settings['password']

        self.__engine = create_engine(self.db_url)
        self.__metadata = MetaData()

    @property
    def db_url(self):
        return f'postgresql://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__db}'

    @property
    def spreadsheet_id(self):
        return SPREADSHEET_ID

    @property
    def engine(self):
        return self.__engine

    @property
    def metadata(self):
        return self.__metadata

    @property
    def connection(self):
        return self.engine.connect()