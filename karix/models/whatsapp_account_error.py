import pprint
import re  # noqa: F401

import six


class WhatsappAccountError(object):

    swagger_types = {
        'param': 'str',
        'message': 'str'
    }

    attribute_map = {
        'param': 'param',
        'message': 'message'
    }

    def __init__(self, param=None, message=None):  # noqa: E501
        self._param = None
        self._message = None
        self.discriminator = None

        self.param = param
        self.message = message

    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, param):
        self._param = param

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if issubclass(WhatsappAccountError, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WhatsappAccountError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
