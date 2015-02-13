#!/usr/bin/env python
# encoding: utf-8
"""
The HAL client that does almost nothing for you.

Cetacean is tightly coupled to Requests, but doesn't actually call it. You set
up your own Requests client and use it to make requests. You feed Cetacean
Requests response objects and it helps you figure out if they're HAL documents
and pull useful data out of them if they are.
"""

__version__ = "0.0.1"

import re

class Cetacean(object):
    pass

class Cetacean(object):

    """The HAL client that does almost nothing for you."""

    def __init__(self, response):
        """Pass it a Requests response object.

        :response: A response object from the Requests library.

        """
        self._response = response
        self._hal_regex = re.compile(r"application/hal\+json")

    def is_hal(self):
        """Test if a response was a HAL document or not.
        :returns: True or False

        """
        return self._hal_regex.match(self._response.headers['content-type'])
