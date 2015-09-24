# encoding: utf-8
"""
The HAL client that does almost nothing for you.

Cetacean doesn't know about HTTP. You set up your own Requests client and use it
to make requests. You feed then Cetacean the decoded bodies as strings and it
helps you pull useful data out of them.
"""

from setuptools import setup, find_packages

import cetacean

setup(
    name="Cetacean",
    version=cetacean.__version__,
    author="Ben Hamill",
    author_email="ben@benhamill.com",
    url="http://github.com/benhamill/cetacean-python#readme",
    license="MIT",
    description="The HAL client that does almost nothing for you.",
    long_description=__doc__,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
