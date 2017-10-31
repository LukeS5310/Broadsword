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


class GetCharactersCharacterIdMedalsGraphic(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, color=None, graphic=None, layer=None, part=None):
        """
        GetCharactersCharacterIdMedalsGraphic - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'color': 'int',
            'graphic': 'str',
            'layer': 'int',
            'part': 'int'
        }

        self.attribute_map = {
            'color': 'color',
            'graphic': 'graphic',
            'layer': 'layer',
            'part': 'part'
        }

        self._color = color
        self._graphic = graphic
        self._layer = layer
        self._part = part

    @property
    def color(self):
        """
        Gets the color of this GetCharactersCharacterIdMedalsGraphic.
        color integer

        :return: The color of this GetCharactersCharacterIdMedalsGraphic.
        :rtype: int
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this GetCharactersCharacterIdMedalsGraphic.
        color integer

        :param color: The color of this GetCharactersCharacterIdMedalsGraphic.
        :type: int
        """

        self._color = color

    @property
    def graphic(self):
        """
        Gets the graphic of this GetCharactersCharacterIdMedalsGraphic.
        graphic string

        :return: The graphic of this GetCharactersCharacterIdMedalsGraphic.
        :rtype: str
        """
        return self._graphic

    @graphic.setter
    def graphic(self, graphic):
        """
        Sets the graphic of this GetCharactersCharacterIdMedalsGraphic.
        graphic string

        :param graphic: The graphic of this GetCharactersCharacterIdMedalsGraphic.
        :type: str
        """
        if graphic is None:
            raise ValueError("Invalid value for `graphic`, must not be `None`")

        self._graphic = graphic

    @property
    def layer(self):
        """
        Gets the layer of this GetCharactersCharacterIdMedalsGraphic.
        layer integer

        :return: The layer of this GetCharactersCharacterIdMedalsGraphic.
        :rtype: int
        """
        return self._layer

    @layer.setter
    def layer(self, layer):
        """
        Sets the layer of this GetCharactersCharacterIdMedalsGraphic.
        layer integer

        :param layer: The layer of this GetCharactersCharacterIdMedalsGraphic.
        :type: int
        """
        if layer is None:
            raise ValueError("Invalid value for `layer`, must not be `None`")

        self._layer = layer

    @property
    def part(self):
        """
        Gets the part of this GetCharactersCharacterIdMedalsGraphic.
        part integer

        :return: The part of this GetCharactersCharacterIdMedalsGraphic.
        :rtype: int
        """
        return self._part

    @part.setter
    def part(self, part):
        """
        Sets the part of this GetCharactersCharacterIdMedalsGraphic.
        part integer

        :param part: The part of this GetCharactersCharacterIdMedalsGraphic.
        :type: int
        """
        if part is None:
            raise ValueError("Invalid value for `part`, must not be `None`")

        self._part = part

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
        if not isinstance(other, GetCharactersCharacterIdMedalsGraphic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
