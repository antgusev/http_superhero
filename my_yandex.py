import requests
import json
import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        # Тут ваша логика
        # Функция может ничего не возвращать
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            "path": f'Python/{path_to_file}'
        }
        headers = {
            "Authorization": token
        }
        response = requests.get(url, headers=headers, params=params)
        # print(response.status_code)
        # pprint(response.json())
        url_for_upload = response.json().get('href', '')
        with open(path_to_file, 'rb') as file:
            result2 = requests.put(url_for_upload, files={"file": file})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "1000009148.jpg"
    token =
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
