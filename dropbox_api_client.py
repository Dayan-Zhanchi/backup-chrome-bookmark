#!C:\Users\Harry\AppData\Local\Programs\Python\Python35-32\python.exe.............
# Include the Dropbox SDK
import dropbox

class Dropbox_api_client:
    # Establish connection with the dropbox api
    def __init__(self):
        with open('api_keys.txt','r') as f:
            api_file_path = f.read()
        self.dbx = dropbox.Dropbox(api_file_path)
        if(self.dbx.users_get_current_account() is not None):
            print("Successfully connected to dropbox api!")
        else:
            print("Failed to connect to the dropbox api!")

    def print_all_contents_directory(self):
        for entry in self.dbx.files_list_folder('').entries:
            print(entry.name)

    def upload_file(self, dest_path_local, dest_path):
        with open(dest_path_local, "rb") as f:
            self.dbx.files_upload(f.read(), dest_path)
        print("Successfully uploaded file to dropbox!")