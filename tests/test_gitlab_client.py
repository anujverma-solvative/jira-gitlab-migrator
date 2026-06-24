from gitlab.client import GitLabClient
from config import GITLAB_PROJECT_ID

gitlab = GitLabClient()

project = gitlab.get(f"/api/v4/projects/{GITLAB_PROJECT_ID}")

print("Project Name :", project["name"])
print("Project ID   :", project["id"])
print("Visibility   :", project["visibility"])