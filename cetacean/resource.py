#!/usr/bin/env python
# encoding: utf-8
class Resource(object):

    """Respresents a generic HAL resource."""

    def get_uri(self, rel):
        """Gets a URI from the document for a given rel.

        :rel: A string matching an expected rel
        :returns: A string that is the URI in question.

        """
        return unless links.include?(rel.to_s)

        URITemplate.new(links[rel.to_s]['href'])
