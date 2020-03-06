import os
from setuptools import setup, find_packages

BASE_DIR = os.path.dirname(__file__)

with open(os.path.join(BASE_DIR, "requirements.txt")) as f:
    requirements = f.readlines()

setup(
    name="odin",
    version="0.0.1",
    description="monitors HTTP targets",
    url="",
    author="Theo \"Bob\" Massard",
    author_email="massar_t@etna-alternance.net",
    license="MIT",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={"console_scripts": ["odin=odin.main:run"]},
)
