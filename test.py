#!C:\Users\Harry\AppData\Local\Programs\Python\Python35-32\python.exe.............
from parser_json_to_html import Parser_json_to_html
import os
import filecmp

# test function - only used for testing
def main():
    file_path = r'''C:\\Users\\Harry\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\Bookmarks'''
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/test.txt'
    parser = Parser_json_to_html()
    parser.parse_json_to_html(file_path, dir_path)
    """if filecmp.cmp('test.txt', 'output.txt', shallow=False):
        print(True)
    else:
        print(False)"""

if __name__ == "__main__":
    main()