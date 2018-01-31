import base64
import requests
import json
from bs4 import BeautifulSoup

class Convert_json_to_html:

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
                return uri
            else:
                print(response.status_code)
        except requests.Timeout as e:
            print("It is time to timeout")
            print(str(e))

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

    def __get_page_link_from_json(self, file_path):
        data = json.load(open(file_path))
        return page_url

    def __convert_chrometimstamp_to_unixtimestamp(self, chrome_timestamp):
        """ chrome timestamp is in microseconds since Jan 1, 1601 and is 1/10 of windows timestamp
            unix timestamp is in seconds since Jan 1, 1970
            the base date-times difference between chrome and unix time format is 11644473600000000 in microseconds
        """
        unix_timestamp = (chrome_timestamp - 11644473600000000) / 10^6 
        return unix_timestamp

    def convert_json_to_html(self, file_path):
        open with(file_path) as json_data:
            data = json.load(json_data)
        page_url = __get_page_link_from_json(file_path)
        # get favicon link
        favicon_link = __get_page_favicon_link(page_url)
        # get json file and convert to readable chrome bookmark html file
        print("")