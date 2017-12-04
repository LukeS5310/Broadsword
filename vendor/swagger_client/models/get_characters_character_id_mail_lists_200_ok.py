# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.7.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetCharactersCharacterIdMailLists200Ok(object):
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
        'mailing_list_id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'mailing_list_id': 'mailing_list_id',
        'name': 'name'
    }

    def __init__(self, mailing_list_id=None, name=None):
        """
        GetCharactersCharacterIdMailLists200Ok - a model defined in Swagger
        """

        self._mailing_list_id = None
        self._name = None
        self.discriminator = None

        self.mailing_list_id = mailing_list_id
        self.name = name

    @property
    def mailing_list_id(self):
        """
        Gets the mailing_list_id of this GetCharactersCharacterIdMailLists200Ok.
        Mailing list ID

        :return: The mailing_list_id of this GetCharactersCharacterIdMailLists200Ok.
        :rtype: int
        """
        return self._mailing_list_id

    @mailing_list_id.setter
    def mailing_list_id(self, mailing_list_id):
        """
        Sets the mailing_list_id of this GetCharactersCharacterIdMailLists200Ok.
        Mailing list ID

        :param mailing_list_id: The mailing_list_id of this GetCharactersCharacterIdMailLists200Ok.
        :type: int
        """
        if mailing_list_id is None:
            raise ValueError("Invalid value for `mailing_list_id`, must not be `None`")

        self._mailing_list_id = mailing_list_id

    @property
    def name(self):
        """
        Gets the name of this GetCharactersCharacterIdMailLists200Ok.
        name string

        :return: The name of this GetCharactersCharacterIdMailLists200Ok.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetCharactersCharacterIdMailLists200Ok.
        name string

        :param name: The name of this GetCharactersCharacterIdMailLists200Ok.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, GetCharactersCharacterIdMailLists200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
