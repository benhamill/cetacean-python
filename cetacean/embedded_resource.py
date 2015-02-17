# encoding: utf-8

from .resource import Resource

class EmbeddedResource(Resource):

    """Represents an embedded HAL resource."""

    def __init__(self, document):
        """Pass it a dictionary built from a HAL resource.

        :document: A dictionary built from a HAL resource.

        """
        self._hal = document
