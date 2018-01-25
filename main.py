import datetime
import json_parser_to_html
from dropbox_api_connect import Dropbox_api

def read_file(file_path):
    with open(file_path, encoding="utf8") as f:
        read_data = f.read()
    return read_data

def write_new_file(dest_path, read_data):
     with open(dest_path, 'w', encoding="utf8") as new_f:
            new_f.write(read_data)

def main():
    # read google chrome bookmarks and make a backup by creating a new file somewhere else in the computer
    file_path = r'''C:\\Users\\Harry\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\Bookmarks'''
    now = datetime.datetime.now()
    new_file_name = '_' + str(now.day) + '_' + str(now.month) + '_' + str(now.year)
    dest_path = r'''C:\Users\Harry\Documents\Chrome Bookmarks\\''' + new_file_name
    read_data = read_file(file_path)
    write_new_file(dest_path, read_data)

    # establish api connection and upload the backup to dropbox
    dropbox_api = Dropbox_api()
    dropbox_api.__init__


if __name__ == "__main__":
    main()
