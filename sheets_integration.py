"""
Google Sheets Integration Module
Handles reading from and writing to Google Sheets for complaint management
"""

import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from datetime import datetime
import os
from typing import List, Dict, Optional

class GoogleSheetsManager:
    """Manages Google Sheets operations for complaint data"""
    
    def __init__(self):
        """Initialize Google Sheets connection"""
        self.scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        self.creds = None
        self.client = None
        self.sheet = None
        self.worksheet = None
        
        # Try to connect if credentials are available
        self._connect()
    
    def _connect(self):
        """Establish connection to Google Sheets"""
        try:
            creds_file = os.getenv('GOOGLE_SHEETS_CREDENTIALS', 'credentials.json')
            if os.path.exists(creds_file):
                self.creds = Credentials.from_service_account_file(
                    creds_file, 
                    scopes=self.scope
                )
                self.client = gspread.authorize(self.creds)
                
                # Open the spreadsheet
                sheet_name = os.getenv('GOOGLE_SHEET_NAME', 'Campus Complaints')
                self.sheet = self.client.open(sheet_name)
                self.worksheet = self.sheet.sheet1
                print("[OK] Connected to Google Sheets")
            else:
                print("[INFO] Google Sheets credentials not found. Using local CSV fallback.")
        except Exception as e:
            print(f"[INFO] Could not connect to Google Sheets: {e}")
            print("Using local CSV fallback.")
    
    def get_all_complaints(self) -> List[Dict]:
        """
        Retrieve all complaints from Google Sheets or local CSV
        
        Returns:
            List of complaint dictionaries
        """
        try:
            if self.worksheet:
                # Get data from Google Sheets
                records = self.worksheet.get_all_records()
                return records
            else:
                # Fallback to local CSV
                return self._read_from_csv()
        except Exception as e:
            print(f"Error reading complaints: {e}")
            return self._read_from_csv()
    
    def _read_from_csv(self) -> List[Dict]:
        """Read complaints from local CSV file"""
        try:
            csv_file = 'Campus_Sustainability_Twin_AI_500_Row_Dataset.csv'
            if os.path.exists(csv_file):
                df = pd.read_csv(csv_file)
                return df.to_dict('records')
            return []
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return []
    
    def add_complaint(self, complaint_data: Dict) -> str:
        """
        Add a new complaint to Google Sheets
        
        Args:
            complaint_data: Dictionary containing complaint information
            
        Returns:
            Complaint ID
        """
        try:
            # Generate complaint ID
            all_complaints = self.get_all_complaints()
            if all_complaints:
                last_id = max([int(c.get('Complaint_ID', 'C0000')[1:]) for c in all_complaints])
                complaint_id = f"C{str(last_id + 1).zfill(4)}"
            else:
                complaint_id = "C0001"
            
            # Prepare row data
            row = [
                complaint_id,
                complaint_data.get('category', ''),
                complaint_data.get('location', ''),
                complaint_data.get('complaint', ''),
                complaint_data.get('priority', 'Medium'),
                complaint_data.get('status', 'Open'),
                complaint_data.get('users_affected', 1),
                complaint_data.get('date', datetime.now().strftime('%d-%m-%Y'))
            ]
            
            if self.worksheet:
                # Add to Google Sheets
                self.worksheet.append_row(row)
            else:
                # Add to local CSV
                self._append_to_csv(row)
            
            return complaint_id
            
        except Exception as e:
            print(f"Error adding complaint: {e}")
            raise
    
    def _append_to_csv(self, row: List):
        """Append a row to local CSV file"""
        try:
            csv_file = 'Campus_Sustainability_Twin_AI_500_Row_Dataset.csv'
            df = pd.read_csv(csv_file)
            new_row = pd.DataFrame([row], columns=df.columns)
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(csv_file, index=False)
        except Exception as e:
            print(f"Error appending to CSV: {e}")
    
    def get_complaint(self, complaint_id: str) -> Optional[Dict]:
        """
        Get a specific complaint by ID
        
        Args:
            complaint_id: The complaint ID to retrieve
            
        Returns:
            Complaint dictionary or None if not found
        """
        try:
            all_complaints = self.get_all_complaints()
            for complaint in all_complaints:
                if complaint.get('Complaint_ID') == complaint_id:
                    return complaint
            return None
        except Exception as e:
            print(f"Error getting complaint: {e}")
            return None
    
    def update_complaint_status(self, complaint_id: str, status: str, notes: Optional[str] = None) -> bool:
        """
        Update the status of a complaint
        
        Args:
            complaint_id: The complaint ID to update
            status: New status (Open, In Progress, Resolved)
            notes: Optional notes about the update
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if self.worksheet:
                # Find the row with the complaint ID
                cell = self.worksheet.find(complaint_id)
                if cell:
                    # Update status column (column 6)
                    self.worksheet.update_cell(cell.row, 6, status)
                    return True
            else:
                # Update in CSV
                return self._update_csv_status(complaint_id, status)
            return False
        except Exception as e:
            print(f"Error updating complaint status: {e}")
            return False
    
    def _update_csv_status(self, complaint_id: str, status: str) -> bool:
        """Update complaint status in local CSV"""
        try:
            csv_file = 'Campus_Sustainability_Twin_AI_500_Row_Dataset.csv'
            df = pd.read_csv(csv_file)
            df.loc[df['Complaint_ID'] == complaint_id, 'Status'] = status
            df.to_csv(csv_file, index=False)
            return True
        except Exception as e:
            print(f"Error updating CSV status: {e}")
            return False
    
    def get_complaints_by_category(self, category: str) -> List[Dict]:
        """Get all complaints for a specific category"""
        all_complaints = self.get_all_complaints()
        return [c for c in all_complaints if c.get('Category') == category]
    
    def get_complaints_by_priority(self, priority: str) -> List[Dict]:
        """Get all complaints with a specific priority"""
        all_complaints = self.get_all_complaints()
        return [c for c in all_complaints if c.get('Priority') == priority]
    
    def get_complaints_by_status(self, status: str) -> List[Dict]:
        """Get all complaints with a specific status"""
        all_complaints = self.get_all_complaints()
        return [c for c in all_complaints if c.get('Status') == status]

# Made with Bob
