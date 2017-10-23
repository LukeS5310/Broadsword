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


class GetKillmailsKillmailIdKillmailHashItem1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, flag=None, item_type_id=None, items=None, quantity_destroyed=None, quantity_dropped=None, singleton=None):
        """
        GetKillmailsKillmailIdKillmailHashItem1 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'flag': 'int',
            'item_type_id': 'int',
            'items': 'list[GetKillmailsKillmailIdKillmailHashItem]',
            'quantity_destroyed': 'int',
            'quantity_dropped': 'int',
            'singleton': 'int'
        }

        self.attribute_map = {
            'flag': 'flag',
            'item_type_id': 'item_type_id',
            'items': 'items',
            'quantity_destroyed': 'quantity_destroyed',
            'quantity_dropped': 'quantity_dropped',
            'singleton': 'singleton'
        }

        self._flag = flag
        self._item_type_id = item_type_id
        self._items = items
        self._quantity_destroyed = quantity_destroyed
        self._quantity_dropped = quantity_dropped
        self._singleton = singleton

    @property
    def flag(self):
        """
        Gets the flag of this GetKillmailsKillmailIdKillmailHashItem1.
        Flag for the location of the item 

        :return: The flag of this GetKillmailsKillmailIdKillmailHashItem1.
        :rtype: int
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """
        Sets the flag of this GetKillmailsKillmailIdKillmailHashItem1.
        Flag for the location of the item 

        :param flag: The flag of this GetKillmailsKillmailIdKillmailHashItem1.
        :type: int
        """
        if flag is None:
            raise ValueError("Invalid value for `flag`, must not be `None`")

        self._flag = flag

    @property
    def item_type_id(self):
        """
        Gets the item_type_id of this GetKillmailsKillmailIdKillmailHashItem1.
        item_type_id integer

        :return: The item_type_id of this GetKillmailsKillmailIdKillmailHashItem1.
        :rtype: int
        """
        return self._item_type_id

    @item_type_id.setter
    def item_type_id(self, item_type_id):
        """
        Sets the item_type_id of this GetKillmailsKillmailIdKillmailHashItem1.
        item_type_id integer

        :param item_type_id: The item_type_id of this GetKillmailsKillmailIdKillmailHashItem1.
        :type: int
        """
        if item_type_id is None:
            raise ValueError("Invalid value for `item_type_id`, must not be `None`")

        self._item_type_id = item_type_id

    @property
    def items(self):
        """
        Gets the items of this GetKillmailsKillmailIdKillmailHashItem1.
        items array

        :return: The items of this GetKillmailsKillmailIdKillmailHashItem1.
        :rtype: list[GetKillmailsKillmailIdKillmailHashItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this GetKillmailsKillmailIdKillmailHashItem1.
        items array

        :param items: The items of this GetKillmailsKillmailIdKillmailHashItem1.
        :type: list[GetKillmailsKillmailIdKillmailHashItem]
        """

        self._items = items

    @property
    def quantity_destroyed(self):
        """
        Gets the quantity_destroyed of this GetKillmailsKillmailIdKillmailHashItem1.
        How many of the item were destroyed if any 

        :return: The quantity_destroyed of this GetKillmailsKillmailIdKillmailHashItem1.
        :rtype: int
        """
        return self._quantity_destroyed

    @quantity_destroyed.setter
    def quantity_destroyed(self, quantity_destroyed):
        """
        Sets the quantity_destroyed of this GetKillmailsKillmailIdKillmailHashItem1.
        How many of the item were destroyed if any 

        :param quantity_destroyed: The quantity_destroyed of this GetKillmailsKillmailIdKillmailHashItem1.
        :type: int
        """

        self._quantity_destroyed = quantity_destroyed

    @property
    def quantity_dropped(self):
        """
        Gets the quantity_dropped of this GetKillmailsKillmailIdKillmailHashItem1.
        How many of the item were dropped if any 

        :return: The quantity_dropped of this GetKillmailsKillmailIdKillmailHashItem1.
        :rtype: int
        """
        return self._quantity_dropped

    @quantity_dropped.setter
    def quantity_dropped(self, quantity_dropped):
        """
        Sets the quantity_dropped of this GetKillmailsKillmailIdKillmailHashItem1.
        How many of the item were dropped if any 

        :param quantity_dropped: The quantity_dropped of this GetKillmailsKillmailIdKillmailHashItem1.
        :type: int
        """

        self._quantity_dropped = quantity_dropped

    @property
    def singleton(self):
        """
        Gets the singleton of this GetKillmailsKillmailIdKillmailHashItem1.
        singleton integer

        :return: The singleton of this GetKillmailsKillmailIdKillmailHashItem1.
        :rtype: int
        """
        return self._singleton

    @singleton.setter
    def singleton(self, singleton):
        """
        Sets the singleton of this GetKillmailsKillmailIdKillmailHashItem1.
        singleton integer

        :param singleton: The singleton of this GetKillmailsKillmailIdKillmailHashItem1.
        :type: int
        """
        if singleton is None:
            raise ValueError("Invalid value for `singleton`, must not be `None`")

        self._singleton = singleton

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
        if not isinstance(other, GetKillmailsKillmailIdKillmailHashItem1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
