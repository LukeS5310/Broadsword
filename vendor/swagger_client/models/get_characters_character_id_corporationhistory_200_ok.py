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


class GetCharactersCharacterIdCorporationhistory200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, corporation_id=None, is_deleted=None, record_id=None, start_date=None):
        """
        GetCharactersCharacterIdCorporationhistory200Ok - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'corporation_id': 'int',
            'is_deleted': 'bool',
            'record_id': 'int',
            'start_date': 'datetime'
        }

        self.attribute_map = {
            'corporation_id': 'corporation_id',
            'is_deleted': 'is_deleted',
            'record_id': 'record_id',
            'start_date': 'start_date'
        }

        self._corporation_id = corporation_id
        self._is_deleted = is_deleted
        self._record_id = record_id
        self._start_date = start_date

    @property
    def corporation_id(self):
        """
        Gets the corporation_id of this GetCharactersCharacterIdCorporationhistory200Ok.
        corporation_id integer

        :return: The corporation_id of this GetCharactersCharacterIdCorporationhistory200Ok.
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """
        Sets the corporation_id of this GetCharactersCharacterIdCorporationhistory200Ok.
        corporation_id integer

        :param corporation_id: The corporation_id of this GetCharactersCharacterIdCorporationhistory200Ok.
        :type: int
        """
        if corporation_id is None:
            raise ValueError("Invalid value for `corporation_id`, must not be `None`")

        self._corporation_id = corporation_id

    @property
    def is_deleted(self):
        """
        Gets the is_deleted of this GetCharactersCharacterIdCorporationhistory200Ok.
        True if the corporation has been deleted

        :return: The is_deleted of this GetCharactersCharacterIdCorporationhistory200Ok.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """
        Sets the is_deleted of this GetCharactersCharacterIdCorporationhistory200Ok.
        True if the corporation has been deleted

        :param is_deleted: The is_deleted of this GetCharactersCharacterIdCorporationhistory200Ok.
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def record_id(self):
        """
        Gets the record_id of this GetCharactersCharacterIdCorporationhistory200Ok.
        An incrementing ID that can be used to canonically establish order of records in cases where dates may be ambiguous

        :return: The record_id of this GetCharactersCharacterIdCorporationhistory200Ok.
        :rtype: int
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """
        Sets the record_id of this GetCharactersCharacterIdCorporationhistory200Ok.
        An incrementing ID that can be used to canonically establish order of records in cases where dates may be ambiguous

        :param record_id: The record_id of this GetCharactersCharacterIdCorporationhistory200Ok.
        :type: int
        """
        if record_id is None:
            raise ValueError("Invalid value for `record_id`, must not be `None`")

        self._record_id = record_id

    @property
    def start_date(self):
        """
        Gets the start_date of this GetCharactersCharacterIdCorporationhistory200Ok.
        start_date string

        :return: The start_date of this GetCharactersCharacterIdCorporationhistory200Ok.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this GetCharactersCharacterIdCorporationhistory200Ok.
        start_date string

        :param start_date: The start_date of this GetCharactersCharacterIdCorporationhistory200Ok.
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")

        self._start_date = start_date

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
        if not isinstance(other, GetCharactersCharacterIdCorporationhistory200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
