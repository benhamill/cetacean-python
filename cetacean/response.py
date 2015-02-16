# encoding: utf-8

import json
import re

from .resource import Resource

class Response(Resource):

    """Represents an HTTP response that is hopefully a HAL document."""

    _hal_regex = re.compile(r"application/hal\+json")

    def __init__(self, raw):
        """Pass it a string containing HAL.

        :raw: A string containing a HAL document.

        """
        self._hal = self._parse_hal(raw)

    def _parse_hal(self, raw):
        """Parses the JSON body of the response.
        :returns: A parsed JSON body (dicts and lists) or an empty dictionary.

        """
        return json.loads(raw)
