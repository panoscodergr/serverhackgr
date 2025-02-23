import requests

class FileUploader:
    def upload(self, url, file_path):
        with open(file_path, 'rb') as file:
            response = requests.post(url, files={'file': file})
        return response
