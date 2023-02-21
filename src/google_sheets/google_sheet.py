import os.path
import pickle
from typing import List, Union

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from core.connectors.db_connector import DBConnector
from core.connectors.gs_connector import GSConnector
from utils.mapping import print_success

from google_sheets.config.constants import DEFAULT_SHEET_NAME
from google_sheets.config.types import T_SHEET_VALUES_RETURN, T_SHEET_VALUES_SEND


class GoogleSheet:
    """
    Класс обращения к Google Sheets по переданному sheet_name

    Аргументы:
    - `sheet_name: str` - имя листа, с которым будем работать, по умолчанию DEFAULT_SHEET_NAME

    Пример:

    google_sheet = GoogleSheet('sheet_name!')
    """

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self, list_name: str = DEFAULT_SHEET_NAME):
        creds = None
        self.__spreadsheet_id = GSConnector().spreadsheet_id
        
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
                creds = flow.run_local_server(port = 0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        if list_name:
            self.__list_name = list_name
        else:
            self.__list_name = DEFAULT_SHEET_NAME

        self.__service = build('sheets', 'v4', credentials = creds)

    def _get_range_values(self, range: str) -> T_SHEET_VALUES_RETURN:
        """
        Метод получения списка списков из Google Sheets по переданному range

        Аргументы:
        - `range: str` - диапазон полей которые будем доставать

        Пример:

        _get_range_values('A3:C') -> [[1, 2, 3], [4, 5, 6], [7, 8, 9], ...]
        """
        range = self.__list_name + range
        result = self.__service.spreadsheets().values().get(spreadsheetId = self.__spreadsheet_id, range = range).execute()
        values = result.get('values', [])
        return values

    def _update_range_values(self, range: str, values: T_SHEET_VALUES_SEND):
        """
        Метод отправки значений в Google Sheets по переданному словарю

        Аргументы:
        - `range: str` - диапазон полей в которые будем записывать значения
        - `values: T_SHEET_VALUES_SEND` - значения которые запишем в эти поля

        Пример:

        google_sheet._update_range_values('entity_config!A1:B4', [[16, 26], [36, 46], [56, 66]])
        """
        data = [{
            'range': range,
            'values': values
        }]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        result = self.__service.spreadsheets().values().batchUpdate(spreadsheetId = self.__spreadsheet_id, body = body).execute()
        print_success(f'{result.get("totalUpdatedCells")} ячеек обновлено.')
