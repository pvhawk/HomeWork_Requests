import requests
import os
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, file_path):

        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload(self, file_path: str):
        files = []
        fullpaths = os.listdir(file_path)
        for file in fullpaths:
            if os.path.isfile(file): files.append(file)
        print(files)
        for file_name in files:
            href = self._get_upload_link(file_path=file_name).get("href", "")
            response = requests.put(href, data=open(file_name, 'rb'))
            response.raise_for_status()
            if response.status_code == 201:
                print("Success")


if __name__ == '__main__':

    path_to_file = os.getcwd()
    URL = 'https://cloud-api.yandex.net:443'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

