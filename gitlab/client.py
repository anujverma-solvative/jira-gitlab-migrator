import requests

from config import (
    GITLAB_URL,
    GITLAB_TOKEN,
)


class GitLabClient:

    def __init__(self):
        self.base_url = GITLAB_URL.rstrip("/")

        self.headers = {
            "PRIVATE-TOKEN": GITLAB_TOKEN,
            "Content-Type": "application/json",
        }

    def get(self, endpoint, params=None):

        url = f"{self.base_url}{endpoint}"

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
        )

        response.raise_for_status()

        return response.json()

    def post(self, endpoint, payload):

        url = f"{self.base_url}{endpoint}"

        response = requests.post(
            url,
            headers=self.headers,
            json=payload,
        )

        response.raise_for_status()

        return response.json()