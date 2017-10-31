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


class GetCharactersCharacterIdPlanetsPlanetIdLink(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, destination_pin_id=None, link_level=None, source_pin_id=None):
        """
        GetCharactersCharacterIdPlanetsPlanetIdLink - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'destination_pin_id': 'int',
            'link_level': 'int',
            'source_pin_id': 'int'
        }

        self.attribute_map = {
            'destination_pin_id': 'destination_pin_id',
            'link_level': 'link_level',
            'source_pin_id': 'source_pin_id'
        }

        self._destination_pin_id = destination_pin_id
        self._link_level = link_level
        self._source_pin_id = source_pin_id

    @property
    def destination_pin_id(self):
        """
        Gets the destination_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdLink.
        destination_pin_id integer

        :return: The destination_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdLink.
        :rtype: int
        """
        return self._destination_pin_id

    @destination_pin_id.setter
    def destination_pin_id(self, destination_pin_id):
        """
        Sets the destination_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdLink.
        destination_pin_id integer

        :param destination_pin_id: The destination_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdLink.
        :type: int
        """
        if destination_pin_id is None:
            raise ValueError("Invalid value for `destination_pin_id`, must not be `None`")

        self._destination_pin_id = destination_pin_id

    @property
    def link_level(self):
        """
        Gets the link_level of this GetCharactersCharacterIdPlanetsPlanetIdLink.
        link_level integer

        :return: The link_level of this GetCharactersCharacterIdPlanetsPlanetIdLink.
        :rtype: int
        """
        return self._link_level

    @link_level.setter
    def link_level(self, link_level):
        """
        Sets the link_level of this GetCharactersCharacterIdPlanetsPlanetIdLink.
        link_level integer

        :param link_level: The link_level of this GetCharactersCharacterIdPlanetsPlanetIdLink.
        :type: int
        """
        if link_level is None:
            raise ValueError("Invalid value for `link_level`, must not be `None`")
        if link_level is not None and link_level > 10:
            raise ValueError("Invalid value for `link_level`, must be a value less than or equal to `10`")
        if link_level is not None and link_level < 0:
            raise ValueError("Invalid value for `link_level`, must be a value greater than or equal to `0`")

        self._link_level = link_level

    @property
    def source_pin_id(self):
        """
        Gets the source_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdLink.
        source_pin_id integer

        :return: The source_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdLink.
        :rtype: int
        """
        return self._source_pin_id

    @source_pin_id.setter
    def source_pin_id(self, source_pin_id):
        """
        Sets the source_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdLink.
        source_pin_id integer

        :param source_pin_id: The source_pin_id of this GetCharactersCharacterIdPlanetsPlanetIdLink.
        :type: int
        """
        if source_pin_id is None:
            raise ValueError("Invalid value for `source_pin_id`, must not be `None`")

        self._source_pin_id = source_pin_id

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
        if not isinstance(other, GetCharactersCharacterIdPlanetsPlanetIdLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
