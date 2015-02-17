# encoding: utf-8
import sys
import collections
import cetacean

class Resource(collections.Mapping):

    """Respresents a HAL resource."""
    _attributes = None

    def __init__(self, raw):
        """Pass it a string containing HAL.

        :raw: A string containing a HAL document.

        """
        self._hal = cetacean._parse_hal(raw)


    def get_uri(self, rel):
        """Gets a URI from the document for a given rel.

        :rel: A string matching an expected rel
        :returns: A string that is the URI in question.

        """
        # if sys.version_info.major == 2:
        # Freakin' 2.6... :fistshake:
        if sys.version_info[0] == 2:
            rel = unicode(rel)

        if rel not in self.links: return None

        return self.links[rel]['href']


    @property
    def links(self):
        """The links part of the HAL document.

        """
        return self._hal['_links'] if '_links' in self._hal else {}

    @property
    def attributes(self):
        """A dicxtionary of just the attributes (not _links or _embedded).

        """
        if self._attributes != None: return self._attributes

        self._attributes = dict((key, val) for key, val in self._hal.items()
                if key not in ['_links', '_embedded'])

        return self._attributes

    def __getitem__(self, attribute_name):
        """Access to the attributes of the resource. Like a dictionary.
        :returns: The value of the attribute.

        """
        return self._hal[attribute_name]

    def __iter__(self):
        """Iterate over the items in the document. Like a dictionary."""
        return self._hal.__iter__()

    def __len__(self):
        """The length of the document. Like a dictionary."""
        return len(self._hal)

    def embedded(self, rel=None):
        """Get an embedded resource or all the embedded resources.

        :rel: Optional rel for the resource to get.
        :returns: A HAL document or a list of HAL documents.

        """
        if rel == None: return self._hal['_embedded']

        # if sys.version_info.major == 2:
        # Freakin' 2.6... :fistshake:
        if sys.version_info[0] == 2:
            rel = unicode(rel)

        document = self.embedded()[rel]

        if isinstance(document, collections.Mapping):
            return cetacean.EmbeddedResource(document)
        else:
            return cetacean.EmbeddedResourceCollection(document)
