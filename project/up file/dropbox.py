from pydrive.auth import GoogleAuth

from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'hello.txt'})

file1.SetContentString('Hello World!')

file1.upload()