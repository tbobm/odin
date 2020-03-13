"""Configuration variables."""
import os


HTTP_TIMEOUT = os.environ.get('ODIN_HTTP_TIMEOUT', 5)
CONFIG_LOCATION = os.environ.get("ODIN_CONFIG_FILE", "/app/odin.yaml")
