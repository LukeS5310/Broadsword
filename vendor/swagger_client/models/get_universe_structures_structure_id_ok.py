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


class GetUniverseStructuresStructureIdOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, position=None, solar_system_id=None, type_id=None):
        """
        GetUniverseStructuresStructureIdOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'position': 'GetUniverseStructuresStructureIdPosition',
            'solar_system_id': 'int',
            'type_id': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'position': 'position',
            'solar_system_id': 'solar_system_id',
            'type_id': 'type_id'
        }

        self._name = name
        self._position = position
        self._solar_system_id = solar_system_id
        self._type_id = type_id

    @property
    def name(self):
        """
        Gets the name of this GetUniverseStructuresStructureIdOk.
        The full name of the structure

        :return: The name of this GetUniverseStructuresStructureIdOk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetUniverseStructuresStructureIdOk.
        The full name of the structure

        :param name: The name of this GetUniverseStructuresStructureIdOk.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def position(self):
        """
        Gets the position of this GetUniverseStructuresStructureIdOk.

        :return: The position of this GetUniverseStructuresStructureIdOk.
        :rtype: GetUniverseStructuresStructureIdPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this GetUniverseStructuresStructureIdOk.

        :param position: The position of this GetUniverseStructuresStructureIdOk.
        :type: GetUniverseStructuresStructureIdPosition
        """

        self._position = position

    @property
    def solar_system_id(self):
        """
        Gets the solar_system_id of this GetUniverseStructuresStructureIdOk.
        solar_system_id integer

        :return: The solar_system_id of this GetUniverseStructuresStructureIdOk.
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """
        Sets the solar_system_id of this GetUniverseStructuresStructureIdOk.
        solar_system_id integer

        :param solar_system_id: The solar_system_id of this GetUniverseStructuresStructureIdOk.
        :type: int
        """
        if solar_system_id is None:
            raise ValueError("Invalid value for `solar_system_id`, must not be `None`")

        self._solar_system_id = solar_system_id

    @property
    def type_id(self):
        """
        Gets the type_id of this GetUniverseStructuresStructureIdOk.
        type_id integer

        :return: The type_id of this GetUniverseStructuresStructureIdOk.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this GetUniverseStructuresStructureIdOk.
        type_id integer

        :param type_id: The type_id of this GetUniverseStructuresStructureIdOk.
        :type: int
        """

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
        if not isinstance(other, GetUniverseStructuresStructureIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
