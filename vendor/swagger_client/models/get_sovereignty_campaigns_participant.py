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


class GetSovereigntyCampaignsParticipant(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, alliance_id=None, score=None):
        """
        GetSovereigntyCampaignsParticipant - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alliance_id': 'int',
            'score': 'float'
        }

        self.attribute_map = {
            'alliance_id': 'alliance_id',
            'score': 'score'
        }

        self._alliance_id = alliance_id
        self._score = score

    @property
    def alliance_id(self):
        """
        Gets the alliance_id of this GetSovereigntyCampaignsParticipant.
        alliance_id integer

        :return: The alliance_id of this GetSovereigntyCampaignsParticipant.
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """
        Sets the alliance_id of this GetSovereigntyCampaignsParticipant.
        alliance_id integer

        :param alliance_id: The alliance_id of this GetSovereigntyCampaignsParticipant.
        :type: int
        """
        if alliance_id is None:
            raise ValueError("Invalid value for `alliance_id`, must not be `None`")

        self._alliance_id = alliance_id

    @property
    def score(self):
        """
        Gets the score of this GetSovereigntyCampaignsParticipant.
        score number

        :return: The score of this GetSovereigntyCampaignsParticipant.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this GetSovereigntyCampaignsParticipant.
        score number

        :param score: The score of this GetSovereigntyCampaignsParticipant.
        :type: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")

        self._score = score

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
        if not isinstance(other, GetSovereigntyCampaignsParticipant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
