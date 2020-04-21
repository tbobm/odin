"""Prometheus-related hooks and metric exporters."""
import typing

from prometheus_client import Gauge, start_http_server


def setup_prometheus_exporters() -> typing.Tuple[Gauge, Gauge]:
    """Return a configured Prometheus exporter."""
    unreachability_gauge = Gauge(
        'odin_target_unreachable',
        '0 if odin can reach the target 1 otherwise',
        ['url', 'method'],
    )
    request_duration = Gauge(
        'odin_http_call_duration',
        'Duration in seconds of the call',
        ['url', 'method'],
        )
    return unreachability_gauge, request_duration


def start_prometheus_exporter():
    """Run the prometheus server."""
    start_http_server(8000)
