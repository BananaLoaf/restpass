try:
    from setuptools import setup
except ModuleNotFoundError:
    from distutils.core import setup

from restpass import PAYLOAD


with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()
description = "Terminal based graphical utility for generating restorable passwords"
assert description == LONG_DESCRIPTION.split("\n")[1]

PAYLOAD["description"] = description
PAYLOAD["long_description"] = LONG_DESCRIPTION


kwargs = {}
for key in PAYLOAD:
    if PAYLOAD[key]:
        kwargs[key] = PAYLOAD[key]


setup(**kwargs)
