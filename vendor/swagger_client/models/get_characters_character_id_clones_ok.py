# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetCharactersCharacterIdClonesOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, home_location=None, jump_clones=None, last_jump_date=None):
        """
        GetCharactersCharacterIdClonesOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'home_location': 'GetCharactersCharacterIdClonesHomeLocation',
            'jump_clones': 'list[GetCharactersCharacterIdClonesJumpClone]',
            'last_jump_date': 'datetime'
        }

        self.attribute_map = {
            'home_location': 'home_location',
            'jump_clones': 'jump_clones',
            'last_jump_date': 'last_jump_date'
        }

        self._home_location = home_location
        self._jump_clones = jump_clones
        self._last_jump_date = last_jump_date

    @property
    def home_location(self):
        """
        Gets the home_location of this GetCharactersCharacterIdClonesOk.

        :return: The home_location of this GetCharactersCharacterIdClonesOk.
        :rtype: GetCharactersCharacterIdClonesHomeLocation
        """
        return self._home_location

    @home_location.setter
    def home_location(self, home_location):
        """
        Sets the home_location of this GetCharactersCharacterIdClonesOk.

        :param home_location: The home_location of this GetCharactersCharacterIdClonesOk.
        :type: GetCharactersCharacterIdClonesHomeLocation
        """

        self._home_location = home_location

    @property
    def jump_clones(self):
        """
        Gets the jump_clones of this GetCharactersCharacterIdClonesOk.
        jump_clones array

        :return: The jump_clones of this GetCharactersCharacterIdClonesOk.
        :rtype: list[GetCharactersCharacterIdClonesJumpClone]
        """
        return self._jump_clones

    @jump_clones.setter
    def jump_clones(self, jump_clones):
        """
        Sets the jump_clones of this GetCharactersCharacterIdClonesOk.
        jump_clones array

        :param jump_clones: The jump_clones of this GetCharactersCharacterIdClonesOk.
        :type: list[GetCharactersCharacterIdClonesJumpClone]
        """
        if jump_clones is None:
            raise ValueError("Invalid value for `jump_clones`, must not be `None`")

        self._jump_clones = jump_clones

    @property
    def last_jump_date(self):
        """
        Gets the last_jump_date of this GetCharactersCharacterIdClonesOk.
        last_jump_date string

        :return: The last_jump_date of this GetCharactersCharacterIdClonesOk.
        :rtype: datetime
        """
        return self._last_jump_date

    @last_jump_date.setter
    def last_jump_date(self, last_jump_date):
        """
        Sets the last_jump_date of this GetCharactersCharacterIdClonesOk.
        last_jump_date string

        :param last_jump_date: The last_jump_date of this GetCharactersCharacterIdClonesOk.
        :type: datetime
        """

        self._last_jump_date = last_jump_date

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
        if not isinstance(other, GetCharactersCharacterIdClonesOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
