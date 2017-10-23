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


class GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cycle_time=None, head_radius=None, heads=None, product_type_id=None, qty_per_cycle=None):
        """
        GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cycle_time': 'int',
            'head_radius': 'float',
            'heads': 'list[GetCharactersCharacterIdPlanetsPlanetIdHead]',
            'product_type_id': 'int',
            'qty_per_cycle': 'int'
        }

        self.attribute_map = {
            'cycle_time': 'cycle_time',
            'head_radius': 'head_radius',
            'heads': 'heads',
            'product_type_id': 'product_type_id',
            'qty_per_cycle': 'qty_per_cycle'
        }

        self._cycle_time = cycle_time
        self._head_radius = head_radius
        self._heads = heads
        self._product_type_id = product_type_id
        self._qty_per_cycle = qty_per_cycle

    @property
    def cycle_time(self):
        """
        Gets the cycle_time of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        in seconds

        :return: The cycle_time of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        :rtype: int
        """
        return self._cycle_time

    @cycle_time.setter
    def cycle_time(self, cycle_time):
        """
        Sets the cycle_time of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        in seconds

        :param cycle_time: The cycle_time of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        :type: int
        """

        self._cycle_time = cycle_time

    @property
    def head_radius(self):
        """
        Gets the head_radius of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        head_radius number

        :return: The head_radius of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        :rtype: float
        """
        return self._head_radius

    @head_radius.setter
    def head_radius(self, head_radius):
        """
        Sets the head_radius of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        head_radius number

        :param head_radius: The head_radius of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        :type: float
        """

        self._head_radius = head_radius

    @property
    def heads(self):
        """
        Gets the heads of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        heads array

        :return: The heads of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        :rtype: list[GetCharactersCharacterIdPlanetsPlanetIdHead]
        """
        return self._heads

    @heads.setter
    def heads(self, heads):
        """
        Sets the heads of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        heads array

        :param heads: The heads of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        :type: list[GetCharactersCharacterIdPlanetsPlanetIdHead]
        """
        if heads is None:
            raise ValueError("Invalid value for `heads`, must not be `None`")

        self._heads = heads

    @property
    def product_type_id(self):
        """
        Gets the product_type_id of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        product_type_id integer

        :return: The product_type_id of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        :rtype: int
        """
        return self._product_type_id

    @product_type_id.setter
    def product_type_id(self, product_type_id):
        """
        Sets the product_type_id of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        product_type_id integer

        :param product_type_id: The product_type_id of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        :type: int
        """

        self._product_type_id = product_type_id

    @property
    def qty_per_cycle(self):
        """
        Gets the qty_per_cycle of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        qty_per_cycle integer

        :return: The qty_per_cycle of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        :rtype: int
        """
        return self._qty_per_cycle

    @qty_per_cycle.setter
    def qty_per_cycle(self, qty_per_cycle):
        """
        Sets the qty_per_cycle of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        qty_per_cycle integer

        :param qty_per_cycle: The qty_per_cycle of this GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails.
        :type: int
        """

        self._qty_per_cycle = qty_per_cycle

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
        if not isinstance(other, GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
