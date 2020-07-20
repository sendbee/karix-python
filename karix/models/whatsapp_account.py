import pprint
import re  # noqa: F401

import six

from karix.models.whatsapp_account_error import WhatsappAccountError  # noqa: F401,E501


class WhatsappAccount(object):

    swagger_types = {
        'uid': 'str',
        'karix_account_uid': 'str',
        'name': 'str'
    }
    attribute_map = {
        'uid': 'uid',
        'karix_account_uid': 'karix_account_uid',
        'name': 'name'
    }

    def __init__(self, uid=None, karix_account_uid=None, name=None):

        self._uid = None
        self._karix_account_uid = None
        self._name = None

        if uid is not None:
            self.uid = uid
        if karix_account_uid is not None:
            self.karix_account_uid = karix_account_uid
        if name is not None:
            self.name = name

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        self._uid = uid

    @property
    def karix_account_uid(self):
        return self._karix_account_uid

    @karix_account_uid.setter
    def karix_account_uid(self, karix_account_uid):
        self._karix_account_uid = karix_account_uid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

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
        if issubclass(WhatsappAccount, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WhatsappAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
