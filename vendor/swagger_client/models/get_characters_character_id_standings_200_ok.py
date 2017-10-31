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


class GetCharactersCharacterIdStandings200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, from_id=None, from_type=None, standing=None):
        """
        GetCharactersCharacterIdStandings200Ok - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'from_id': 'int',
            'from_type': 'str',
            'standing': 'float'
        }

        self.attribute_map = {
            'from_id': 'from_id',
            'from_type': 'from_type',
            'standing': 'standing'
        }

        self._from_id = from_id
        self._from_type = from_type
        self._standing = standing

    @property
    def from_id(self):
        """
        Gets the from_id of this GetCharactersCharacterIdStandings200Ok.
        from_id integer

        :return: The from_id of this GetCharactersCharacterIdStandings200Ok.
        :rtype: int
        """
        return self._from_id

    @from_id.setter
    def from_id(self, from_id):
        """
        Sets the from_id of this GetCharactersCharacterIdStandings200Ok.
        from_id integer

        :param from_id: The from_id of this GetCharactersCharacterIdStandings200Ok.
        :type: int
        """
        if from_id is None:
            raise ValueError("Invalid value for `from_id`, must not be `None`")

        self._from_id = from_id

    @property
    def from_type(self):
        """
        Gets the from_type of this GetCharactersCharacterIdStandings200Ok.
        from_type string

        :return: The from_type of this GetCharactersCharacterIdStandings200Ok.
        :rtype: str
        """
        return self._from_type

    @from_type.setter
    def from_type(self, from_type):
        """
        Sets the from_type of this GetCharactersCharacterIdStandings200Ok.
        from_type string

        :param from_type: The from_type of this GetCharactersCharacterIdStandings200Ok.
        :type: str
        """
        allowed_values = ["agent", "npc_corp", "faction"]
        if from_type not in allowed_values:
            raise ValueError(
                "Invalid value for `from_type` ({0}), must be one of {1}"
                .format(from_type, allowed_values)
            )

        self._from_type = from_type

    @property
    def standing(self):
        """
        Gets the standing of this GetCharactersCharacterIdStandings200Ok.
        standing number

        :return: The standing of this GetCharactersCharacterIdStandings200Ok.
        :rtype: float
        """
        return self._standing

    @standing.setter
    def standing(self, standing):
        """
        Sets the standing of this GetCharactersCharacterIdStandings200Ok.
        standing number

        :param standing: The standing of this GetCharactersCharacterIdStandings200Ok.
        :type: float
        """
        if standing is None:
            raise ValueError("Invalid value for `standing`, must not be `None`")
        if standing is not None and standing > 10:
            raise ValueError("Invalid value for `standing`, must be a value less than or equal to `10`")
        if standing is not None and standing < -10:
            raise ValueError("Invalid value for `standing`, must be a value greater than or equal to `-10`")

        self._standing = standing

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
        if not isinstance(other, GetCharactersCharacterIdStandings200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
