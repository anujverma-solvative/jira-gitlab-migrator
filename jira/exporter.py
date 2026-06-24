import json
import os
from urllib import response

from jira.client import JiraClient


class JiraExporter:

    def __init__(self, jira: JiraClient):
        self.jira = jira

    def export_project(self, project_key: str):

        print(f"Exporting project {project_key}")

        issues = []

        start_at = 0
        max_results = 100

        while True:

            response = self.jira.get(
                "/rest/api/3/search/jql",
                params={
                    "jql": f"project={project_key}",
                    "startAt": start_at,
                    "maxResults": max_results,
                },
            )
            print(response)

            batch = response["issues"]

            issues.extend(batch)

            print(f"Downloaded {len(issues)} issues...")

            if response.get("isLast", False):
                break

            start_at += max_results

        os.makedirs("storage/exports", exist_ok=True)

        filename = f"storage/exports/{project_key}.json"

        with open(filename, "w") as f:
            json.dump(issues, f, indent=2)

        print(f"\nSaved {len(issues)} issues to {filename}")