import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from info import file_id, file_path_builder

def authenicate():
    gauth = GoogleAuth()

    gauth.LoadCredentialsFile("[1].txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("[1].txt")
    
    return gauth

def retrieve_file(accessed):
    path = file_path_builder('[2].pdf', '[3]')
    if not accessed:
        if not os.path.exists(path[1]):
            os.mkdir("[3]")

        drive = GoogleDrive(authenicate())
        file = drive.CreateFile({'id': file_id})
        download_mimetype = 'application/pdf'

        file.GetContentFile(path[0],  mimetype=download_mimetype)

        os.startfile(path[1])
    
    return path[0]