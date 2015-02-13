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

def Cetacean(response):
    """Feed me a response object from the Requests library.

    :response: a requests.models.Response
    :returns: a cetacean.Response

    """
    return Response(response)
