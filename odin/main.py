"""Monitor infrastructure."""
import typing

from odin import conf, logger, export
from odin import http_utils, utils


def process() -> typing.Generator[typing.Tuple[dict, str], None, None]:
    """Main loop."""
    targets = utils.get_targets(conf.CONFIG_LOCATION)
    for idx, url in enumerate(targets, 1):
        result = http_utils.contact_url(url)
        logger.info("idx=%s url=%s result=%r", idx, url, result)
        yield result, url


def run():
    """Loop-based program."""
    logger.info("starting up odin.")
    exporter = export.setup_prometheus_exporter()
    export.start_prometheus_exporter()
    while True:
        for result, target in process():
            exporter.labels(url=target, method='GET').set(result["error"])
