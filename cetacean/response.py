#!/usr/bin/env python
# encoding: utf-8

import json
import re

from .resource import Resource

class Response(Resource):

    """Represents an HTTP response that is hopefully a HAL document."""

    def __init__(self, response):
        """Pass it a Requests response object.

        :response: A response object from the Requests library.

        """
        self._response = response
        self._hal_regex = re.compile(r"application/hal\+json")
        self._hal = None

    def is_hal(self):
        """Test if a response was a HAL document or not.
        :returns: True or False

        """
        return bool(self._hal_regex.match(self._response.headers['content-type']))

    def _hal(self):
        """Returns the parsed HAL body of the response
        :returns: A parsed HAL body (dicts and lists) or an empty dictionary.

        """
        if self._hal != None: return self._hal

        self._hal = _parse_hal()

        return self._hal

    def _parse_hal(self):
        """Parses the JSON body of the response.
        :returns: A parsed JSON body (dicts and lists) or an empty dictionary.

        """
        if not is_hal(): return {}

        try:
            return json.loads(self._response.content)
        except ValueError, e:
            return {}
