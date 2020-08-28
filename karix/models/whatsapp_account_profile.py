import pprint
import re  # noqa: F401

import six

from karix.models.whatsapp_account_error import WhatsappAccountError  # noqa: F401,E501


class WhatsappAccountProfile(object):

    swagger_types = {
        'number': 'str',
        'email': 'str',
        'address': 'str',
        'description': 'str',
        'vertical': 'str',
        'websites': 'object'
    }
    attribute_map = {
        'number': 'number',
        'email': 'email',
        'address': 'address',
        'description': 'description',
        'vertical': 'vertical',
        'websites': 'websites'
    }

    def __init__(self, number=None, email=None, address=None,
                 description=None, vertical=None, websites=None):

        self.number = None
        self.email = None
        self.address = None
        self.description = None
        self.vertical = None
        self.websites = None

        if number is not None:
            self.number = number
        if email is not None:
            self.email = email
        if address is not None:
            self.address = address
        if description is not None:
            self.description = description
        if vertical is not None:
            self.vertical = vertical
        if websites is not None:
            self.websites = websites

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

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
        if issubclass(WhatsappAccountProfile, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WhatsappAccountProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
