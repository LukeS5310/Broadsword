# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetFwLeaderboardsCharactersLastWeek1(object):
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
        'character_id': 'int',
        'amount': 'int'
    }

    attribute_map = {
        'character_id': 'character_id',
        'amount': 'amount'
    }

    def __init__(self, character_id=None, amount=None):
        """
        GetFwLeaderboardsCharactersLastWeek1 - a model defined in Swagger
        """

        self._character_id = None
        self._amount = None
        self.discriminator = None

        if character_id is not None:
          self.character_id = character_id
        if amount is not None:
          self.amount = amount

    @property
    def character_id(self):
        """
        Gets the character_id of this GetFwLeaderboardsCharactersLastWeek1.
        character_id integer

        :return: The character_id of this GetFwLeaderboardsCharactersLastWeek1.
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """
        Sets the character_id of this GetFwLeaderboardsCharactersLastWeek1.
        character_id integer

        :param character_id: The character_id of this GetFwLeaderboardsCharactersLastWeek1.
        :type: int
        """

        self._character_id = character_id

    @property
    def amount(self):
        """
        Gets the amount of this GetFwLeaderboardsCharactersLastWeek1.
        Amount of victory points

        :return: The amount of this GetFwLeaderboardsCharactersLastWeek1.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this GetFwLeaderboardsCharactersLastWeek1.
        Amount of victory points

        :param amount: The amount of this GetFwLeaderboardsCharactersLastWeek1.
        :type: int
        """

        self._amount = amount

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
        if not isinstance(other, GetFwLeaderboardsCharactersLastWeek1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
