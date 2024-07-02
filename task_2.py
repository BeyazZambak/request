from tokens import token, path_to_file, path_to_disk
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {"Content Type" : "application/json", "Authorization": f"OAuth {self.token}"}
    
    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, "overwrite": "true"}
        responce = requests.get(upload_url, headers=headers, params=params).json()
        return responce

    def upload_file_to_disk(self, disk_file_path, path_to_file):
        href = self._get_upload_link(disk_file_path=disk_file_path)
        href = href['href']
        responce = requests.put(href, data=open(path_to_file, 'rb'))
        responce.raise_for_status()


if __name__ == '__main__':
    path_to_file = path_to_file
    path_to_disk = path_to_disk
    token = token
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk(path_to_disk, path_to_file)