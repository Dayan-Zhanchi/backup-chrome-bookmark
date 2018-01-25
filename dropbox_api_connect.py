# Include the Dropbox SDK
import dropbox

class Dropbox_api:

    def __init__(self):
        with open('api_keys.txt','r') as f:
            api_file_path = f.read()
        self.dbx = dropbox.Dropbox(api_file_path)
        print(dbx.users_get_current_account())