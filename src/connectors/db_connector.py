from sqlalchemy import create_engine, MetaData


from env import webhook, DEFAULT_CONNECTION, SPREADSHEET_ID

from config.types import T_CONNECTION


class DBConnector:
    def __init__(self, connection: T_CONNECTION = DEFAULT_CONNECTION):
        self.__host = connection['host']
        self.__port = connection['port']
        self.__db = connection['db']
        self.__user = connection['user']
        self.__password = connection['password']

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