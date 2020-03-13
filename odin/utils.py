"""Utility function for Odin."""
import typing

import yaml


def get_targets(filename: str) -> typing.List[str]:
    """Load the configuration file.

    The configuration file is expected to be a YAML file listing
    the target urls as a list.
    For more information, refer to the README.md or the example configuration.
    """
    with open(filename) as config:
        targets = yaml.safe_load(config)
    return targets
