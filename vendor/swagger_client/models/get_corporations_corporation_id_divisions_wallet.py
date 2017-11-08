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


class GetCorporationsCorporationIdDivisionsWallet(object):
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
        'division': 'int',
        'name': 'str'
    }

    attribute_map = {
        'division': 'division',
        'name': 'name'
    }

    def __init__(self, division=None, name=None):
        """
        GetCorporationsCorporationIdDivisionsWallet - a model defined in Swagger
        """

        self._division = None
        self._name = None
        self.discriminator = None

        if division is not None:
          self.division = division
        if name is not None:
          self.name = name

    @property
    def division(self):
        """
        Gets the division of this GetCorporationsCorporationIdDivisionsWallet.
        division integer

        :return: The division of this GetCorporationsCorporationIdDivisionsWallet.
        :rtype: int
        """
        return self._division

    @division.setter
    def division(self, division):
        """
        Sets the division of this GetCorporationsCorporationIdDivisionsWallet.
        division integer

        :param division: The division of this GetCorporationsCorporationIdDivisionsWallet.
        :type: int
        """
        if division is not None and division > 7:
            raise ValueError("Invalid value for `division`, must be a value less than or equal to `7`")
        if division is not None and division < 1:
            raise ValueError("Invalid value for `division`, must be a value greater than or equal to `1`")

        self._division = division

    @property
    def name(self):
        """
        Gets the name of this GetCorporationsCorporationIdDivisionsWallet.
        name string

        :return: The name of this GetCorporationsCorporationIdDivisionsWallet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetCorporationsCorporationIdDivisionsWallet.
        name string

        :param name: The name of this GetCorporationsCorporationIdDivisionsWallet.
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")

        self._name = name

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
        if not isinstance(other, GetCorporationsCorporationIdDivisionsWallet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
