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


class GetCorporationsCorporationIdOutpostsOutpostIdOk(object):
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
        'owner_id': 'int',
        'system_id': 'int',
        'docking_cost_per_ship_volume': 'float',
        'office_rental_cost': 'int',
        'type_id': 'int',
        'reprocessing_efficiency': 'float',
        'reprocessing_station_take': 'float',
        'standing_owner_id': 'int',
        'coordinates': 'GetCorporationsCorporationIdOutpostsOutpostIdCoordinates',
        'services': 'list[GetCorporationsCorporationIdOutpostsOutpostIdService]'
    }

    attribute_map = {
        'owner_id': 'owner_id',
        'system_id': 'system_id',
        'docking_cost_per_ship_volume': 'docking_cost_per_ship_volume',
        'office_rental_cost': 'office_rental_cost',
        'type_id': 'type_id',
        'reprocessing_efficiency': 'reprocessing_efficiency',
        'reprocessing_station_take': 'reprocessing_station_take',
        'standing_owner_id': 'standing_owner_id',
        'coordinates': 'coordinates',
        'services': 'services'
    }

    def __init__(self, owner_id=None, system_id=None, docking_cost_per_ship_volume=None, office_rental_cost=None, type_id=None, reprocessing_efficiency=None, reprocessing_station_take=None, standing_owner_id=None, coordinates=None, services=None):
        """
        GetCorporationsCorporationIdOutpostsOutpostIdOk - a model defined in Swagger
        """

        self._owner_id = None
        self._system_id = None
        self._docking_cost_per_ship_volume = None
        self._office_rental_cost = None
        self._type_id = None
        self._reprocessing_efficiency = None
        self._reprocessing_station_take = None
        self._standing_owner_id = None
        self._coordinates = None
        self._services = None
        self.discriminator = None

        self.owner_id = owner_id
        self.system_id = system_id
        self.docking_cost_per_ship_volume = docking_cost_per_ship_volume
        self.office_rental_cost = office_rental_cost
        self.type_id = type_id
        self.reprocessing_efficiency = reprocessing_efficiency
        self.reprocessing_station_take = reprocessing_station_take
        self.standing_owner_id = standing_owner_id
        self.coordinates = coordinates
        self.services = services

    @property
    def owner_id(self):
        """
        Gets the owner_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        The entity that owns the station (e.g. the entity whose logo is on the station services bar)

        :return: The owner_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        The entity that owns the station (e.g. the entity whose logo is on the station services bar)

        :param owner_id: The owner_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :type: int
        """
        if owner_id is None:
            raise ValueError("Invalid value for `owner_id`, must not be `None`")

        self._owner_id = owner_id

    @property
    def system_id(self):
        """
        Gets the system_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        The ID of the solar system the outpost rests in

        :return: The system_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """
        Sets the system_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        The ID of the solar system the outpost rests in

        :param system_id: The system_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :type: int
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")

        self._system_id = system_id

    @property
    def docking_cost_per_ship_volume(self):
        """
        Gets the docking_cost_per_ship_volume of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        docking_cost_per_ship_volume number

        :return: The docking_cost_per_ship_volume of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :rtype: float
        """
        return self._docking_cost_per_ship_volume

    @docking_cost_per_ship_volume.setter
    def docking_cost_per_ship_volume(self, docking_cost_per_ship_volume):
        """
        Sets the docking_cost_per_ship_volume of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        docking_cost_per_ship_volume number

        :param docking_cost_per_ship_volume: The docking_cost_per_ship_volume of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :type: float
        """
        if docking_cost_per_ship_volume is None:
            raise ValueError("Invalid value for `docking_cost_per_ship_volume`, must not be `None`")

        self._docking_cost_per_ship_volume = docking_cost_per_ship_volume

    @property
    def office_rental_cost(self):
        """
        Gets the office_rental_cost of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        office_rental_cost integer

        :return: The office_rental_cost of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :rtype: int
        """
        return self._office_rental_cost

    @office_rental_cost.setter
    def office_rental_cost(self, office_rental_cost):
        """
        Sets the office_rental_cost of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        office_rental_cost integer

        :param office_rental_cost: The office_rental_cost of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :type: int
        """
        if office_rental_cost is None:
            raise ValueError("Invalid value for `office_rental_cost`, must not be `None`")

        self._office_rental_cost = office_rental_cost

    @property
    def type_id(self):
        """
        Gets the type_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        The type ID of the given outpost

        :return: The type_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        The type ID of the given outpost

        :param type_id: The type_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")

        self._type_id = type_id

    @property
    def reprocessing_efficiency(self):
        """
        Gets the reprocessing_efficiency of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        reprocessing_efficiency number

        :return: The reprocessing_efficiency of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :rtype: float
        """
        return self._reprocessing_efficiency

    @reprocessing_efficiency.setter
    def reprocessing_efficiency(self, reprocessing_efficiency):
        """
        Sets the reprocessing_efficiency of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        reprocessing_efficiency number

        :param reprocessing_efficiency: The reprocessing_efficiency of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :type: float
        """
        if reprocessing_efficiency is None:
            raise ValueError("Invalid value for `reprocessing_efficiency`, must not be `None`")

        self._reprocessing_efficiency = reprocessing_efficiency

    @property
    def reprocessing_station_take(self):
        """
        Gets the reprocessing_station_take of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        reprocessing_station_take number

        :return: The reprocessing_station_take of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :rtype: float
        """
        return self._reprocessing_station_take

    @reprocessing_station_take.setter
    def reprocessing_station_take(self, reprocessing_station_take):
        """
        Sets the reprocessing_station_take of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        reprocessing_station_take number

        :param reprocessing_station_take: The reprocessing_station_take of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :type: float
        """
        if reprocessing_station_take is None:
            raise ValueError("Invalid value for `reprocessing_station_take`, must not be `None`")

        self._reprocessing_station_take = reprocessing_station_take

    @property
    def standing_owner_id(self):
        """
        Gets the standing_owner_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        The owner ID that sets the ability for someone to dock based on standings.

        :return: The standing_owner_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :rtype: int
        """
        return self._standing_owner_id

    @standing_owner_id.setter
    def standing_owner_id(self, standing_owner_id):
        """
        Sets the standing_owner_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        The owner ID that sets the ability for someone to dock based on standings.

        :param standing_owner_id: The standing_owner_id of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :type: int
        """
        if standing_owner_id is None:
            raise ValueError("Invalid value for `standing_owner_id`, must not be `None`")

        self._standing_owner_id = standing_owner_id

    @property
    def coordinates(self):
        """
        Gets the coordinates of this GetCorporationsCorporationIdOutpostsOutpostIdOk.

        :return: The coordinates of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :rtype: GetCorporationsCorporationIdOutpostsOutpostIdCoordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """
        Sets the coordinates of this GetCorporationsCorporationIdOutpostsOutpostIdOk.

        :param coordinates: The coordinates of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :type: GetCorporationsCorporationIdOutpostsOutpostIdCoordinates
        """
        if coordinates is None:
            raise ValueError("Invalid value for `coordinates`, must not be `None`")

        self._coordinates = coordinates

    @property
    def services(self):
        """
        Gets the services of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        A list of services the given outpost provides

        :return: The services of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :rtype: list[GetCorporationsCorporationIdOutpostsOutpostIdService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        A list of services the given outpost provides

        :param services: The services of this GetCorporationsCorporationIdOutpostsOutpostIdOk.
        :type: list[GetCorporationsCorporationIdOutpostsOutpostIdService]
        """
        if services is None:
            raise ValueError("Invalid value for `services`, must not be `None`")

        self._services = services

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
        if not isinstance(other, GetCorporationsCorporationIdOutpostsOutpostIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
