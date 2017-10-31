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


class GetCharactersCharacterIdPlanetsPlanetIdPin(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, contents=None, expiry_time=None, extractor_details=None, factory_details=None, install_time=None, last_cycle_start=None, latitude=None, longitude=None, pin_id=None, schematic_id=None, type_id=None):
        """
        GetCharactersCharacterIdPlanetsPlanetIdPin - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'contents': 'list[GetCharactersCharacterIdPlanetsPlanetIdContent]',
            'expiry_time': 'datetime',
            'extractor_details': 'GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails',
            'factory_details': 'GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails',
            'install_time': 'datetime',
            'last_cycle_start': 'datetime',
            'latitude': 'float',
            'longitude': 'float',
            'pin_id': 'int',
            'schematic_id': 'int',
            'type_id': 'int'
        }

        self.attribute_map = {
            'contents': 'contents',
            'expiry_time': 'expiry_time',
            'extractor_details': 'extractor_details',
            'factory_details': 'factory_details',
            'install_time': 'install_time',
            'last_cycle_start': 'last_cycle_start',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'pin_id': 'pin_id',
            'schematic_id': 'schematic_id',
            'type_id': 'type_id'
        }

        self._contents = contents
        self._expiry_time = expiry_time
        self._extractor_details = extractor_details
        self._factory_details = factory_details
        self._install_time = install_time
        self._last_cycle_start = last_cycle_start
        self._latitude = latitude
        self._longitude = longitude
        self._pin_id = pin_id
        self._schematic_id = schematic_id
        self._type_id = type_id

    @property
    def contents(self):
        """
        Gets the contents of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        contents array

        :return: The contents of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :rtype: list[GetCharactersCharacterIdPlanetsPlanetIdContent]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """
        Sets the contents of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        contents array

        :param contents: The contents of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :type: list[GetCharactersCharacterIdPlanetsPlanetIdContent]
        """

        self._contents = contents

    @property
    def expiry_time(self):
        """
        Gets the expiry_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        expiry_time string

        :return: The expiry_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :rtype: datetime
        """
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, expiry_time):
        """
        Sets the expiry_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        expiry_time string

        :param expiry_time: The expiry_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :type: datetime
        """

        self._expiry_time = expiry_time

    @property
    def extractor_details(self):
        """
        Gets the extractor_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.

        :return: The extractor_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :rtype: GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails
        """
        return self._extractor_details

    @extractor_details.setter
    def extractor_details(self, extractor_details):
        """
        Sets the extractor_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.

        :param extractor_details: The extractor_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :type: GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails
        """

        self._extractor_details = extractor_details

    @property
    def factory_details(self):
        """
        Gets the factory_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.

        :return: The factory_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :rtype: GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails
        """
        return self._factory_details

    @factory_details.setter
    def factory_details(self, factory_details):
        """
        Sets the factory_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.

        :param factory_details: The factory_details of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :type: GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails
        """

        self._factory_details = factory_details

    @property
    def install_time(self):
        """
        Gets the install_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        install_time string

        :return: The install_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :rtype: datetime
        """
        return self._install_time

    @install_time.setter
    def install_time(self, install_time):
        """
        Sets the install_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        install_time string

        :param install_time: The install_time of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :type: datetime
        """

        self._install_time = install_time

    @property
    def last_cycle_start(self):
        """
        Gets the last_cycle_start of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        last_cycle_start string

        :return: The last_cycle_start of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :rtype: datetime
        """
        return self._last_cycle_start

    @last_cycle_start.setter
    def last_cycle_start(self, last_cycle_start):
        """
        Sets the last_cycle_start of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        last_cycle_start string

        :param last_cycle_start: The last_cycle_start of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :type: datetime
        """

        self._last_cycle_start = last_cycle_start

    @property
    def latitude(self):
        """
        Gets the latitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        latitude number

        :return: The latitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        latitude number

        :param latitude: The latitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :type: float
        """
        if latitude is None:
            raise ValueError("Invalid value for `latitude`, must not be `None`")

        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        longitude number

        :return: The longitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        longitude number

        :param longitude: The longitude of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :type: float
        """
        if longitude is None:
            raise ValueError("Invalid value for `longitude`, must not be `None`")

        self._longitude = longitude

    @property
    def pin_id(self):
        """
        Gets the pin_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        pin_id integer

        :return: The pin_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :rtype: int
        """
        return self._pin_id

    @pin_id.setter
    def pin_id(self, pin_id):
        """
        Sets the pin_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        pin_id integer

        :param pin_id: The pin_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :type: int
        """
        if pin_id is None:
            raise ValueError("Invalid value for `pin_id`, must not be `None`")

        self._pin_id = pin_id

    @property
    def schematic_id(self):
        """
        Gets the schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        schematic_id integer

        :return: The schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :rtype: int
        """
        return self._schematic_id

    @schematic_id.setter
    def schematic_id(self, schematic_id):
        """
        Sets the schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        schematic_id integer

        :param schematic_id: The schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :type: int
        """

        self._schematic_id = schematic_id

    @property
    def type_id(self):
        """
        Gets the type_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        type_id integer

        :return: The type_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        type_id integer

        :param type_id: The type_id of this GetCharactersCharacterIdPlanetsPlanetIdPin.
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")

        self._type_id = type_id

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
        if not isinstance(other, GetCharactersCharacterIdPlanetsPlanetIdPin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
