# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.6.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetInsurancePricesLevel(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cost=None, name=None, payout=None):
        """
        GetInsurancePricesLevel - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cost': 'float',
            'name': 'str',
            'payout': 'float'
        }

        self.attribute_map = {
            'cost': 'cost',
            'name': 'name',
            'payout': 'payout'
        }

        self._cost = cost
        self._name = name
        self._payout = payout

    @property
    def cost(self):
        """
        Gets the cost of this GetInsurancePricesLevel.
        cost number

        :return: The cost of this GetInsurancePricesLevel.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this GetInsurancePricesLevel.
        cost number

        :param cost: The cost of this GetInsurancePricesLevel.
        :type: float
        """
        if cost is None:
            raise ValueError("Invalid value for `cost`, must not be `None`")

        self._cost = cost

    @property
    def name(self):
        """
        Gets the name of this GetInsurancePricesLevel.
        Localized insurance level

        :return: The name of this GetInsurancePricesLevel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetInsurancePricesLevel.
        Localized insurance level

        :param name: The name of this GetInsurancePricesLevel.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def payout(self):
        """
        Gets the payout of this GetInsurancePricesLevel.
        payout number

        :return: The payout of this GetInsurancePricesLevel.
        :rtype: float
        """
        return self._payout

    @payout.setter
    def payout(self, payout):
        """
        Sets the payout of this GetInsurancePricesLevel.
        payout number

        :param payout: The payout of this GetInsurancePricesLevel.
        :type: float
        """
        if payout is None:
            raise ValueError("Invalid value for `payout`, must not be `None`")

        self._payout = payout

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
        if not isinstance(other, GetInsurancePricesLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
