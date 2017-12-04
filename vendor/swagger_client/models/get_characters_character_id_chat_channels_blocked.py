# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.7.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetCharactersCharacterIdChatChannelsBlocked(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'accessor_id': 'int',
        'accessor_type': 'str',
        'reason': 'str',
        'end_at': 'datetime'
    }

    attribute_map = {
        'accessor_id': 'accessor_id',
        'accessor_type': 'accessor_type',
        'reason': 'reason',
        'end_at': 'end_at'
    }

    def __init__(self, accessor_id=None, accessor_type=None, reason=None, end_at=None):
        """
        GetCharactersCharacterIdChatChannelsBlocked - a model defined in Swagger
        """

        self._accessor_id = None
        self._accessor_type = None
        self._reason = None
        self._end_at = None
        self.discriminator = None

        self.accessor_id = accessor_id
        self.accessor_type = accessor_type
        if reason is not None:
          self.reason = reason
        if end_at is not None:
          self.end_at = end_at

    @property
    def accessor_id(self):
        """
        Gets the accessor_id of this GetCharactersCharacterIdChatChannelsBlocked.
        ID of a blocked channel member

        :return: The accessor_id of this GetCharactersCharacterIdChatChannelsBlocked.
        :rtype: int
        """
        return self._accessor_id

    @accessor_id.setter
    def accessor_id(self, accessor_id):
        """
        Sets the accessor_id of this GetCharactersCharacterIdChatChannelsBlocked.
        ID of a blocked channel member

        :param accessor_id: The accessor_id of this GetCharactersCharacterIdChatChannelsBlocked.
        :type: int
        """
        if accessor_id is None:
            raise ValueError("Invalid value for `accessor_id`, must not be `None`")

        self._accessor_id = accessor_id

    @property
    def accessor_type(self):
        """
        Gets the accessor_type of this GetCharactersCharacterIdChatChannelsBlocked.
        accessor_type string

        :return: The accessor_type of this GetCharactersCharacterIdChatChannelsBlocked.
        :rtype: str
        """
        return self._accessor_type

    @accessor_type.setter
    def accessor_type(self, accessor_type):
        """
        Sets the accessor_type of this GetCharactersCharacterIdChatChannelsBlocked.
        accessor_type string

        :param accessor_type: The accessor_type of this GetCharactersCharacterIdChatChannelsBlocked.
        :type: str
        """
        if accessor_type is None:
            raise ValueError("Invalid value for `accessor_type`, must not be `None`")
        allowed_values = ["character", "corporation", "alliance"]
        if accessor_type not in allowed_values:
            raise ValueError(
                "Invalid value for `accessor_type` ({0}), must be one of {1}"
                .format(accessor_type, allowed_values)
            )

        self._accessor_type = accessor_type

    @property
    def reason(self):
        """
        Gets the reason of this GetCharactersCharacterIdChatChannelsBlocked.
        Reason this accessor is blocked

        :return: The reason of this GetCharactersCharacterIdChatChannelsBlocked.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this GetCharactersCharacterIdChatChannelsBlocked.
        Reason this accessor is blocked

        :param reason: The reason of this GetCharactersCharacterIdChatChannelsBlocked.
        :type: str
        """

        self._reason = reason

    @property
    def end_at(self):
        """
        Gets the end_at of this GetCharactersCharacterIdChatChannelsBlocked.
        Time at which this accessor will no longer be blocked

        :return: The end_at of this GetCharactersCharacterIdChatChannelsBlocked.
        :rtype: datetime
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """
        Sets the end_at of this GetCharactersCharacterIdChatChannelsBlocked.
        Time at which this accessor will no longer be blocked

        :param end_at: The end_at of this GetCharactersCharacterIdChatChannelsBlocked.
        :type: datetime
        """

        self._end_at = end_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GetCharactersCharacterIdChatChannelsBlocked):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
