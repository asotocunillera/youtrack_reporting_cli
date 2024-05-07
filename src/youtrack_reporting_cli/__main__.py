from youtrack_reporting_cli.client import YoutrackClient
from youtrack_reporting_cli.config import Config

config = Config()
yt_client = YoutrackClient(config=config)
project_fields = ["id", "name", "shortName", "description", "createdBy(login,name,id)"]
projects = yt_client.get("admin/projects", fields=project_fields)
print(projects["body"])
