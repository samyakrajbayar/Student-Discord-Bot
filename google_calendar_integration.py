import os
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

class GoogleCalendarIntegration:
    def __init__(self):
        self.service = None
        self.setup_service()
    
    def setup_service(self):
        """Setup Google Calendar API service"""
        creds = None
        
        # Check if we have stored credentials
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                # For Replit deployment, you'd want to handle OAuth differently
                # This is a simplified version for local development
                google_api_key = os.getenv('GOOGLE_API_KEY')
                if google_api_key:
                    # Use service account credentials instead
                    print("Using Google API Key for calendar access")
                    return None
                else:
                    print("Google Calendar integration not configured")
                    return None
        
        try:
            self.service = build('calendar', 'v3', credentials=creds)
            print("Google Calendar service initialized successfully!")
        except Exception as e:
            print(f"Failed to initialize Google Calendar service: {e}")
            self.service = None
    
    async def create_study_event(self, title: str, description: str, start_time: datetime.datetime, duration_minutes: int):
        """Create a study session event in Google Calendar"""
        if not self.service:
            return None
        
        end_time = start_time + datetime.timedelta(minutes=duration_minutes)
        
        event = {
            'summary': f'📚 {title}',
            'description': f'StudyMentor Session: {description}',
            'start': {
                'dateTime': start_time.isoformat(),
                'timeZone': 'America/New_York',  # You might want to make this configurable
            },
            'end': {
                'dateTime': end_time.isoformat(),
                'timeZone': 'America/New_York',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},  # 1 day before
                    {'method': 'popup', 'minutes': 10},  # 10 minutes before
                ],
            },
        }
        
        try:
            event = self.service.events().insert(calendarId='primary', body=event).execute()
            return event.get('htmlLink')
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None
    
    async def create_assignment_deadline(self, title: str, description: str, due_date: datetime.datetime):
        """Create an assignment deadline event"""
        if not self.service:
            return None
        
        event = {
            'summary': f'📝 DUE: {title}',
            'description': f'StudyMentor Assignment: {description}',
            'start': {
                'date': due_date.strftime('%Y-%m-%d'),
            },
            'end': {
                'date': due_date.strftime('%Y-%m-%d'),
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60 * 3},  # 3 days before
                    {'method': 'email', 'minutes': 24 * 60},      # 1 day before
                    {'method': 'popup', 'minutes': 60},           # 1 hour before
                ],
            },
        }
        
        try:
            event = self.service.events().insert(calendarId='primary', body=event).execute()
            return event.get('htmlLink')
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None
    
    async def get_upcoming_events(self, max_results: int = 10):
        """Get upcoming events from calendar"""
        if not self.service:
            return []
        
        try:
            now = datetime.datetime.utcnow().isoformat() + 'Z'
            events_result = self.service.events().list(
                calendarId='primary', 
                timeMin=now,
                maxResults=max_results, 
                singleEvents=True,
                orderBy='startTime'
            ).execute()
            events = events_result.get('items', [])
            
            formatted_events = []
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                formatted_events.append({
                    'summary': event['summary'],
                    'start': start,
                    'description': event.get('description', ''),
                    'link': event.get('htmlLink', '')
                })
            
            return formatted_events
        except HttpError as error:
            print(f'An error occurred: {error}')
            return []

# Global instance
calendar_integration = GoogleCalendarIntegration()

# Helper functions for Discord bot integration
async def add_study_session_to_calendar(title: str, description: str, start_time: datetime.datetime, duration: int):
    """Add study session to Google Calendar"""
    return await calendar_integration.create_study_event(title, description, start_time, duration)

async def add_assignment_to_calendar(title: str, description: str, due_date: datetime.datetime):
    """Add assignment deadline to Google Calendar"""
    return await calendar_integration.create_assignment_deadline(title, description, due_date)

async def get_calendar_events(max_results: int = 5):
    """Get upcoming calendar events"""
    return await calendar_integration.get_upcoming_events(max_results)