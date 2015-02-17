# encoding: utf-8

import collections
import cetacean

class EmbeddedResourceCollection(collections.Sequence):

    """Represents a list of embedded HAL resources"""

    def __init__(self, document_list):
        """Pass in a list of HAL recourses.

        :document_list: A list of HAL resources.

        """
        self._document_list = document_list

    def __getitem__(self, index):
        """Access to the contained HAL documents. Like a list.

        :returns: A cetacean.EmbeddedResource.

        """
        return cetacean.EmbeddedResource(self._document_list[index])

    def __len__(self):
        """Get the length of the collection. List a list.

        """
        return len(self._document_list)
