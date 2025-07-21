import os
import datetime
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = 'your-google-sheet-id-here'
RANGE_NAME = 'logger!A1'

def get_service():
    creds = None
    if os.path.exists('data/token.json'):
        creds = Credentials.from_authorized_user_file('data/token.json', SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('data/creds.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('data/token.json', 'w') as token:
            token.write(creds.to_json())
    return build('sheets', 'v4', credentials=creds)

def log_job(company, title, location, category, status, notes):
    service = get_service()
    sheet = service.spreadsheets()
    date_applied = datetime.datetime.now().strftime("%Y-%m-%d")
    values = [[company, title, location, date_applied, category, status, notes]]
    body = {"values": values}
    sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption="USER_ENTERED",
        body=body
    ).execute()
    print("✅ Job logged successfully!")

# Example usage
if __name__ == "__main__":
    log_job(
        company="Sample Co",
        title="Analyst",
        location="Remote",
        category="Data",
        status="Applied",
        notes="Test log"
    )
