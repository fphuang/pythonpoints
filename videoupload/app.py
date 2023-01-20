import requests
import os

api_key = "kG1XL76KxpLhRyIxNTCAq4nd8EfTvfNJVHERoh5Aeui"
auth_url = f'https://sandbox.api.video/auth/api_key'
create_url = f'https://sandbox.api.video/videos'
CHUNK_SIZE = 6000000


def read_in_chunks(chunk_reader, chunk_size=CHUNK_SIZE):
    while True:
        data = chunk_reader.read(chunk_size)
        if not data:
            break
        yield data


def get_video_upload_url(video_id):
    return f"{create_url}/{video_id}/source"


class VideoUploader:
    def __init__(self, file: str):
        self._token = None
        self._file = file

    def shake_hands(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        payload = {"apiKey": api_key}

        response = requests.post(auth_url, json=payload, headers=headers)
        response = response.json()
        self._token = response.get("access_token")
        print(f"token: {self._token}")

    def auth_string(self):
        return f'Bearer {self._token}'

    def create_video_container(self) -> str:
        headers2 = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": self.auth_string()
        }

        payload2 = {
            'title': 'Demo Video from Fangping\'s mac',
            'description': 'Video upload test'
        }

        response = requests.post(create_url, json=payload2, headers=headers2).json()
        print(response)
        return response["videoId"]

    def upload_video(self, video_url):
        content_name = str(self._file)
        content_path = os.path.abspath(self._file)
        content_size = os.stat(content_path).st_size

        print(content_name, content_path, content_size)

        with open(content_path, "rb") as chunk_reader:
            index = 0
            offset = 0
            headers = {}

            for chunk in read_in_chunks(chunk_reader, CHUNK_SIZE):
                offset = index + len(chunk)
                headers['Content-Range'] = f'bytes {index}-{offset - 1} {content_size}'
                headers['Authorization'] = self.auth_string()
                index = offset

                try:
                    response = requests.post(video_url, files={"file": chunk}, headers=headers)
                    print(response.json())
                    print(f'response: {response}, Content-Range: {headers["Content-Range"]}')
                except Exception as ex:
                    print(ex)

    def start(self):
        self.shake_hands()
        video_id = self.create_video_container()
        video_upload_url = get_video_upload_url(video_id)
        self.upload_video(video_upload_url)


if __file__ == "__main__":
    VideoUploader("").start()
