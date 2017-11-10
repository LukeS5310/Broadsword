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


class GetCorporationsCorporationIdMembersTitles200Ok(object):
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
        'character_id': 'int',
        'titles': 'list[int]'
    }

    attribute_map = {
        'character_id': 'character_id',
        'titles': 'titles'
    }

    def __init__(self, character_id=None, titles=None):
        """
        GetCorporationsCorporationIdMembersTitles200Ok - a model defined in Swagger
        """

        self._character_id = None
        self._titles = None
        self.discriminator = None

        self.character_id = character_id
        self.titles = titles

    @property
    def character_id(self):
        """
        Gets the character_id of this GetCorporationsCorporationIdMembersTitles200Ok.
        character_id integer

        :return: The character_id of this GetCorporationsCorporationIdMembersTitles200Ok.
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """
        Sets the character_id of this GetCorporationsCorporationIdMembersTitles200Ok.
        character_id integer

        :param character_id: The character_id of this GetCorporationsCorporationIdMembersTitles200Ok.
        :type: int
        """
        if character_id is None:
            raise ValueError("Invalid value for `character_id`, must not be `None`")

        self._character_id = character_id

    @property
    def titles(self):
        """
        Gets the titles of this GetCorporationsCorporationIdMembersTitles200Ok.
        A list of title_id

        :return: The titles of this GetCorporationsCorporationIdMembersTitles200Ok.
        :rtype: list[int]
        """
        return self._titles

    @titles.setter
    def titles(self, titles):
        """
        Sets the titles of this GetCorporationsCorporationIdMembersTitles200Ok.
        A list of title_id

        :param titles: The titles of this GetCorporationsCorporationIdMembersTitles200Ok.
        :type: list[int]
        """
        if titles is None:
            raise ValueError("Invalid value for `titles`, must not be `None`")

        self._titles = titles

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
        if not isinstance(other, GetCorporationsCorporationIdMembersTitles200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
