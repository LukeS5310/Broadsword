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


class GetCorporationsNames200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, corporation_id=None, corporation_name=None):
        """
        GetCorporationsNames200Ok - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'corporation_id': 'int',
            'corporation_name': 'str'
        }

        self.attribute_map = {
            'corporation_id': 'corporation_id',
            'corporation_name': 'corporation_name'
        }

        self._corporation_id = corporation_id
        self._corporation_name = corporation_name

    @property
    def corporation_id(self):
        """
        Gets the corporation_id of this GetCorporationsNames200Ok.
        corporation_id integer

        :return: The corporation_id of this GetCorporationsNames200Ok.
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """
        Sets the corporation_id of this GetCorporationsNames200Ok.
        corporation_id integer

        :param corporation_id: The corporation_id of this GetCorporationsNames200Ok.
        :type: int
        """
        if corporation_id is None:
            raise ValueError("Invalid value for `corporation_id`, must not be `None`")

        self._corporation_id = corporation_id

    @property
    def corporation_name(self):
        """
        Gets the corporation_name of this GetCorporationsNames200Ok.
        corporation_name string

        :return: The corporation_name of this GetCorporationsNames200Ok.
        :rtype: str
        """
        return self._corporation_name

    @corporation_name.setter
    def corporation_name(self, corporation_name):
        """
        Sets the corporation_name of this GetCorporationsNames200Ok.
        corporation_name string

        :param corporation_name: The corporation_name of this GetCorporationsNames200Ok.
        :type: str
        """
        if corporation_name is None:
            raise ValueError("Invalid value for `corporation_name`, must not be `None`")

        self._corporation_name = corporation_name

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
        if not isinstance(other, GetCorporationsNames200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
