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


class GetCorporationsCorporationIdStructures200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, corporation_id=None, current_vul=None, fuel_expires=None, next_vul=None, profile_id=None, services=None, state_timer_end=None, state_timer_start=None, structure_id=None, system_id=None, type_id=None, unanchors_at=None):
        """
        GetCorporationsCorporationIdStructures200Ok - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'corporation_id': 'int',
            'current_vul': 'list[GetCorporationsCorporationIdStructuresCurrentVul]',
            'fuel_expires': 'date',
            'next_vul': 'list[GetCorporationsCorporationIdStructuresNextVul]',
            'profile_id': 'int',
            'services': 'list[GetCorporationsCorporationIdStructuresService]',
            'state_timer_end': 'date',
            'state_timer_start': 'date',
            'structure_id': 'int',
            'system_id': 'int',
            'type_id': 'int',
            'unanchors_at': 'date'
        }

        self.attribute_map = {
            'corporation_id': 'corporation_id',
            'current_vul': 'current_vul',
            'fuel_expires': 'fuel_expires',
            'next_vul': 'next_vul',
            'profile_id': 'profile_id',
            'services': 'services',
            'state_timer_end': 'state_timer_end',
            'state_timer_start': 'state_timer_start',
            'structure_id': 'structure_id',
            'system_id': 'system_id',
            'type_id': 'type_id',
            'unanchors_at': 'unanchors_at'
        }

        self._corporation_id = corporation_id
        self._current_vul = current_vul
        self._fuel_expires = fuel_expires
        self._next_vul = next_vul
        self._profile_id = profile_id
        self._services = services
        self._state_timer_end = state_timer_end
        self._state_timer_start = state_timer_start
        self._structure_id = structure_id
        self._system_id = system_id
        self._type_id = type_id
        self._unanchors_at = unanchors_at

    @property
    def corporation_id(self):
        """
        Gets the corporation_id of this GetCorporationsCorporationIdStructures200Ok.
        ID of the corporation that owns the structure

        :return: The corporation_id of this GetCorporationsCorporationIdStructures200Ok.
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """
        Sets the corporation_id of this GetCorporationsCorporationIdStructures200Ok.
        ID of the corporation that owns the structure

        :param corporation_id: The corporation_id of this GetCorporationsCorporationIdStructures200Ok.
        :type: int
        """
        if corporation_id is None:
            raise ValueError("Invalid value for `corporation_id`, must not be `None`")

        self._corporation_id = corporation_id

    @property
    def current_vul(self):
        """
        Gets the current_vul of this GetCorporationsCorporationIdStructures200Ok.
        This week's vulnerability windows, Monday is day 0

        :return: The current_vul of this GetCorporationsCorporationIdStructures200Ok.
        :rtype: list[GetCorporationsCorporationIdStructuresCurrentVul]
        """
        return self._current_vul

    @current_vul.setter
    def current_vul(self, current_vul):
        """
        Sets the current_vul of this GetCorporationsCorporationIdStructures200Ok.
        This week's vulnerability windows, Monday is day 0

        :param current_vul: The current_vul of this GetCorporationsCorporationIdStructures200Ok.
        :type: list[GetCorporationsCorporationIdStructuresCurrentVul]
        """
        if current_vul is None:
            raise ValueError("Invalid value for `current_vul`, must not be `None`")

        self._current_vul = current_vul

    @property
    def fuel_expires(self):
        """
        Gets the fuel_expires of this GetCorporationsCorporationIdStructures200Ok.
        Date on which the structure will run out of fuel

        :return: The fuel_expires of this GetCorporationsCorporationIdStructures200Ok.
        :rtype: date
        """
        return self._fuel_expires

    @fuel_expires.setter
    def fuel_expires(self, fuel_expires):
        """
        Sets the fuel_expires of this GetCorporationsCorporationIdStructures200Ok.
        Date on which the structure will run out of fuel

        :param fuel_expires: The fuel_expires of this GetCorporationsCorporationIdStructures200Ok.
        :type: date
        """

        self._fuel_expires = fuel_expires

    @property
    def next_vul(self):
        """
        Gets the next_vul of this GetCorporationsCorporationIdStructures200Ok.
        Next week's vulnerability windows, Monday is day 0

        :return: The next_vul of this GetCorporationsCorporationIdStructures200Ok.
        :rtype: list[GetCorporationsCorporationIdStructuresNextVul]
        """
        return self._next_vul

    @next_vul.setter
    def next_vul(self, next_vul):
        """
        Sets the next_vul of this GetCorporationsCorporationIdStructures200Ok.
        Next week's vulnerability windows, Monday is day 0

        :param next_vul: The next_vul of this GetCorporationsCorporationIdStructures200Ok.
        :type: list[GetCorporationsCorporationIdStructuresNextVul]
        """
        if next_vul is None:
            raise ValueError("Invalid value for `next_vul`, must not be `None`")

        self._next_vul = next_vul

    @property
    def profile_id(self):
        """
        Gets the profile_id of this GetCorporationsCorporationIdStructures200Ok.
        The id of the ACL profile for this citadel

        :return: The profile_id of this GetCorporationsCorporationIdStructures200Ok.
        :rtype: int
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """
        Sets the profile_id of this GetCorporationsCorporationIdStructures200Ok.
        The id of the ACL profile for this citadel

        :param profile_id: The profile_id of this GetCorporationsCorporationIdStructures200Ok.
        :type: int
        """
        if profile_id is None:
            raise ValueError("Invalid value for `profile_id`, must not be `None`")

        self._profile_id = profile_id

    @property
    def services(self):
        """
        Gets the services of this GetCorporationsCorporationIdStructures200Ok.
        Contains a list of service upgrades, and their state

        :return: The services of this GetCorporationsCorporationIdStructures200Ok.
        :rtype: list[GetCorporationsCorporationIdStructuresService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this GetCorporationsCorporationIdStructures200Ok.
        Contains a list of service upgrades, and their state

        :param services: The services of this GetCorporationsCorporationIdStructures200Ok.
        :type: list[GetCorporationsCorporationIdStructuresService]
        """

        self._services = services

    @property
    def state_timer_end(self):
        """
        Gets the state_timer_end of this GetCorporationsCorporationIdStructures200Ok.
        Date at which the structure will move to it's next state

        :return: The state_timer_end of this GetCorporationsCorporationIdStructures200Ok.
        :rtype: date
        """
        return self._state_timer_end

    @state_timer_end.setter
    def state_timer_end(self, state_timer_end):
        """
        Sets the state_timer_end of this GetCorporationsCorporationIdStructures200Ok.
        Date at which the structure will move to it's next state

        :param state_timer_end: The state_timer_end of this GetCorporationsCorporationIdStructures200Ok.
        :type: date
        """

        self._state_timer_end = state_timer_end

    @property
    def state_timer_start(self):
        """
        Gets the state_timer_start of this GetCorporationsCorporationIdStructures200Ok.
        Date at which the structure entered it's current state

        :return: The state_timer_start of this GetCorporationsCorporationIdStructures200Ok.
        :rtype: date
        """
        return self._state_timer_start

    @state_timer_start.setter
    def state_timer_start(self, state_timer_start):
        """
        Sets the state_timer_start of this GetCorporationsCorporationIdStructures200Ok.
        Date at which the structure entered it's current state

        :param state_timer_start: The state_timer_start of this GetCorporationsCorporationIdStructures200Ok.
        :type: date
        """

        self._state_timer_start = state_timer_start

    @property
    def structure_id(self):
        """
        Gets the structure_id of this GetCorporationsCorporationIdStructures200Ok.
        The Item ID of the structure

        :return: The structure_id of this GetCorporationsCorporationIdStructures200Ok.
        :rtype: int
        """
        return self._structure_id

    @structure_id.setter
    def structure_id(self, structure_id):
        """
        Sets the structure_id of this GetCorporationsCorporationIdStructures200Ok.
        The Item ID of the structure

        :param structure_id: The structure_id of this GetCorporationsCorporationIdStructures200Ok.
        :type: int
        """
        if structure_id is None:
            raise ValueError("Invalid value for `structure_id`, must not be `None`")

        self._structure_id = structure_id

    @property
    def system_id(self):
        """
        Gets the system_id of this GetCorporationsCorporationIdStructures200Ok.
        The solar system the structure is in

        :return: The system_id of this GetCorporationsCorporationIdStructures200Ok.
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """
        Sets the system_id of this GetCorporationsCorporationIdStructures200Ok.
        The solar system the structure is in

        :param system_id: The system_id of this GetCorporationsCorporationIdStructures200Ok.
        :type: int
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")

        self._system_id = system_id

    @property
    def type_id(self):
        """
        Gets the type_id of this GetCorporationsCorporationIdStructures200Ok.
        The type id of the structure

        :return: The type_id of this GetCorporationsCorporationIdStructures200Ok.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this GetCorporationsCorporationIdStructures200Ok.
        The type id of the structure

        :param type_id: The type_id of this GetCorporationsCorporationIdStructures200Ok.
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")

        self._type_id = type_id

    @property
    def unanchors_at(self):
        """
        Gets the unanchors_at of this GetCorporationsCorporationIdStructures200Ok.
        Date at which the structure will unanchor

        :return: The unanchors_at of this GetCorporationsCorporationIdStructures200Ok.
        :rtype: date
        """
        return self._unanchors_at

    @unanchors_at.setter
    def unanchors_at(self, unanchors_at):
        """
        Sets the unanchors_at of this GetCorporationsCorporationIdStructures200Ok.
        Date at which the structure will unanchor

        :param unanchors_at: The unanchors_at of this GetCorporationsCorporationIdStructures200Ok.
        :type: date
        """

        self._unanchors_at = unanchors_at

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
        if not isinstance(other, GetCorporationsCorporationIdStructures200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other