import requests
from requests.auth import HTTPBasicAuth

from config import (
    JIRA_URL,
    JIRA_EMAIL,
    JIRA_API_TOKEN,
)


class JiraClient:

    def __init__(self):
        self.base_url = JIRA_URL.rstrip("/")
        self.auth = HTTPBasicAuth(
            JIRA_EMAIL,
            JIRA_API_TOKEN,
        )

        self.headers = {
            "Accept": "application/json"
        }

    def get(self, endpoint, params=None):
        """
        Generic GET request.
        """

        url = f"{self.base_url}{endpoint}"

        response = requests.get(
            url,
            auth=self.auth,
            headers=self.headers,
            params=params,
        )

        response.raise_for_status()

        return response.json()