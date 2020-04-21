"""HTTP-related functions and wrappers."""
import time
import typing

import requests

from odin import conf, logger


def _perform_call(url: str) -> typing.Union[requests.Response, bool]:
    try:
        logger.debug(
            "should have been using a timeout of %s",
            conf.HTTP_TIMEOUT,
        )
        # NOTE: configure request
        #       - different HTTP methods
        #       - authentication
        response = requests.get(url, timeout=conf.HTTP_TIMEOUT)
        response.raise_for_status()
        return response
    except (requests.exceptions.BaseHTTPError, requests.exceptions.HTTPError) as http_error:
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
    now = time.time()
    response = _perform_call(url)
    duration = time.time() - now
    logger.info("request executed in %s seconds", duration)
    if response is False:
        result["error"] = True
        result["http_code"] = None
        result["duration"] = duration
    else:
        result["error"] = False
        result["http_code"] = response.status_code
        result["duration"] = duration
    return result


def contact_url(url: str):
    """Perform HTTP calls on target urls."""
    result = perform_call(url)
    return result
