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


class GetLoyaltyStoresCorporationIdOffersRequiredItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, quantity=None, type_id=None):
        """
        GetLoyaltyStoresCorporationIdOffersRequiredItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'quantity': 'int',
            'type_id': 'int'
        }

        self.attribute_map = {
            'quantity': 'quantity',
            'type_id': 'type_id'
        }

        self._quantity = quantity
        self._type_id = type_id

    @property
    def quantity(self):
        """
        Gets the quantity of this GetLoyaltyStoresCorporationIdOffersRequiredItem.
        quantity integer

        :return: The quantity of this GetLoyaltyStoresCorporationIdOffersRequiredItem.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this GetLoyaltyStoresCorporationIdOffersRequiredItem.
        quantity integer

        :param quantity: The quantity of this GetLoyaltyStoresCorporationIdOffersRequiredItem.
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity

    @property
    def type_id(self):
        """
        Gets the type_id of this GetLoyaltyStoresCorporationIdOffersRequiredItem.
        type_id integer

        :return: The type_id of this GetLoyaltyStoresCorporationIdOffersRequiredItem.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this GetLoyaltyStoresCorporationIdOffersRequiredItem.
        type_id integer

        :param type_id: The type_id of this GetLoyaltyStoresCorporationIdOffersRequiredItem.
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")

        self._type_id = type_id

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
        if not isinstance(other, GetLoyaltyStoresCorporationIdOffersRequiredItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
