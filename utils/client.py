import os
from typing import Any, Dict, Optional

import requests

BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
TIMEOUT = int(os.getenv("TIMEOUT", "15"))

DEFAULT_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> requests.Response:
    url = f"{BASE_URL}{path}"
    merged_headers = {**DEFAULT_HEADERS, **(headers or {})}

    return requests.request(
        method=method,
        url=url,
        params=params,
        json=json,
        headers=merged_headers,
        timeout=TIMEOUT,
    )


def get(path: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
    return request("GET", path, params=params)


def post(path: str, json: Dict[str, Any]) -> requests.Response:
    return request("POST", path, json=json)