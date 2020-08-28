import pprint
import re  # noqa: F401

import six

from karix.models.whatsapp_account_error import WhatsappAccountError  # noqa: F401,E501


class WhatsappAccountPhoto(object):

    swagger_types = {
        'number': 'str',
        'url': 'str'
    }
    attribute_map = {
        'number': 'number',
        'url': 'url'
    }

    def __init__(self, number=None, url=None):

        self._number = None
        self._url = None

        if number is not None:
            self.number = number
        if url is not None:
            self.url = url

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

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
        if issubclass(WhatsappAccountPhoto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WhatsappAccountPhoto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
