#!/usr/bin/env python
# encoding: utf-8

import re

class Response(object):

    """Represents an HTTP response that is hopefully a HAL document."""

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
