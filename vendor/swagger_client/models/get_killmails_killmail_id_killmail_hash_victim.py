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


class GetKillmailsKillmailIdKillmailHashVictim(object):
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
        'corporation_id': 'int',
        'alliance_id': 'int',
        'faction_id': 'int',
        'damage_taken': 'int',
        'ship_type_id': 'int',
        'items': 'list[GetKillmailsKillmailIdKillmailHashItem1]',
        'position': 'GetKillmailsKillmailIdKillmailHashPosition'
    }

    attribute_map = {
        'character_id': 'character_id',
        'corporation_id': 'corporation_id',
        'alliance_id': 'alliance_id',
        'faction_id': 'faction_id',
        'damage_taken': 'damage_taken',
        'ship_type_id': 'ship_type_id',
        'items': 'items',
        'position': 'position'
    }

    def __init__(self, character_id=None, corporation_id=None, alliance_id=None, faction_id=None, damage_taken=None, ship_type_id=None, items=None, position=None):
        """
        GetKillmailsKillmailIdKillmailHashVictim - a model defined in Swagger
        """

        self._character_id = None
        self._corporation_id = None
        self._alliance_id = None
        self._faction_id = None
        self._damage_taken = None
        self._ship_type_id = None
        self._items = None
        self._position = None
        self.discriminator = None

        if character_id is not None:
          self.character_id = character_id
        if corporation_id is not None:
          self.corporation_id = corporation_id
        if alliance_id is not None:
          self.alliance_id = alliance_id
        if faction_id is not None:
          self.faction_id = faction_id
        self.damage_taken = damage_taken
        self.ship_type_id = ship_type_id
        if items is not None:
          self.items = items
        if position is not None:
          self.position = position

    @property
    def character_id(self):
        """
        Gets the character_id of this GetKillmailsKillmailIdKillmailHashVictim.
        character_id integer

        :return: The character_id of this GetKillmailsKillmailIdKillmailHashVictim.
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """
        Sets the character_id of this GetKillmailsKillmailIdKillmailHashVictim.
        character_id integer

        :param character_id: The character_id of this GetKillmailsKillmailIdKillmailHashVictim.
        :type: int
        """

        self._character_id = character_id

    @property
    def corporation_id(self):
        """
        Gets the corporation_id of this GetKillmailsKillmailIdKillmailHashVictim.
        corporation_id integer

        :return: The corporation_id of this GetKillmailsKillmailIdKillmailHashVictim.
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """
        Sets the corporation_id of this GetKillmailsKillmailIdKillmailHashVictim.
        corporation_id integer

        :param corporation_id: The corporation_id of this GetKillmailsKillmailIdKillmailHashVictim.
        :type: int
        """

        self._corporation_id = corporation_id

    @property
    def alliance_id(self):
        """
        Gets the alliance_id of this GetKillmailsKillmailIdKillmailHashVictim.
        alliance_id integer

        :return: The alliance_id of this GetKillmailsKillmailIdKillmailHashVictim.
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """
        Sets the alliance_id of this GetKillmailsKillmailIdKillmailHashVictim.
        alliance_id integer

        :param alliance_id: The alliance_id of this GetKillmailsKillmailIdKillmailHashVictim.
        :type: int
        """

        self._alliance_id = alliance_id

    @property
    def faction_id(self):
        """
        Gets the faction_id of this GetKillmailsKillmailIdKillmailHashVictim.
        faction_id integer

        :return: The faction_id of this GetKillmailsKillmailIdKillmailHashVictim.
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """
        Sets the faction_id of this GetKillmailsKillmailIdKillmailHashVictim.
        faction_id integer

        :param faction_id: The faction_id of this GetKillmailsKillmailIdKillmailHashVictim.
        :type: int
        """

        self._faction_id = faction_id

    @property
    def damage_taken(self):
        """
        Gets the damage_taken of this GetKillmailsKillmailIdKillmailHashVictim.
        How much total damage was taken by the victim 

        :return: The damage_taken of this GetKillmailsKillmailIdKillmailHashVictim.
        :rtype: int
        """
        return self._damage_taken

    @damage_taken.setter
    def damage_taken(self, damage_taken):
        """
        Sets the damage_taken of this GetKillmailsKillmailIdKillmailHashVictim.
        How much total damage was taken by the victim 

        :param damage_taken: The damage_taken of this GetKillmailsKillmailIdKillmailHashVictim.
        :type: int
        """
        if damage_taken is None:
            raise ValueError("Invalid value for `damage_taken`, must not be `None`")

        self._damage_taken = damage_taken

    @property
    def ship_type_id(self):
        """
        Gets the ship_type_id of this GetKillmailsKillmailIdKillmailHashVictim.
        The ship that the victim was piloting and was destroyed 

        :return: The ship_type_id of this GetKillmailsKillmailIdKillmailHashVictim.
        :rtype: int
        """
        return self._ship_type_id

    @ship_type_id.setter
    def ship_type_id(self, ship_type_id):
        """
        Sets the ship_type_id of this GetKillmailsKillmailIdKillmailHashVictim.
        The ship that the victim was piloting and was destroyed 

        :param ship_type_id: The ship_type_id of this GetKillmailsKillmailIdKillmailHashVictim.
        :type: int
        """
        if ship_type_id is None:
            raise ValueError("Invalid value for `ship_type_id`, must not be `None`")

        self._ship_type_id = ship_type_id

    @property
    def items(self):
        """
        Gets the items of this GetKillmailsKillmailIdKillmailHashVictim.
        items array

        :return: The items of this GetKillmailsKillmailIdKillmailHashVictim.
        :rtype: list[GetKillmailsKillmailIdKillmailHashItem1]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this GetKillmailsKillmailIdKillmailHashVictim.
        items array

        :param items: The items of this GetKillmailsKillmailIdKillmailHashVictim.
        :type: list[GetKillmailsKillmailIdKillmailHashItem1]
        """

        self._items = items

    @property
    def position(self):
        """
        Gets the position of this GetKillmailsKillmailIdKillmailHashVictim.

        :return: The position of this GetKillmailsKillmailIdKillmailHashVictim.
        :rtype: GetKillmailsKillmailIdKillmailHashPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this GetKillmailsKillmailIdKillmailHashVictim.

        :param position: The position of this GetKillmailsKillmailIdKillmailHashVictim.
        :type: GetKillmailsKillmailIdKillmailHashPosition
        """

        self._position = position

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
        if not isinstance(other, GetKillmailsKillmailIdKillmailHashVictim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
