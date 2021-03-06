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


class GetCharactersCharacterIdWalletJournalExtraInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, alliance_id=None, character_id=None, contract_id=None, corporation_id=None, destroyed_ship_type_id=None, job_id=None, location_id=None, npc_id=None, npc_name=None, planet_id=None, system_id=None, transaction_id=None):
        """
        GetCharactersCharacterIdWalletJournalExtraInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alliance_id': 'int',
            'character_id': 'int',
            'contract_id': 'int',
            'corporation_id': 'int',
            'destroyed_ship_type_id': 'int',
            'job_id': 'int',
            'location_id': 'int',
            'npc_id': 'int',
            'npc_name': 'str',
            'planet_id': 'int',
            'system_id': 'int',
            'transaction_id': 'int'
        }

        self.attribute_map = {
            'alliance_id': 'alliance_id',
            'character_id': 'character_id',
            'contract_id': 'contract_id',
            'corporation_id': 'corporation_id',
            'destroyed_ship_type_id': 'destroyed_ship_type_id',
            'job_id': 'job_id',
            'location_id': 'location_id',
            'npc_id': 'npc_id',
            'npc_name': 'npc_name',
            'planet_id': 'planet_id',
            'system_id': 'system_id',
            'transaction_id': 'transaction_id'
        }

        self._alliance_id = alliance_id
        self._character_id = character_id
        self._contract_id = contract_id
        self._corporation_id = corporation_id
        self._destroyed_ship_type_id = destroyed_ship_type_id
        self._job_id = job_id
        self._location_id = location_id
        self._npc_id = npc_id
        self._npc_name = npc_name
        self._planet_id = planet_id
        self._system_id = system_id
        self._transaction_id = transaction_id

    @property
    def alliance_id(self):
        """
        Gets the alliance_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        alliance_id integer

        :return: The alliance_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """
        Sets the alliance_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        alliance_id integer

        :param alliance_id: The alliance_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :type: int
        """

        self._alliance_id = alliance_id

    @property
    def character_id(self):
        """
        Gets the character_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        character_id integer

        :return: The character_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """
        Sets the character_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        character_id integer

        :param character_id: The character_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :type: int
        """

        self._character_id = character_id

    @property
    def contract_id(self):
        """
        Gets the contract_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        contract_id integer

        :return: The contract_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :rtype: int
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """
        Sets the contract_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        contract_id integer

        :param contract_id: The contract_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :type: int
        """

        self._contract_id = contract_id

    @property
    def corporation_id(self):
        """
        Gets the corporation_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        corporation_id integer

        :return: The corporation_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """
        Sets the corporation_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        corporation_id integer

        :param corporation_id: The corporation_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :type: int
        """

        self._corporation_id = corporation_id

    @property
    def destroyed_ship_type_id(self):
        """
        Gets the destroyed_ship_type_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        destroyed_ship_type_id integer

        :return: The destroyed_ship_type_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :rtype: int
        """
        return self._destroyed_ship_type_id

    @destroyed_ship_type_id.setter
    def destroyed_ship_type_id(self, destroyed_ship_type_id):
        """
        Sets the destroyed_ship_type_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        destroyed_ship_type_id integer

        :param destroyed_ship_type_id: The destroyed_ship_type_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :type: int
        """

        self._destroyed_ship_type_id = destroyed_ship_type_id

    @property
    def job_id(self):
        """
        Gets the job_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        job_id integer

        :return: The job_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        job_id integer

        :param job_id: The job_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :type: int
        """

        self._job_id = job_id

    @property
    def location_id(self):
        """
        Gets the location_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        location_id integer

        :return: The location_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        location_id integer

        :param location_id: The location_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :type: int
        """

        self._location_id = location_id

    @property
    def npc_id(self):
        """
        Gets the npc_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        npc_id integer

        :return: The npc_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :rtype: int
        """
        return self._npc_id

    @npc_id.setter
    def npc_id(self, npc_id):
        """
        Sets the npc_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        npc_id integer

        :param npc_id: The npc_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :type: int
        """

        self._npc_id = npc_id

    @property
    def npc_name(self):
        """
        Gets the npc_name of this GetCharactersCharacterIdWalletJournalExtraInfo.
        npc_name string

        :return: The npc_name of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :rtype: str
        """
        return self._npc_name

    @npc_name.setter
    def npc_name(self, npc_name):
        """
        Sets the npc_name of this GetCharactersCharacterIdWalletJournalExtraInfo.
        npc_name string

        :param npc_name: The npc_name of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :type: str
        """

        self._npc_name = npc_name

    @property
    def planet_id(self):
        """
        Gets the planet_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        planet_id integer

        :return: The planet_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :rtype: int
        """
        return self._planet_id

    @planet_id.setter
    def planet_id(self, planet_id):
        """
        Sets the planet_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        planet_id integer

        :param planet_id: The planet_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :type: int
        """

        self._planet_id = planet_id

    @property
    def system_id(self):
        """
        Gets the system_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        system_id integer

        :return: The system_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """
        Sets the system_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        system_id integer

        :param system_id: The system_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :type: int
        """

        self._system_id = system_id

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        transaction_id integer

        :return: The transaction_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        transaction_id integer

        :param transaction_id: The transaction_id of this GetCharactersCharacterIdWalletJournalExtraInfo.
        :type: int
        """

        self._transaction_id = transaction_id

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
        if not isinstance(other, GetCharactersCharacterIdWalletJournalExtraInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
