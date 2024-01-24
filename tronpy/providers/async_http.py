import os
from typing import Any, Union
from urllib.parse import urljoin

import httpx
from httpx import Timeout

from tronpy.version import VERSION

DEFAULT_TIMEOUT = 10.0
DEFAULT_API_KEY = "f92221d5-7056-4366-b96f-65d3662ec2d9"


class AsyncHTTPProvider:
    """An Async HTTP Provider for API request.
        if endpoint_uri is None:
            self.endpoint_uri = os.environ.get("TRONPY_HTTP_PROVIDER_URI", "https://api.trongrid.io/")
        elif isinstance(endpoint_uri, (dict,)):
            self.endpoint_uri = endpoint_uri["fullnode"]
        elif isinstance(endpoint_uri, (str,)):
            self.endpoint_uri = endpoint_uri
        else:
            raise TypeError(f"unknown endpoint uri {endpoint_uri}")

        headers = {"User-Agent": f"Tronpy/{VERSION}", "Tron-Pro-Api-Key": api_key}
        if jw_token is not None:
            headers["Authorization"] = f"Bearer {jw_token}"
        if client is None:
            self.client = httpx.AsyncClient(headers=headers, timeout=Timeout(timeout))
        else:
            self.client = client

        self.timeout = timeout
        """Request timeout in second."""

    async def make_request(self, method: str, params: Any = None) -> dict:
        if params is None:
            params = {}
        url = urljoin(self.endpoint_uri, method)
        resp = await self.client.post(url, json=params)
        resp.raise_for_status()
        return resp.json()
