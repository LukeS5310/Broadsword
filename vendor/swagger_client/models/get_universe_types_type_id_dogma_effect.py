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


class GetUniverseTypesTypeIdDogmaEffect(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, effect_id=None, is_default=None):
        """
        GetUniverseTypesTypeIdDogmaEffect - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'effect_id': 'int',
            'is_default': 'bool'
        }

        self.attribute_map = {
            'effect_id': 'effect_id',
            'is_default': 'is_default'
        }

        self._effect_id = effect_id
        self._is_default = is_default

    @property
    def effect_id(self):
        """
        Gets the effect_id of this GetUniverseTypesTypeIdDogmaEffect.
        effect_id integer

        :return: The effect_id of this GetUniverseTypesTypeIdDogmaEffect.
        :rtype: int
        """
        return self._effect_id

    @effect_id.setter
    def effect_id(self, effect_id):
        """
        Sets the effect_id of this GetUniverseTypesTypeIdDogmaEffect.
        effect_id integer

        :param effect_id: The effect_id of this GetUniverseTypesTypeIdDogmaEffect.
        :type: int
        """
        if effect_id is None:
            raise ValueError("Invalid value for `effect_id`, must not be `None`")

        self._effect_id = effect_id

    @property
    def is_default(self):
        """
        Gets the is_default of this GetUniverseTypesTypeIdDogmaEffect.
        is_default boolean

        :return: The is_default of this GetUniverseTypesTypeIdDogmaEffect.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this GetUniverseTypesTypeIdDogmaEffect.
        is_default boolean

        :param is_default: The is_default of this GetUniverseTypesTypeIdDogmaEffect.
        :type: bool
        """
        if is_default is None:
            raise ValueError("Invalid value for `is_default`, must not be `None`")

        self._is_default = is_default

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
        if not isinstance(other, GetUniverseTypesTypeIdDogmaEffect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
