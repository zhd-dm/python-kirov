import os.path
import pickle
from typing import List, Union

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from utils.settings import Settings

DEFAULT_LIST_NAME = 'entity_config!'
RANGE_BASE_FIELDS_TO_DB_TYPES = 'A3:C'

T_SHEET_RANGE = str
T_SHEET_VALUES = List[Union[str, int, List[Union[str, int]]]]

class GoogleSheet:
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self, list_name: str = DEFAULT_LIST_NAME):
        creds = None
        if os.path.exists('token.pickle'):
            pass
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                pass
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
                creds = flow.run_local_server(port = 0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        if list_name:
            self.__list_name = list_name
        else:
            self.__list_name = DEFAULT_LIST_NAME

        

        self.__service = build('sheets', 'v4', credentials = creds)

    def _get_range_values(self, range: T_SHEET_RANGE):
        range = self.__list_name + range
        result = self.__service.spreadsheets().values().get(spreadsheetId = Settings().spreadsheet_id, range = range).execute()
        values = result.get('values', [])
        return values

    def _update_range_values(self, range: T_SHEET_RANGE, values: T_SHEET_VALUES):
        data = [{
            'range': range,
            'values': values
        }]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        result = self.__service.spreadsheets().values().batchUpdate(spreadsheetId = Settings().spreadsheet_id, body = body).execute()
        print(f'{result.get("totalUpdatedCells")} ячеек обновлено.')

    def _get_base_fields_to_db_types(self):
        return self._get_range_values(RANGE_BASE_FIELDS_TO_DB_TYPES)


# => A3:C - выборка base_fields_to_db_types
# => G3:I - выборка для crm.deal.list
#

#
# ======== Примеры ========
#

# => GET
#
#    google_sheet = GoogleSheet()
#    range = 'entity_config!A3:C35'
#    google_sheet._get_range_values(range)

# ============================================

# => UPDATE
#
#    google_sheet = GoogleSheet()
#    range = 'entity_config!A1:B4'
#    values = [
#        [16, 26],
#        [36, 46],
#        [56, 66]
#    ]
#    google_sheet._update_range_values(range, values)