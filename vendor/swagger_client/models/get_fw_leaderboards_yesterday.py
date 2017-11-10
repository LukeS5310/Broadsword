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


class GetFwLeaderboardsYesterday(object):
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
        'faction_id': 'int',
        'amount': 'int'
    }

    attribute_map = {
        'faction_id': 'faction_id',
        'amount': 'amount'
    }

    def __init__(self, faction_id=None, amount=None):
        """
        GetFwLeaderboardsYesterday - a model defined in Swagger
        """

        self._faction_id = None
        self._amount = None
        self.discriminator = None

        if faction_id is not None:
          self.faction_id = faction_id
        if amount is not None:
          self.amount = amount

    @property
    def faction_id(self):
        """
        Gets the faction_id of this GetFwLeaderboardsYesterday.
        faction_id integer

        :return: The faction_id of this GetFwLeaderboardsYesterday.
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """
        Sets the faction_id of this GetFwLeaderboardsYesterday.
        faction_id integer

        :param faction_id: The faction_id of this GetFwLeaderboardsYesterday.
        :type: int
        """

        self._faction_id = faction_id

    @property
    def amount(self):
        """
        Gets the amount of this GetFwLeaderboardsYesterday.
        Amount of kills

        :return: The amount of this GetFwLeaderboardsYesterday.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this GetFwLeaderboardsYesterday.
        Amount of kills

        :param amount: The amount of this GetFwLeaderboardsYesterday.
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
        if not isinstance(other, GetFwLeaderboardsYesterday):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
