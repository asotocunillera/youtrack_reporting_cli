from typing import Any

import requests

from youtrack_reporting_cli.config import Config

from .abstract_client import AbstractClient, Response


class YoutrackClient(AbstractClient):
    def __init__(self, config: Config) -> None:
        self._base_url = f"{config.yt_scheme}://{config.yt_host}:{config.yt_port}/api"
        self._headers = {
            "Authorization": config.yt_auth,
            "Accept": "application/json",
            "Cache-Control": "no-cache",
        }

        self._disable_ssl_certificate_validation = (
            config.yt_disable_ssl_certificate_validation
        )
        self._verify = not self._disable_ssl_certificate_validation

    def get(
        self,
        endpoint: str,
        query: dict[str, Any] | None = None,
        fields: list[str] | None = None,
        limit: int = 0,
        skip: int = 0,
    ) -> Response:

        endpoint = f"{self._base_url}/{endpoint}"
        if fields is not None:
            endpoint = f"{endpoint}?fields={','.join(fields)}"

        # TODO: add query, limit and skip variables to endpoint
        response = requests.get(endpoint, headers=self._headers, verify=self._verify)
        return {
            "body": response.json(),
            "headers": response.headers,
            "reason": response.reason,
            "status": response.status_code,
        }
