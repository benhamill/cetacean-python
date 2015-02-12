# encoding: utf-8

from setuptools import setup

setup(
    name="Cetacean",
    version="0.0.1",
    author="Ben Hamill",
    author_email="ben@benhamill.com",
    url="http://github.com/benhamill/cetacean-python#readme",
    licens="MIT",
    description="The HAL client that does almost nothing for you.",
    long_description="""
The HAL client that does almost nothing for you.

Cetacean is tightly coupled to Requests, but doesn't actually call it. You set
up your own Requests client and use it to make requests. You feed Cetacean
Requests response objects and it helps you figure out if they're HAL documents
and pull useful data out of them if they are.
""",
    py_modules=["ceatacean"],
    classifiers=[],
)
