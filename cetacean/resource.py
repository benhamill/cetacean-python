#!/usr/bin/env python
# encoding: utf-8
class Resource(object):

    """Respresents a generic HAL resource."""

    def get_uri(self, rel):
        """Gets a URI from the document for a given rel.

        :rel: A string matching an expected rel
        :returns: A string that is the URI in question.

        """
        if unicode(rel) not in self.links: return None

        return self.links[unicode(rel)]['href']


    @property
    def links(self):
        """Return the links part of the HAL document.
        :returns: A dictionary of the links or an empty dictionary.

        """
        return self._hal['_links'] if '_links' in self._hal else {}
