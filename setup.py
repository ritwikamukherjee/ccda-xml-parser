from setuptools import setup
from io import open
from os import path
import sys

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="ccda-parser",
    version="0.0.1",
    python_requires='>=3.9',
    author="",
    author_email="",
    description= "",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[''],
    packages=[''],
    py_modules=['']
)