import pprint
import re  # noqa: F401

import six


class EditWhatsappProfile(object):

    swagger_types = {
        'email': 'str',
        'address': 'str',
        'description': 'str',
        'vertical': 'str',
        'websites': 'list'
    }
    attribute_map = {
        'email': 'email',
        'address': 'address',
        'description': 'description',
        'vertical': 'vertical',
        'websites': 'websites'
    }

    def __init__(self, email=None, address=None,
                 description=None, vertical=None, websites=None):

        self._email = None
        self._address = None
        self._description = None
        self._vertical = None
        self._websites = None

        self.email = email
        self.address = address
        self.description = description
        self.vertical = vertical
        self.websites = websites

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def vertical(self):
        return self._vertical

    @vertical.setter
    def vertical(self, vertical):
        self._vertical = vertical

    @property
    def websites(self):
        return self._websites

    @websites.setter
    def websites(self, websites):
        self._websites = websites

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
        if issubclass(EditWhatsappProfile, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, EditWhatsappProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
