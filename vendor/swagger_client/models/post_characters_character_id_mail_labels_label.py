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


class PostCharactersCharacterIdMailLabelsLabel(object):
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
        'name': 'str',
        'color': 'str'
    }

    attribute_map = {
        'name': 'name',
        'color': 'color'
    }

    def __init__(self, name=None, color='#ffffff'):
        """
        PostCharactersCharacterIdMailLabelsLabel - a model defined in Swagger
        """

        self._name = None
        self._color = None
        self.discriminator = None

        self.name = name
        if color is not None:
          self.color = color

    @property
    def name(self):
        """
        Gets the name of this PostCharactersCharacterIdMailLabelsLabel.
        name string

        :return: The name of this PostCharactersCharacterIdMailLabelsLabel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PostCharactersCharacterIdMailLabelsLabel.
        name string

        :param name: The name of this PostCharactersCharacterIdMailLabelsLabel.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 40:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `40`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def color(self):
        """
        Gets the color of this PostCharactersCharacterIdMailLabelsLabel.
        Hexadecimal string representing label color, in RGB format

        :return: The color of this PostCharactersCharacterIdMailLabelsLabel.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this PostCharactersCharacterIdMailLabelsLabel.
        Hexadecimal string representing label color, in RGB format

        :param color: The color of this PostCharactersCharacterIdMailLabelsLabel.
        :type: str
        """
        allowed_values = ["#0000fe", "#006634", "#0099ff", "#00ff33", "#01ffff", "#349800", "#660066", "#666666", "#999999", "#99ffff", "#9a0000", "#ccff9a", "#e6e6e6", "#fe0000", "#ff6600", "#ffff01", "#ffffcd", "#ffffff"]
        if color not in allowed_values:
            raise ValueError(
                "Invalid value for `color` ({0}), must be one of {1}"
                .format(color, allowed_values)
            )

        self._color = color

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
        if not isinstance(other, PostCharactersCharacterIdMailLabelsLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
