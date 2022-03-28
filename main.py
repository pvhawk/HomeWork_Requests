# import requests
import os
from pprint import pprint



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        pass


if __name__ == '__main__':
    BASE_PATH = os.getcwd()
    NAME_FILE = 'TEST.TXT'
    path_to_file = os.path.join(BASE_PATH, NAME_FILE)
    print(path_to_file)
    URL = 'https://cloud-api.yandex.net:443'
    token = 'AQAAAAAgbrfDAADLW4zLGVzNH0x8gyNUpBkWV3c'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
