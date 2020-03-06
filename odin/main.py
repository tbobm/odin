"""Monitor infrastructure."""
import typing

import requests

from odin import conf, logger


def _perform_call(url: str) -> typing.Union[requests.Response, bool]:
    try:
        logger.debug(
            "should have been using a timeout of %s",
            conf.REQUEST_DEFAULT_TIMEOUT,
        )
        return requests.get(url)
    except requests.exceptions.BaseHTTPError:
        return False


def perform_call(url: str) -> dict:
    """Perform the HTTP call and format output.

    .. code::javascript
        {
            "error": false,
            "http_code": 200,
            "duration": 1555, // response time in ms
        }
    """
    result = dict()
    response = _perform_call(url)
    if result is False:
        result["error"] = True
        result["http_code"] = None
        # TODO: wrap _perform_call with a timer
        result["duration"] = 0
    else:
        result["error"] = False
        result["http_code"] = response.status_code
        result["duration"] = 0
    return result


def check(urls: typing.List[str]):
    """Perform HTTP calls on target urls."""
    for idx, url in enumerate(urls, 1):
        result = perform_call(url)
        logger.info("idx=%s url=%s result=%r", idx, url, result)
    # TODO: yield results for further processing


def process():
    """Main loop."""
    check(conf.TARGETS)
    # TODO: fetch results
    # TODO: implement result processing


def run():
    """Loop-based program."""
    while True:
        process()
