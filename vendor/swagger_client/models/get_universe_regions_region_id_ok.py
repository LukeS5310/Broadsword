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


class GetUniverseRegionsRegionIdOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, constellations=None, description=None, name=None, region_id=None):
        """
        GetUniverseRegionsRegionIdOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'constellations': 'list[int]',
            'description': 'str',
            'name': 'str',
            'region_id': 'int'
        }

        self.attribute_map = {
            'constellations': 'constellations',
            'description': 'description',
            'name': 'name',
            'region_id': 'region_id'
        }

        self._constellations = constellations
        self._description = description
        self._name = name
        self._region_id = region_id

    @property
    def constellations(self):
        """
        Gets the constellations of this GetUniverseRegionsRegionIdOk.
        constellations array

        :return: The constellations of this GetUniverseRegionsRegionIdOk.
        :rtype: list[int]
        """
        return self._constellations

    @constellations.setter
    def constellations(self, constellations):
        """
        Sets the constellations of this GetUniverseRegionsRegionIdOk.
        constellations array

        :param constellations: The constellations of this GetUniverseRegionsRegionIdOk.
        :type: list[int]
        """
        if constellations is None:
            raise ValueError("Invalid value for `constellations`, must not be `None`")

        self._constellations = constellations

    @property
    def description(self):
        """
        Gets the description of this GetUniverseRegionsRegionIdOk.
        description string

        :return: The description of this GetUniverseRegionsRegionIdOk.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GetUniverseRegionsRegionIdOk.
        description string

        :param description: The description of this GetUniverseRegionsRegionIdOk.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this GetUniverseRegionsRegionIdOk.
        name string

        :return: The name of this GetUniverseRegionsRegionIdOk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetUniverseRegionsRegionIdOk.
        name string

        :param name: The name of this GetUniverseRegionsRegionIdOk.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def region_id(self):
        """
        Gets the region_id of this GetUniverseRegionsRegionIdOk.
        region_id integer

        :return: The region_id of this GetUniverseRegionsRegionIdOk.
        :rtype: int
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this GetUniverseRegionsRegionIdOk.
        region_id integer

        :param region_id: The region_id of this GetUniverseRegionsRegionIdOk.
        :type: int
        """
        if region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")

        self._region_id = region_id

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
        if not isinstance(other, GetUniverseRegionsRegionIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
