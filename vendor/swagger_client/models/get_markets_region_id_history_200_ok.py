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


class GetMarketsRegionIdHistory200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, average=None, date=None, highest=None, lowest=None, order_count=None, volume=None):
        """
        GetMarketsRegionIdHistory200Ok - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'average': 'float',
            'date': 'date',
            'highest': 'float',
            'lowest': 'float',
            'order_count': 'int',
            'volume': 'int'
        }

        self.attribute_map = {
            'average': 'average',
            'date': 'date',
            'highest': 'highest',
            'lowest': 'lowest',
            'order_count': 'order_count',
            'volume': 'volume'
        }

        self._average = average
        self._date = date
        self._highest = highest
        self._lowest = lowest
        self._order_count = order_count
        self._volume = volume

    @property
    def average(self):
        """
        Gets the average of this GetMarketsRegionIdHistory200Ok.
        average number

        :return: The average of this GetMarketsRegionIdHistory200Ok.
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """
        Sets the average of this GetMarketsRegionIdHistory200Ok.
        average number

        :param average: The average of this GetMarketsRegionIdHistory200Ok.
        :type: float
        """
        if average is None:
            raise ValueError("Invalid value for `average`, must not be `None`")

        self._average = average

    @property
    def date(self):
        """
        Gets the date of this GetMarketsRegionIdHistory200Ok.
        The date of this historical statistic entry

        :return: The date of this GetMarketsRegionIdHistory200Ok.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this GetMarketsRegionIdHistory200Ok.
        The date of this historical statistic entry

        :param date: The date of this GetMarketsRegionIdHistory200Ok.
        :type: date
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")

        self._date = date

    @property
    def highest(self):
        """
        Gets the highest of this GetMarketsRegionIdHistory200Ok.
        highest number

        :return: The highest of this GetMarketsRegionIdHistory200Ok.
        :rtype: float
        """
        return self._highest

    @highest.setter
    def highest(self, highest):
        """
        Sets the highest of this GetMarketsRegionIdHistory200Ok.
        highest number

        :param highest: The highest of this GetMarketsRegionIdHistory200Ok.
        :type: float
        """
        if highest is None:
            raise ValueError("Invalid value for `highest`, must not be `None`")

        self._highest = highest

    @property
    def lowest(self):
        """
        Gets the lowest of this GetMarketsRegionIdHistory200Ok.
        lowest number

        :return: The lowest of this GetMarketsRegionIdHistory200Ok.
        :rtype: float
        """
        return self._lowest

    @lowest.setter
    def lowest(self, lowest):
        """
        Sets the lowest of this GetMarketsRegionIdHistory200Ok.
        lowest number

        :param lowest: The lowest of this GetMarketsRegionIdHistory200Ok.
        :type: float
        """
        if lowest is None:
            raise ValueError("Invalid value for `lowest`, must not be `None`")

        self._lowest = lowest

    @property
    def order_count(self):
        """
        Gets the order_count of this GetMarketsRegionIdHistory200Ok.
        Total number of orders happened that day

        :return: The order_count of this GetMarketsRegionIdHistory200Ok.
        :rtype: int
        """
        return self._order_count

    @order_count.setter
    def order_count(self, order_count):
        """
        Sets the order_count of this GetMarketsRegionIdHistory200Ok.
        Total number of orders happened that day

        :param order_count: The order_count of this GetMarketsRegionIdHistory200Ok.
        :type: int
        """
        if order_count is None:
            raise ValueError("Invalid value for `order_count`, must not be `None`")

        self._order_count = order_count

    @property
    def volume(self):
        """
        Gets the volume of this GetMarketsRegionIdHistory200Ok.
        Total

        :return: The volume of this GetMarketsRegionIdHistory200Ok.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """
        Sets the volume of this GetMarketsRegionIdHistory200Ok.
        Total

        :param volume: The volume of this GetMarketsRegionIdHistory200Ok.
        :type: int
        """
        if volume is None:
            raise ValueError("Invalid value for `volume`, must not be `None`")

        self._volume = volume

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
        if not isinstance(other, GetMarketsRegionIdHistory200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
