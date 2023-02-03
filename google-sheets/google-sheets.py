import os.path
import pickle
from typing import List, Union

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# from Kirov.env import SPREADSHEET_ID

T_SHEET_RANGE = str
T_SHEET_VALUES = List[Union[str, int, List[Union[str, int]]]]

class GoogleSheet:
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port = 0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.__service = build('sheets', 'v4', credentials = creds)

    def _read_range_values(self, range: T_SHEET_RANGE):
        result = self.__service.spreadsheets().values().get(spreadsheetId = SPREADSHEET_ID, range = range).execute()
        values = result.get('values', [])
        pass
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
        result = self.__service.spreadsheets().values().batchUpdate(spreadsheetId = SPREADSHEET_ID, body = body).execute()
        print(f'{result.get("totalUpdatedCells")} ячеек обновлено.')

        
def main():
   google_sheet = GoogleSheet()
   range = 'entity_config!A3:C35'
   print(google_sheet._read_range_values(range))

main()


#
# ======== Примеры ========
#

# => GET
#
#    google_sheet = GoogleSheet()
#    range = 'entity_config!A3:C35'

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