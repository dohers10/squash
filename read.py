from __future__ import print_function

from google.oauth2 import service_account


import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1oLlHd_DcgYN9dAs7qcA_Nx2Z6skKprDwwimdUu-81nI'
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Squash Premier League - 2023!B1:K9").execute()
values = result.get('values', [])
#print(values)

# Calculate the row number to start appending data
matchday_number = int(input("Enter the Matchday number: "))  # Input matchday number as before
start_row = (matchday_number - 1) * 3 + 5  # Calculate the starting row


# Append to google sheet
data = [["Squash1"]]
res = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=f"Test!A{start_row}", 
                            valueInputOption="USER_ENTERED", insertDataOption="OVERWRITE",
                            body={"values":data}).execute()

# Append to google sheet
# data = [["Squash1"]]  # Your data here
# res = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range=f"Squash Premier League - 2023!A{start_row}",
#                             valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS",
#                             body={"values": data}).execute()

# print(res)

# if not values:
#     print('No data found.')
#     return

# print('Name, Major:')
# for row in values:
#     # Print columns A and E, which correspond to indices 0 and 4.
#     print('%s, %s' % (row[0], row[4]))
# except HttpError as err:
# print(err)