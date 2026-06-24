from jira.client import JiraClient

jira = JiraClient()

me = jira.get("/rest/api/3/myself")

print(me["displayName"])
print(me["emailAddress"])