from sqlalchemy import create_engine, MetaData


from env import webhook, DEFAULT_SETTINGS, SPREADSHEET_ID

from config.types import T_SETTINGS


class DBConnector:
    def __init__(self, settings: T_SETTINGS = DEFAULT_SETTINGS):
        self.__host = settings['host']
        self.__port = settings['port']
        self.__db = settings['db']
        self.__user = settings['user']
        self.__password = settings['password']

    @property
    def webhook(self):
        return webhook

    @property
    def db_url(self):
        return f'postgresql://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__db}'

    @property
    def spreadsheet_id(self):
        return SPREADSHEET_ID

    @property
    def engine(self):
        return create_engine(self.db_url)

    @property
    def metadata(self):
        return MetaData()

    @property
    def connection(self):
        return self.engine.connect()