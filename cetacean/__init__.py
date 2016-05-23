# encoding: utf-8
"""
The HAL client that does almost nothing for you.

Cetacean doesn't know about HTTP. You set up your own Requests client and use it
to make requests. You feed then Cetacean the decoded bodies as strings and it
helps you pull useful data out of them.
"""

import json

from .resource import Resource
from .embedded_resource import EmbeddedResource
from .embedded_resource_collection import EmbeddedResourceCollection

__version__ = "1.0.1"

def Cetacean(raw):
    """Feed me a string containing HAL.

    :raw: a string containing a HAL document.
    :returns: a cetacean.Resource

    """
    return Resource(raw)

def _parse_hal(raw):
    """Parses the JSON body of a response.
    :returns: A parsed JSON body (dicts and lists).

    """
    return json.loads(raw)
