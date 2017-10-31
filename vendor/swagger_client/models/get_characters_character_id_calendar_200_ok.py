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


class GetCharactersCharacterIdCalendar200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, event_date=None, event_id=None, event_response=None, importance=None, title=None):
        """
        GetCharactersCharacterIdCalendar200Ok - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'event_date': 'datetime',
            'event_id': 'int',
            'event_response': 'str',
            'importance': 'int',
            'title': 'str'
        }

        self.attribute_map = {
            'event_date': 'event_date',
            'event_id': 'event_id',
            'event_response': 'event_response',
            'importance': 'importance',
            'title': 'title'
        }

        self._event_date = event_date
        self._event_id = event_id
        self._event_response = event_response
        self._importance = importance
        self._title = title

    @property
    def event_date(self):
        """
        Gets the event_date of this GetCharactersCharacterIdCalendar200Ok.
        event_date string

        :return: The event_date of this GetCharactersCharacterIdCalendar200Ok.
        :rtype: datetime
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """
        Sets the event_date of this GetCharactersCharacterIdCalendar200Ok.
        event_date string

        :param event_date: The event_date of this GetCharactersCharacterIdCalendar200Ok.
        :type: datetime
        """

        self._event_date = event_date

    @property
    def event_id(self):
        """
        Gets the event_id of this GetCharactersCharacterIdCalendar200Ok.
        event_id integer

        :return: The event_id of this GetCharactersCharacterIdCalendar200Ok.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this GetCharactersCharacterIdCalendar200Ok.
        event_id integer

        :param event_id: The event_id of this GetCharactersCharacterIdCalendar200Ok.
        :type: int
        """

        self._event_id = event_id

    @property
    def event_response(self):
        """
        Gets the event_response of this GetCharactersCharacterIdCalendar200Ok.
        event_response string

        :return: The event_response of this GetCharactersCharacterIdCalendar200Ok.
        :rtype: str
        """
        return self._event_response

    @event_response.setter
    def event_response(self, event_response):
        """
        Sets the event_response of this GetCharactersCharacterIdCalendar200Ok.
        event_response string

        :param event_response: The event_response of this GetCharactersCharacterIdCalendar200Ok.
        :type: str
        """
        allowed_values = ["declined", "not_responded", "accepted", "tentative"]
        if event_response not in allowed_values:
            raise ValueError(
                "Invalid value for `event_response` ({0}), must be one of {1}"
                .format(event_response, allowed_values)
            )

        self._event_response = event_response

    @property
    def importance(self):
        """
        Gets the importance of this GetCharactersCharacterIdCalendar200Ok.
        importance integer

        :return: The importance of this GetCharactersCharacterIdCalendar200Ok.
        :rtype: int
        """
        return self._importance

    @importance.setter
    def importance(self, importance):
        """
        Sets the importance of this GetCharactersCharacterIdCalendar200Ok.
        importance integer

        :param importance: The importance of this GetCharactersCharacterIdCalendar200Ok.
        :type: int
        """

        self._importance = importance

    @property
    def title(self):
        """
        Gets the title of this GetCharactersCharacterIdCalendar200Ok.
        title string

        :return: The title of this GetCharactersCharacterIdCalendar200Ok.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this GetCharactersCharacterIdCalendar200Ok.
        title string

        :param title: The title of this GetCharactersCharacterIdCalendar200Ok.
        :type: str
        """

        self._title = title

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
        if not isinstance(other, GetCharactersCharacterIdCalendar200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
