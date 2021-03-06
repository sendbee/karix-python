import pprint
import re  # noqa: F401

import six

from karix.models.whatsapp_account import WhatsappAccount  # noqa: F401,E501
from karix.models.array_meta_response import ArrayMetaResponse  # noqa: F401,E501


class InlineResponse2015(object):
    swagger_types = {
        'objects': 'list[WhatsappAccount]',
        'meta': 'ArrayMetaResponse'
    }

    attribute_map = {
        'objects': 'objects',
        'meta': 'meta'
    }

    def __init__(self, objects=None, meta=None):  # noqa: E501
        self._objects = None
        self._meta = None
        self.discriminator = None

        if objects is not None:
            self.objects = objects
        if meta is not None:
            self.meta = meta

    @property
    def objects(self):
        return self._objects

    @objects.setter
    def objects(self, objects):
        self._objects = objects

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, meta):
        self._meta = meta

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse2015, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InlineResponse2015):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
