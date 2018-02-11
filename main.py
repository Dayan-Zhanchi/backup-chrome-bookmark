#!C:\Users\Harry\AppData\Local\Programs\Python\Python35-32\python.exe.............
import datetime
from parser_json_to_html import Parser_json_to_html
from dropbox_api_client import Dropbox_api_client

def __read_file(file_path):
    with open(file_path, 'r', encoding="utf8") as f:
        read_data = f.read()
    return read_data

def __write_new_file(dest_path_local, read_data):
     with open(dest_path_local, 'w', encoding="utf8") as new_f:
            new_f.write(read_data)

def main():
    # read google chrome bookmarks and make a backup by creating a new file somewhere else in the computer
    file_path = r'''C:\\Users\\Harry\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\Bookmarks'''
    now = datetime.datetime.now()
    new_file_name = '_' + str(now.day) + '_' + str(now.month) + '_' + str(now.year)
    new_file_name_html = 'bookmarks_' + new_file_name + '.html'
    dest_path_local = r'''C:\Users\Harry\Documents\Chrome Bookmarks\\''' + new_file_name
    dest_path = r'''/''' + new_file_name
    read_data = __read_file(file_path)
    __write_new_file(dest_path_local, read_data)

    # parse json and convert to html
    parser = Parser_json_to_html()

    # establish api connection and upload the backup to dropbox
    dropbox_api = Dropbox_api_client()
    dropbox_api.upload_file(dest_path_local, dest_path)



if __name__ == "__main__":
    main()
