import pprint
import re  # noqa: F401

import six

from karix.models.object_meta_response import ObjectMetaResponse  # noqa: F401,E501
from karix.models.whatsapp_account_photo import WhatsappAccountPhoto


class InlineResponse2019(object):

    swagger_types = {
        'objects': 'list[WhatsappAccountPhoto]',
        'meta': 'ObjectMetaResponse'
    }

    attribute_map = {
        'data': 'data',
        'meta': 'meta'
    }

    def __init__(self, data=None, meta=None):  # noqa: E501
        self._data = None
        self._meta = None
        self.discriminator = None

        if data is not None:
            self.data = data
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
        if issubclass(InlineResponse2017, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InlineResponse2017):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
