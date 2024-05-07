from abc import ABC, abstractmethod
from typing import Any, TypedDict

from requests.structures import CaseInsensitiveDict
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning


class Response(TypedDict):
    body: Any
    headers: CaseInsensitiveDict[str]
    reason: str
    status: int


class AbstractClient(ABC):

    # for now we disabled insecure request warnings
    disable_warnings(InsecureRequestWarning)

    @abstractmethod
    def get(
        self,
        endpoint: str,
        query: dict[str, Any] | None = None,
        fields: list[str] | None = None,
        limit: int = 0,
        skip: int = 0,
    ) -> Response:
        """
        GET HTTP Method

        Parameters
        ----------
        endpoint: str
            endpoint to do the http request
        query: dict[str, Any] | None (default `None`)
        fields: list[str] | None (default `None`)
        limit: int (default `0`)
        skip: int (default `0`)
        """
