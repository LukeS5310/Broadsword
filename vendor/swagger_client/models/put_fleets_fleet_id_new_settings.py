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


class PutFleetsFleetIdNewSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, is_free_move=None, motd=None):
        """
        PutFleetsFleetIdNewSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'is_free_move': 'bool',
            'motd': 'str'
        }

        self.attribute_map = {
            'is_free_move': 'is_free_move',
            'motd': 'motd'
        }

        self._is_free_move = is_free_move
        self._motd = motd

    @property
    def is_free_move(self):
        """
        Gets the is_free_move of this PutFleetsFleetIdNewSettings.
        Should free-move be enabled in the fleet

        :return: The is_free_move of this PutFleetsFleetIdNewSettings.
        :rtype: bool
        """
        return self._is_free_move

    @is_free_move.setter
    def is_free_move(self, is_free_move):
        """
        Sets the is_free_move of this PutFleetsFleetIdNewSettings.
        Should free-move be enabled in the fleet

        :param is_free_move: The is_free_move of this PutFleetsFleetIdNewSettings.
        :type: bool
        """

        self._is_free_move = is_free_move

    @property
    def motd(self):
        """
        Gets the motd of this PutFleetsFleetIdNewSettings.
        New fleet MOTD in CCP flavoured HTML

        :return: The motd of this PutFleetsFleetIdNewSettings.
        :rtype: str
        """
        return self._motd

    @motd.setter
    def motd(self, motd):
        """
        Sets the motd of this PutFleetsFleetIdNewSettings.
        New fleet MOTD in CCP flavoured HTML

        :param motd: The motd of this PutFleetsFleetIdNewSettings.
        :type: str
        """

        self._motd = motd

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
        if not isinstance(other, PutFleetsFleetIdNewSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
