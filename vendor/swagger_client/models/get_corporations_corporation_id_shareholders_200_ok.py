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


class GetCorporationsCorporationIdShareholders200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, share_count=None, shareholder_id=None, shareholder_type=None):
        """
        GetCorporationsCorporationIdShareholders200Ok - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'share_count': 'int',
            'shareholder_id': 'int',
            'shareholder_type': 'str'
        }

        self.attribute_map = {
            'share_count': 'share_count',
            'shareholder_id': 'shareholder_id',
            'shareholder_type': 'shareholder_type'
        }

        self._share_count = share_count
        self._shareholder_id = shareholder_id
        self._shareholder_type = shareholder_type

    @property
    def share_count(self):
        """
        Gets the share_count of this GetCorporationsCorporationIdShareholders200Ok.
        share_count integer

        :return: The share_count of this GetCorporationsCorporationIdShareholders200Ok.
        :rtype: int
        """
        return self._share_count

    @share_count.setter
    def share_count(self, share_count):
        """
        Sets the share_count of this GetCorporationsCorporationIdShareholders200Ok.
        share_count integer

        :param share_count: The share_count of this GetCorporationsCorporationIdShareholders200Ok.
        :type: int
        """
        if share_count is None:
            raise ValueError("Invalid value for `share_count`, must not be `None`")

        self._share_count = share_count

    @property
    def shareholder_id(self):
        """
        Gets the shareholder_id of this GetCorporationsCorporationIdShareholders200Ok.
        shareholder_id integer

        :return: The shareholder_id of this GetCorporationsCorporationIdShareholders200Ok.
        :rtype: int
        """
        return self._shareholder_id

    @shareholder_id.setter
    def shareholder_id(self, shareholder_id):
        """
        Sets the shareholder_id of this GetCorporationsCorporationIdShareholders200Ok.
        shareholder_id integer

        :param shareholder_id: The shareholder_id of this GetCorporationsCorporationIdShareholders200Ok.
        :type: int
        """
        if shareholder_id is None:
            raise ValueError("Invalid value for `shareholder_id`, must not be `None`")

        self._shareholder_id = shareholder_id

    @property
    def shareholder_type(self):
        """
        Gets the shareholder_type of this GetCorporationsCorporationIdShareholders200Ok.
        shareholder_type string

        :return: The shareholder_type of this GetCorporationsCorporationIdShareholders200Ok.
        :rtype: str
        """
        return self._shareholder_type

    @shareholder_type.setter
    def shareholder_type(self, shareholder_type):
        """
        Sets the shareholder_type of this GetCorporationsCorporationIdShareholders200Ok.
        shareholder_type string

        :param shareholder_type: The shareholder_type of this GetCorporationsCorporationIdShareholders200Ok.
        :type: str
        """
        allowed_values = ["character", "corporation"]
        if shareholder_type not in allowed_values:
            raise ValueError(
                "Invalid value for `shareholder_type` ({0}), must be one of {1}"
                .format(shareholder_type, allowed_values)
            )

        self._shareholder_type = shareholder_type

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
        if not isinstance(other, GetCorporationsCorporationIdShareholders200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
