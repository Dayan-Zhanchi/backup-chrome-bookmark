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

    def __init__(self):
        # get json file and convert to readable chrome bookmark html file
        self.output_html_file = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
        <!-- This is an automatically generated file.
        It will be read and overwritten.
        DO NOT EDIT! -->
        <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
        <TITLE>Bookmarks</TITLE>
        <H1>Bookmarks</H1>
        <DL><p>\n""" 

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
        
        # note it's important to convert the timestamp argument into an int
        # also important to round the answer down with int
        chrome_timestamp = int(chrome_timestamp)
        if (chrome_timestamp - 11644473600000000) <= 0:
            unix_timestamp = 0
        else:
            unix_timestamp = int((chrome_timestamp - 11644473600000000) / 10**6)
        return unix_timestamp

    def __close_DL_p_tag(self):
        self.output_html_file = "".join((self.output_html_file, "</DL><p>\n"))

    def __create_folder_node(self, name, date, date_modified, output_html_file):
        self.output_html_file = "".join((output_html_file, '<DT><H3 ADD_DATE="{date}" LAST_MODIFIED="{last_modified}">{name}</H3>\n<DL><p>\n'.format(
                    name = name, 
                    date = self.__convert_chrometimestamp_to_unixtimestamp(date),
                    last_modified = self.__convert_chrometimestamp_to_unixtimestamp(date_modified)
                    )))

    def __create_url_node(self, url, name, date, output_html_file):
        self.output_html_file = "".join((output_html_file, '<DT><A HREF="{url}" ADD_DATE="{date}">{name}</A>\n'.format(
                    url = url,
                    name = name,
                    date = self.__convert_chrometimestamp_to_unixtimestamp(date)
                    )))

    def __parse_json_to_html_helper(self, json_data):
        for node in json_data:
            if 'url' in node:
                self.__create_url_node(
                    node['url'],
                    node['name'], 
                    node['date_added'],  
                    self.output_html_file)

            elif node['children'] == []:
                self.__create_folder_node(
                    node['name'], 
                    node['date_added'],
                    node['date_modified'],
                    self.output_html_file)
                self.__close_DL_p_tag()

            elif node['children']:
                self.__create_folder_node(
                    node['name'], 
                    node['date_added'],
                    node['date_modified'],
                    self.output_html_file)
                self.__parse_json_to_html_helper(node['children'])
                self.__close_DL_p_tag()
                
    def parse_json_to_html(self, file_path):
        node = self.__get_json_data(file_path)

        if node['roots']['bookmark_bar']:
            """self.output_html_file = "".join((self.output_html_file, '<DT><H3 ADD_DATE="{date}" LAST_MODIFIED="{last_modified}" PERSONAL_TOOLBAR="{boolean}">{name}</H3>\n<DL><p>\n'.format(
                name = node['roots']['bookmark_bar']['name'], 
                date = self.__convert_chrometimestamp_to_unixtimestamp(node['roots']['bookmark_bar']['date_added']),
                last_modified = self.__convert_chrometimestamp_to_unixtimestamp(node['roots']['bookmark_bar']['date_modified']),
                boolean = "true"
                )))"""
            self.__parse_json_to_html_helper(node['roots']['bookmark_bar']['children'])
            #self.__close_DL_p_tag()

        if node['roots']['other']:
            self.__create_folder_node(
                node['roots']['other']['name'], 
                node['roots']['other']['date_added'],
                node['roots']['other']['date_modified'],
                self.output_html_file)
            self.__parse_json_to_html_helper(node['roots']['other']['children'])
            self.__close_DL_p_tag()

        if node['roots']['synced']:
            self.__parse_json_to_html_helper(node['roots']['synced']['children'])
            self.__close_DL_p_tag()

        return self.output_html_file
