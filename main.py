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
    # set the file and destination paths
    file_path = r'''C:\\Users\\Harry\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\Bookmarks'''
    now = datetime.datetime.now()
    new_file_name_json = '_' + str(now.day) + '_' + str(now.month) + '_' + str(now.year)
    new_file_name_html = 'bookmarks_' + new_file_name_json + '.html'
    dest_path_local_json = r'''C:\Users\Harry\Documents\Chrome Bookmarks\\''' + new_file_name_json
    dest_path_local_html = r'''C:\Users\Harry\Documents\Chrome Bookmarks\\''' + new_file_name_html
    dropbox_dest_path_json = r'''/''' + new_file_name_json
    dropbox_dest_path_html = r'''/''' + new_file_name_html

    # read google chrome bookmarks and make a backup by creating a new file somewhere else in the computer
    json_data = __read_file(file_path)
    __write_new_file(dest_path_local_json, json_data)

    # parse json and convert to html
    parser = Parser_json_to_html()
    html_data = parser.parse_json_to_html(file_path)
    __write_new_file(dest_path_local_html, html_data)

    # establish api connection and upload the backups to dropbox
    dropbox_api = Dropbox_api_client()
    dropbox_api.upload_file(dest_path_local_json, dropbox_dest_path_json)
    dropbox_api.upload_file(dest_path_local_html, dropbox_dest_path_html)



if __name__ == "__main__":
    main()
