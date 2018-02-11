#!C:\Users\Harry\AppData\Local\Programs\Python\Python35-32\python.exe.............
from parser_json_to_html import Parser_json_to_html
import os
import datetime
import filecmp

def __read_file(file_path):
    with open(file_path, 'r', encoding="utf8") as f:
        read_data = f.read()
    return read_data

def __write_new_file(dest_path_local, read_data):
     with open(dest_path_local, 'w', encoding="utf8") as new_f:
            new_f.write(read_data)


# test function - only used for testing
def main():
    now = datetime.datetime.now()
    new_file_name = '_' + str(now.day) + '_' + str(now.month) + '_' + str(now.year)
    file_path = r'''C:\\Users\\Harry\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\Bookmarks'''
    dir_path_txt_1 = os.path.dirname(os.path.realpath(__file__)) + '/test1.txt'
    dir_path_txt_2 = os.path.dirname(os.path.realpath(__file__)) + '/test2.txt'
    dir_path_html = os.path.dirname(os.path.realpath(__file__)) + '/output.html'
    dest_path_local = os.path.dirname(os.path.realpath(__file__)) + '/' + new_file_name
    parser = Parser_json_to_html()
    data = parser.parse_json_to_html(file_path, dir_path_txt_1, dir_path_html)
    
    read_data = __read_file(file_path)
    __write_new_file(dest_path_local, read_data)

    __write_new_file(dir_path_html, data)

    """if filecmp.cmp('', 'output.html', shallow=False):
        print(True)
    else:
        print(False)"""

if __name__ == "__main__":
    main()