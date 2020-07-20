import pprint
import re  # noqa: F401

import six

from karix.models.whatsapp_template import WhatsappTemplate  # noqa: F401,E501
from karix.models.object_meta_response import ObjectMetaResponse  # noqa: F401,E501


class InlineResponse2014(object):

    swagger_types = {
        'meta': 'ObjectMetaResponse',
        'data': 'WhatsappTemplate'
    }

    attribute_map = {
        'meta': 'meta',
        'data': 'data'
    }

    def __init__(self, meta=None, data=None):  # noqa: E501
        self._meta = None
        self._data = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        if data is not None:
            self.data = data

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, meta):
        self._meta = meta

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

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
        if issubclass(InlineResponse2014, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InlineResponse2014):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
