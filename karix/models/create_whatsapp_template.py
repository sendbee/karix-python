import pprint
import re  # noqa: F401

import six


class CreateWhatsappTemplate(object):

    swagger_types = {
        'uid': 'str',
        'category': 'str',
        'whatsapp_account_uid': 'str',
        'name': 'str',
        'language_code': 'str',
        'attachment': 'str',
        'text': 'str'
    }
    attribute_map = {
        'uid': 'uid',
        'category': 'category',
        'whatsapp_account_uid': 'whatsapp_account_uid',
        'name': 'name',
        'language_code': 'language_code',
        'attachment': 'attachment',
        'text': 'text'
    }

    def __init__(self, uid=None, category=None, whatsapp_account_uid=None,
                 name=None, language_code=None, attachment=None, text=None):

        self._uid = None
        self._category = None
        self._whatsapp_account_uid = None
        self._name = None
        self._language_code = None
        self._attachment = None
        self._text = None

        if uid is not None:
            self.uid = uid
        if category is not None:
            self.category = category
        if whatsapp_account_uid is not None:
            self.whatsapp_account_uid = whatsapp_account_uid
        if name is not None:
            self.name = name
        if language_code is not None:
            self.language_code = language_code

        self.attachment = attachment

        if text is not None:
            self.text = text

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        self._uid = uid

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @property
    def whatsapp_account_uid(self):
        return self._whatsapp_account_uid

    @whatsapp_account_uid.setter
    def whatsapp_account_uid(self, whatsapp_account_uid):
        self._whatsapp_account_uid = whatsapp_account_uid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def language_code(self):
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        self._language_code = language_code

    @property
    def attachment(self):
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        self._attachment = attachment

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
        if issubclass(CreateWhatsappTemplate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CreateWhatsappTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
