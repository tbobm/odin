"""Prometheus-related hooks and metric exporters."""
from prometheus_client import Gauge, start_http_server


def setup_prometheus_exporter() -> Gauge:
    """Return a configured Prometheus exporter."""

    unreachability_gauge = Gauge(
        'odin_target_unreachable',
        '0 if odin can reach the target 1 otherwise',
        ['url', 'method'],
    )

    return unreachability_gauge


def start_prometheus_exporter():
    """Run the prometheus server."""
    start_http_server(8000)
