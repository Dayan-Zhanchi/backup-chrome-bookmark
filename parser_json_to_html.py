#!C:\Users\Harry\AppData\Local\Programs\Python\Python35-32\python.exe.............
import os
import base64
import requests
import json
from bs4 import BeautifulSoup

class Parser_json_to_html:

    # converts the bookmark file to an html file in Netscape bookmark file format
    # for more information about Netscape bookmark file format visit the link below
    # link: https://msdn.microsoft.com/en-us/library/aa753582(v=vs.85).aspx

    def __write_new_file(self, dest_path_local, read_data):
        with open(dest_path_local, 'w', encoding="utf8") as new_f:
                new_f.write(read_data)

    def __get_json_data(self, file_path):
        with open(file_path, 'r', encoding='utf8') as json_data:
            data = json.load(json_data)
        return data
    
    def __get_page_favicon_link(self, url):
        # function may still not work if the favicon is somewhere else
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                favicon_link1 = soup.find('link', rel='shortcut icon')
                if favicon_link1 is not None:
                    return favicon_link1
                else:
                    favicon_link2 = soup.find('link', rel='icon')
                    if favicon_link2 is not None:
                        return favicon_link2
                    else:
                        try:
                            favicon_link3 = url + '/favicon.ico'
                            response = requests.get(favicon_link3, timeout=5)
                            if response.status_code == 200:
                                return favicon_link3
                            else:
                                print(response.status_code)
                        except requests.Timeout as e:
                            print("It is time to timeout")
                            print(str(e))
            else:
                print(response.status_code)
        except requests.Timeout as e:
            print("It is time to timeout")
            print(str(e))

    def __convert_img_url_to_base64(self, img_url):
        try:
            response = requests.get(img_url, timeout=5)
            if response.status_code == 200:
                print(response.content)
                b64 = base64.b64encode(response.content)
                print(b64)
                uri = ("data:" + 
                response.headers['Content-Type'] + ";" +
                "base64," + str(base64.b64encode(response.content).decode("utf-8")))
                print(response.headers['Content-Type'])
                print(uri)
                return uri
            else:
                print(response.status_code)
        except requests.Timeout as e:
            print("It is time to timeout")
            print(str(e))


    def __convert_chrometimestamp_to_unixtimestamp(self, chrome_timestamp):
        # chrome timestamp is in microseconds since Jan 1, 1601 and is 1/10 of windows timestamp
        # unix timestamp is in seconds since Jan 1, 1970
        # the base date-times difference between chrome and unix time format is 11644473600000000 in microseconds
        
        unix_timestamp = (chrome_timestamp - 11644473600000000) / 10^6 
        return unix_timestamp

    def __parse_json_to_html_helper(self, json_data, output_html_file, dest_file_path):
        self.__write_new_file(dest_file_path, json.dumps(json_data['roots']['bookmark_bar'], indent = 4))
        print(len(json_data['roots']['bookmark_bar']))

    def parse_json_to_html(self, file_path, dest_file_path):
        # get json file and convert to readable chrome bookmark html file
        output_html_file = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
        <!-- This is an automatically generated file.
        It will be read and overwritten.
        DO NOT EDIT! -->
        <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
        <TITLE>Bookmarks</TITLE>
        <H1>Bookmarks</H1>
        <DL><p>
        
        """ 
        data = self.__get_json_data(file_path)
        self.__parse_json_to_html_helper(data, output_html_file, dest_file_path)

