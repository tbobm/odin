"""Monitor infrastructure."""
import time
import typing

from odin import conf, logger, export
from odin import http_utils, utils


def process() -> typing.Generator[typing.Tuple[http_utils.HTTPResult, str], None, None]:
    """Main loop."""
    targets = utils.get_targets(conf.CONFIG_LOCATION)
    for idx, url in enumerate(targets, 1):
        result = http_utils.contact_url(url)
        logger.info("idx=%s url=%s result=%r", idx, url, result)
        yield result, url


def run():
    """Loop-based program."""
    logger.info("starting up odin.")
    reachability, response_time_gauge = export.setup_prometheus_exporters()
    export.start_prometheus_exporter()
    while True:
        for result, target in process():
            reachability.labels(url=target, method='GET').set(result.error)
            response_time_gauge.labels(url=target, method='GET').set(result.duration)
        time.sleep(conf.SLEEPY_DURATION)
