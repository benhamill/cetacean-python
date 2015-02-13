#!/usr/bin/env python
# encoding: utf-8
class Resource(object):

    """Respresents a generic HAL resource."""

    def get_uri(self, rel):
        """Gets a URI from the document for a given rel.

        :rel: A string matching an expected rel
        :returns: A string that is the URI in question.

        """
        if unicode(rel) not in self._links(): return None

        return self._links()[unicode(rel)]['href']
