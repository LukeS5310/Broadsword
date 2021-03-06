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


class GetCharactersCharacterIdBookmarksTarget(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, coordinates=None, item=None, location_id=None):
        """
        GetCharactersCharacterIdBookmarksTarget - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'coordinates': 'GetCharactersCharacterIdBookmarksCoordinates',
            'item': 'GetCharactersCharacterIdBookmarksItem',
            'location_id': 'int'
        }

        self.attribute_map = {
            'coordinates': 'coordinates',
            'item': 'item',
            'location_id': 'location_id'
        }

        self._coordinates = coordinates
        self._item = item
        self._location_id = location_id

    @property
    def coordinates(self):
        """
        Gets the coordinates of this GetCharactersCharacterIdBookmarksTarget.

        :return: The coordinates of this GetCharactersCharacterIdBookmarksTarget.
        :rtype: GetCharactersCharacterIdBookmarksCoordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """
        Sets the coordinates of this GetCharactersCharacterIdBookmarksTarget.

        :param coordinates: The coordinates of this GetCharactersCharacterIdBookmarksTarget.
        :type: GetCharactersCharacterIdBookmarksCoordinates
        """

        self._coordinates = coordinates

    @property
    def item(self):
        """
        Gets the item of this GetCharactersCharacterIdBookmarksTarget.

        :return: The item of this GetCharactersCharacterIdBookmarksTarget.
        :rtype: GetCharactersCharacterIdBookmarksItem
        """
        return self._item

    @item.setter
    def item(self, item):
        """
        Sets the item of this GetCharactersCharacterIdBookmarksTarget.

        :param item: The item of this GetCharactersCharacterIdBookmarksTarget.
        :type: GetCharactersCharacterIdBookmarksItem
        """

        self._item = item

    @property
    def location_id(self):
        """
        Gets the location_id of this GetCharactersCharacterIdBookmarksTarget.
        location_id integer

        :return: The location_id of this GetCharactersCharacterIdBookmarksTarget.
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this GetCharactersCharacterIdBookmarksTarget.
        location_id integer

        :param location_id: The location_id of this GetCharactersCharacterIdBookmarksTarget.
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")

        self._location_id = location_id

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
        if not isinstance(other, GetCharactersCharacterIdBookmarksTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
