# coding: utf-8

"""
    karix api

    # Overview  Karix API lets you interact with the Karix platform using an omnichannel messaging API. It also allows you to query your account, set up webhooks and buy phone numbers.  # API and Clients Versioning  Karix APIs are versioned using the format vX.Y where X is the major version number and Y is minor. All minor version releases are backwards compatible but major releases are not, please be careful when upgrading.  Version header `api-version` is used by Karix platform to determine the version of the API request. To use Karix API v2 you can send `api-version` as `\"2.0\"`.  If an API request does not contain `api-version` header then Karix platform uses the pinned API version of the account as the default verison. Your account defaults to the latest API version release at the time of signup. You can check the pinned API version form the [dashboard](https://cloud.karix.io/dashboard).  Karix also provides Helper Libraries for all major languages. Release versions of these libraries correspond to their API Version supported. Client version vX.Y.Z supports API version vX.Y. Helper libraries are configured to send `api-version` header based on the library version. When using official Karix helper libraries, you dont need to concern yourself with pinned version. Using helper library of latest version will give you access to latest features.  # Supported Channels  Karix omnichannel messaging API supports the following channels:   - sms   - whatsapp  ## SMS Channel To send a message to one or more destinations over SMS channel set `channel` to `sms` in the [Messaging API](#operation/sendMessage).  In trial mode, your account can only send messages to numbers within the sandbox.  ## Whatsapp Channel To send a message to a destination over WhatsApp channel set `channel` to `whatsapp` in the [Messaging API](#operation/sendMessage).  Currently WhatsApp channel can only be used from within the sandbox. Contact [support](mailto:support@karix.io) for an early access outside the sandbox.  Any messages you initiate over WhatsApp to end users must conform to a template configured in WhatsApp. These messages are called \"Notification Messages\". Currently only text messages can be sent as Notification Messages.  Any responses you receive from end users and all replies you send within 24 hours of the last received response are called \"Conversation Messages\".  When using the sandbox for testing and development purposes, we have provided for the following pre-approved templates for \"Notification Messages\":    - Your order * has been dispatched. Please expect delivery by *   - OTP requested by you on * is *   - Thank you for your payment of * * on *. Your transaction ID is *  You can replace `*` with any text of your choice.  Both Notification and Conversation messages are priced differently, please refer to the [pricing page](http://karix.io/messaging/pricing/) for more details.  # Common Request Structures  All Karix APIs follow a common REST format with the following resources:   - account   - message   - webhook   - number  ## Creating a resource To create a resource send a `POST` request with the desired parameters in a JSON object to `/<resource>/` url. A successful response will contain the details of the single resource created with HTTP status code `201 Created`. Note: An exception to this is the `Create Message` API which is a bulk API and returns       a list of message records.  ## Fetching a resource To fetch a resource by its Unique ID send a `GET` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will contain the details of the single resource fetched with HTTP status code `200 OK`  ## Editing a resource To edit certain parameters of a resource send a `PATCH` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource, with a JSON object containing only the parameters which need to be updated. Edit resource APIs generally have no required parameters. A successful response will contain all the details of the single resource after editing.  ## Deleting a resource To delete a resource send a `DELETE` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will return HTTP status code `204 No Content` with no body.  ## Fetching a list of resources To fetch a list of resources send a `GET` request to `/<resource>/` with filters as GET parameters. A successful response will contain a list of filtered paginated objects with HTTP status code `200 OK`.  ### Pagination Pagination for list APIs are controlled using GET parameters:   - `limit`: Number of objects to be returned   - `offset`: Number of objects to skip before collecting the output list.  # Common Response Structures  All Karix APIs follow a common respose structure.  ## Success Responses  ### Single Resource Response  Responses returning a single object will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | data          |               | Details of the object                     |  ### List Resource Response  Responses returning a list of objects will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | |               | previous      | Link to the previous page of the list     | |               | next          | Link to the next page of the list         | |               | total         | Total number of objects over all pages    | | objects       |               | List of objects with details              |  ## Error Responses  ### Validation Error Response  Responses for requests which failed due to validation errors will have the follwing keys: | Key           | Child Key     | Description                                | |:------------- |:------------- |:------------------------------------------ | | meta          |               | Meta Details about request and response    | |               | request_uuid  | Unique request identifier                  | | error         |               | Details for the error                      | |               | message       | Error message                              | |               | param         | (Optional) parameter this error relates to |  Validation error responses will return HTTP Status Code `400 Bad Request`  ### Insufficient Balance Response  Some requests will require to consume account credits. In case of insufficient balance the following keys will be returned: | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | error         |               | Details for the error                     | |               | message       | `Insufficient Balance`                    |  Insufficient balance response will return HTTP Status Code `402 Payment Required`  # Events and Webhooks  All asynchronous events generated by Karix platform follow a common structure:  | Key           | Child Key     | Description                                 | |:------------- |:------------- |:------------------------------------------- | | uid           |               | Alphanumeric unique ID of the event         | | api_version   |               | 2.0                                         | | type          |               | Type of the event.                          | | data          |               | Details of the object attached to the event |  Currently implemented event types are:   - `message`: These events are generated when a message is created or       its status is changed. When event `type` is `message` the `data`       parameter contains the Message object (check out the response.data of       [Get Message](#operation/getMessageById) API).     - For outbound messages, `message` events are sent to `events_url` parameter of       [Send Message](#operation/sendMessage) API     - For inbound messages, `message` events are sent to the webhook attached       to the phone number resource using [Edit Number](#tag/Number) API     - For inbound messages to whatsapp sandbox, `message` events are sent to       Webhook URL set on the [Dashboard](https://cloud.karix.io/dashboard/#whatsapp-demo).   # noqa: E501

    OpenAPI spec version: 2.0
    Contact: support@karix.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MessageChannelDetailsSms(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mobile_country_code': 'str',
        'mobile_network_code': 'str',
        'rate': 'str',
        'parts': 'int'
    }

    attribute_map = {
        'mobile_country_code': 'mobile_country_code',
        'mobile_network_code': 'mobile_network_code',
        'rate': 'rate',
        'parts': 'parts'
    }

    def __init__(self, mobile_country_code=None, mobile_network_code=None, rate=None, parts=None):  # noqa: E501
        """MessageChannelDetailsSms - a model defined in Swagger"""  # noqa: E501

        self._mobile_country_code = None
        self._mobile_network_code = None
        self._rate = None
        self._parts = None
        self.discriminator = None

        self.mobile_country_code = mobile_country_code
        self.mobile_network_code = mobile_network_code
        self.rate = rate
        self.parts = parts

    @property
    def mobile_country_code(self):
        """Gets the mobile_country_code of this MessageChannelDetailsSms.  # noqa: E501

        Mobile Country Code of the destination number. Refer to [Wikipedia: Mobile country code](https://en.wikipedia.org/wiki/Mobile_country_code)   # noqa: E501

        :return: The mobile_country_code of this MessageChannelDetailsSms.  # noqa: E501
        :rtype: str
        """
        return self._mobile_country_code

    @mobile_country_code.setter
    def mobile_country_code(self, mobile_country_code):
        """Sets the mobile_country_code of this MessageChannelDetailsSms.

        Mobile Country Code of the destination number. Refer to [Wikipedia: Mobile country code](https://en.wikipedia.org/wiki/Mobile_country_code)   # noqa: E501

        :param mobile_country_code: The mobile_country_code of this MessageChannelDetailsSms.  # noqa: E501
        :type: str
        """
        if mobile_country_code is None:
            raise ValueError("Invalid value for `mobile_country_code`, must not be `None`")  # noqa: E501

        self._mobile_country_code = mobile_country_code

    @property
    def mobile_network_code(self):
        """Gets the mobile_network_code of this MessageChannelDetailsSms.  # noqa: E501

        Mobile Network Code of the destination number. Refer to [Wikipedia: Mobile country code](https://en.wikipedia.org/wiki/Mobile_country_code)   # noqa: E501

        :return: The mobile_network_code of this MessageChannelDetailsSms.  # noqa: E501
        :rtype: str
        """
        return self._mobile_network_code

    @mobile_network_code.setter
    def mobile_network_code(self, mobile_network_code):
        """Sets the mobile_network_code of this MessageChannelDetailsSms.

        Mobile Network Code of the destination number. Refer to [Wikipedia: Mobile country code](https://en.wikipedia.org/wiki/Mobile_country_code)   # noqa: E501

        :param mobile_network_code: The mobile_network_code of this MessageChannelDetailsSms.  # noqa: E501
        :type: str
        """
        if mobile_network_code is None:
            raise ValueError("Invalid value for `mobile_network_code`, must not be `None`")  # noqa: E501

        self._mobile_network_code = mobile_network_code

    @property
    def rate(self):
        """Gets the rate of this MessageChannelDetailsSms.  # noqa: E501

        Cost per part of this message. Refer to [`text`](#/definitions/Message/properties/content/text)   # noqa: E501

        :return: The rate of this MessageChannelDetailsSms.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this MessageChannelDetailsSms.

        Cost per part of this message. Refer to [`text`](#/definitions/Message/properties/content/text)   # noqa: E501

        :param rate: The rate of this MessageChannelDetailsSms.  # noqa: E501
        :type: str
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

    @property
    def parts(self):
        """Gets the parts of this MessageChannelDetailsSms.  # noqa: E501

        Number of parts to the message if the message was too long Refer to [`text`](#/definitions/Message/properties/text)   # noqa: E501

        :return: The parts of this MessageChannelDetailsSms.  # noqa: E501
        :rtype: int
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this MessageChannelDetailsSms.

        Number of parts to the message if the message was too long Refer to [`text`](#/definitions/Message/properties/text)   # noqa: E501

        :param parts: The parts of this MessageChannelDetailsSms.  # noqa: E501
        :type: int
        """
        if parts is None:
            raise ValueError("Invalid value for `parts`, must not be `None`")  # noqa: E501

        self._parts = parts

    def to_dict(self):
        """Returns the model properties as a dict"""
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
        if issubclass(MessageChannelDetailsSms, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MessageChannelDetailsSms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other