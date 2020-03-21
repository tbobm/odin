"""Configuration variables."""
import os


HTTP_TIMEOUT = os.environ.get('ODIN_HTTP_TIMEOUT', 5)
SLEEPY_DURATION = int(os.environ.get('ODIN_SLEEP_DURATION', "30"))
CONFIG_LOCATION = os.environ.get("ODIN_CONFIG_FILE", "/app/odin.yaml")
