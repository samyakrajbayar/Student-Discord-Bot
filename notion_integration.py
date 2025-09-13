import os
from notion_client import Client
from datetime import datetime
import json

class NotionIntegration:
    def __init__(self):
        self.client = None
        self.database_id = None
        self.setup_client()
    
    def setup_client(self):
        """Initialize Notion client"""
        notion_token = os.getenv('NOTION_TOKEN')
        self.database_id = os.getenv('NOTION_DATABASE_ID')
        
        if notion_token:
            try:
                self.client = Client(auth=notion_token)
                print("Notion client initialized successfully!")
            except Exception as e:
                print(f"Failed to initialize Notion client: {e}")
                self.client = None
        else:
            print("Notion integration not configured - NOTION_TOKEN not found")
    
    async def create_task_page(self, title: str, description: str, due_date: str = None, priority: int = 1):
        """Create a new task page in Notion"""
        if not self.client or not self.database_id:
            return None
        
        try:
            # Prepare properties for the new page
            properties = {
                "Title": {
                    "title": [
                        {
                            "text": {
                                "content": title
                            }
                        }
                    ]
                },
                "Description": {
                    "rich_text": [
                        {
                            "text": {
                                "content": description
                            }
                        }
                    ]
                },
                "Status": {
                    "select": {
                        "name": "Not Started"
                    }
                },
                "Priority": {
                    "select": {
                        "name": "High" if priority == 3 else "Medium" if priority == 2 else "Low"
                    }
                },
                "Created": {
                    "date": {
                        "start": datetime.now().isoformat()
                    }
                }
            }
            
            # Add due date if provided
            if due_date and due_date != "No deadline":
                try:
                    # Parse various date formats
                    if len(due_date) == 10:  # YYYY-MM-DD
                        properties["Due Date"] = {
                            "date": {
                                "start": due_date
                            }
                        }
                except:
                    pass  # Skip if date parsing fails
            
            # Create the page
            new_page = self.client.pages.create(
                parent={"database_id": self.database_id},
                properties=properties
            )
            
            return new_page['url']
        except Exception as e:
            print(f"Failed to create Notion page: {e}")
            return None
    
    async def update_task_status(self, page_id: str, status: str):
        """Update the status of a task in Notion"""
        if not self.client:
            return False
        
        try:
            self.client.pages.update(
                page_id=page_id,
                properties={
                    "Status": {
                        "select": {
                            "name": status
                        }
                    }
                }
            )
            return True
        except Exception as e:
            print(f"Failed to update Notion page: {e}")
            return False
    
    async def create_study_log(self, subject: str, duration: int, notes: str = ""):
        """Create a study session log in Notion"""
        if not self.client or not self.database_id:
            return None
        
        try:
            properties = {
                "Subject": {
                    "title": [
                        {
                            "text": {
                                "content": f"Study Session: {subject}"
                            }
                        }
                    ]
                },
                "Duration": {
                    "number": duration
                },
                "Date": {
                    "date": {
                        "start": datetime.now().isoformat()
                    }
                },
                "Notes": {
                    "rich_text": [
                        {
                            "text": {
                                "content": notes or f"Studied {subject} for {duration} minutes"
                            }
                        }
                    ]
                },
                "Type": {
                    "select": {
                        "name": "Study Session"
                    }
                }
            }
            
            new_page = self.client.pages.create(
                parent={"database_id": self.database_id},
                properties=properties
            )
            
            return new_page['url']
        except Exception as e:
            print(f"Failed to create study log in Notion: {e}")
            return None
    
    async def get_recent_tasks(self, limit: int = 10):
        """Get recent tasks from Notion database"""
        if not self.client or not self.database_id:
            return []
        
        try:
            results = self.client.databases.query(
                database_id=self.database_id,
                sorts=[
                    {
                        "property": "Created",
                        "direction": "descending"
                    }
                ],
                page_size=limit
            )
            
            tasks = []
            for page in results['results']:
                props = page['properties']
                task = {
                    'id': page['id'],
                    'title': props.get('Title', {}).get('title', [{}])[0].get('text', {}).get('content', 'Untitled'),
                    'status': props.get('Status', {}).get('select', {}).get('name', 'Unknown'),
                    'priority': props.get('Priority', {}).get('select', {}).get('name', 'Low'),
                    'url': page['url']
                }
                
                # Get due date if available
                due_date = props.get('Due Date', {}).get('date')
                if due_date:
                    task['due_date'] = due_date.get('start')
                
                tasks.append(task)
            
            return tasks
        except Exception as e:
            print(f"Failed to get tasks from Notion: {e}")
            return []

# Global instance
notion_integration = NotionIntegration()

# Helper functions for Discord bot integration
async def sync_task_to_notion(title: str, description: str, due_date: str = None, priority: int = 1):
    """Sync a task to Notion"""
    return await notion_integration.create_task_page(title, description, due_date, priority)

async def log_study_session_to_notion(subject: str, duration: int, notes: str = ""):
    """Log study session to Notion"""
    return await notion_integration.create_study_log(subject, duration, notes)

async def get_notion_tasks(limit: int = 5):
    """Get recent tasks from Notion"""
    return await notion_integration.get_recent_tasks(limit)