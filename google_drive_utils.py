# Authenticate with service account credentials
from google.oauth2 import service_account
from google.auth.transport.requests import Request
# Access Google Drive using the authenticated credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload,MediaIoBaseDownload
import os
import io
def get_drive_service():
    credentials = service_account.Credentials.from_service_account_file(
        'project-50039-73698bbbff76.json',
        scopes=['https://www.googleapis.com/auth/drive']
    )
    # Authenticate the credentials
    credentials.refresh(Request())
    # Build a Drive service object
    drive_service = build('drive', 'v3', credentials=credentials)
    return drive_service
    
def retrieve_files_from_drive(drive_service, files_to_retrieve):
  for file_obj in files_to_retrieve:
    # pylint: disable=maybe-no-member
    request = drive_service.files().get_media(fileId=file_obj["id"])
    fh = io.FileIO(f'{file_obj["name"]}', mode='wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
      status, done = downloader.next_chunk()
      print(f"Download {int(status.progress() * 100)}.")

def get_dataset_from_drive(drive_service):
    results = drive_service.files().list(pageSize=200).execute()
    items = results.get('files', [])
    files_to_retrieve = []
    if not items:
        print('No files found.')
    else:
        # print('Files:')
        for item in items:
            if item["name"].startswith("apnea-ecg-database"):
              print("fount dataset in drive")
              files_to_retrieve.append(item)
              print("starting download...")
              retrieve_files_from_drive(drive_service, files_to_retrieve)
