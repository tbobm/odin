"""HTTP-related functions and wrappers."""
from dataclasses import dataclass
import time
import typing

import requests

from odin import conf, logger


@dataclass
class HTTPResult:
    """Information gathered while processing HTTP calls."""

    target: str
    method: str
    error: bool
    duration: typing.Optional[float]
    http_code: typing.Optional[int]


def _perform_call(url: str) -> typing.Union[requests.Response, typing.Literal[False]]:
    try:
        logger.debug(
            "should have been using a timeout of %s",
            conf.HTTP_TIMEOUT,
        )
        # NOTE: configure request
        #       - different HTTP methods
        #       - authentication
        response = requests.get(url, timeout=conf.HTTP_TIMEOUT)
        return response
    except requests.exceptions.BaseHTTPError as http_error:
        logger.error(
            "could not reach url=%s reason=%r",
            url,
            http_error
        )
        return False
    except requests.exceptions.ReadTimeout:
        logger.error(
            "request timed out url=%s",
            url,
        )
        return False
    except requests.exceptions.ConnectionError:
        logger.error(
            "request failed url=%s",
            url,
        )
        return False


def _unreachable_response(url: str, duration: float) -> HTTPResult:
    return HTTPResult(url, "GET", True, duration, 0)


def perform_call(url: str) -> HTTPResult:
    """Perform the HTTP call and format output.

    .. code::javascript
        {
            "error": false,
            "http_code": 200,
            "duration": 1555, // response time in ms
        }
    """
    now = time.time()
    response = _perform_call(url)
    duration = time.time() - now
    if not response:
        return _unreachable_response(url, duration)
    logger.info("request executed in %s seconds", duration)
    try:
        # 4XX-5XX error codes
        response.raise_for_status()
        error = False
    except requests.exceptions.HTTPError as http_error:
        logger.error(
            "could not reach url=%s reason=%r",
            url,
            http_error
        )
        error = True
    result = HTTPResult(url, "GET", error, duration, response.status_code)
    return result


def contact_url(url: str) -> HTTPResult:
    """Perform HTTP calls on target urls."""
    result = perform_call(url)
    return result
