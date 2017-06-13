import os
from datetime import timedelta
import datetime
import pytz
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

service_account_email = 'new-383@lucid-formula-170000.iam.gserviceaccount.com'

CLIENT_SECRET_FILE = 'client_secrets.json'

SCOPES = 'https://www.googleapis.com/auth/calendar'
scopes = [SCOPES]

def build_service():
    credentials = ServiceAccountCredentials.from_json_keyfile(
        service_account_email=service_account_email,
        filename=CLIENT_SECRET_FILE,
        scopes=SCOPES
    )

    http = credentials.authorize(httplib2.Http())

    service = build('calendar', 'v3', http=http)

    return service


def create_event():
    service = build_service()

    start_datetime = datetime.datetime.now(tz=pytz.utc)
    event = service.events().insert(calendarId='<suyashgarg2>@gmail.com', body={
        'summary': 'Foo',
        'description': 'Bar',
        'start': {'dateTime': start_datetime.isoformat()},
        'end': {'dateTime': (start_datetime + timedelta(minutes=15)).isoformat()},
    }).execute()

    print(event)
