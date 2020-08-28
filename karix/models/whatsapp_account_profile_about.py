import pprint
import re  # noqa: F401

import six

from karix.models.whatsapp_account_error import WhatsappAccountError  # noqa: F401,E501


class WhatsappAccountProfileAbout(object):

    swagger_types = {
        'number': 'str',
        'text': 'str'
    }
    attribute_map = {
        'number': 'number',
        'text': 'text'
    }

    def __init__(self, number=None, text=None):

        self._number = None
        self._text = None

        if number is not None:
            self.number = number
        if text is not None:
            self.text = text

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

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
        if issubclass(WhatsappAccountProfileAbout, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WhatsappAccountProfileAbout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
