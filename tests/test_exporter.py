from jira.client import JiraClient
from jira.exporter import JiraExporter

jira = JiraClient()

exporter = JiraExporter(jira)

exporter.export_project("GMD")