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


class GetUniverseSchematicsSchematicIdOk(object):
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
        'schematic_name': 'str',
        'cycle_time': 'int'
    }

    attribute_map = {
        'schematic_name': 'schematic_name',
        'cycle_time': 'cycle_time'
    }

    def __init__(self, schematic_name=None, cycle_time=None):
        """
        GetUniverseSchematicsSchematicIdOk - a model defined in Swagger
        """

        self._schematic_name = None
        self._cycle_time = None
        self.discriminator = None

        self.schematic_name = schematic_name
        self.cycle_time = cycle_time

    @property
    def schematic_name(self):
        """
        Gets the schematic_name of this GetUniverseSchematicsSchematicIdOk.
        schematic_name string

        :return: The schematic_name of this GetUniverseSchematicsSchematicIdOk.
        :rtype: str
        """
        return self._schematic_name

    @schematic_name.setter
    def schematic_name(self, schematic_name):
        """
        Sets the schematic_name of this GetUniverseSchematicsSchematicIdOk.
        schematic_name string

        :param schematic_name: The schematic_name of this GetUniverseSchematicsSchematicIdOk.
        :type: str
        """
        if schematic_name is None:
            raise ValueError("Invalid value for `schematic_name`, must not be `None`")

        self._schematic_name = schematic_name

    @property
    def cycle_time(self):
        """
        Gets the cycle_time of this GetUniverseSchematicsSchematicIdOk.
        Time in seconds to process a run

        :return: The cycle_time of this GetUniverseSchematicsSchematicIdOk.
        :rtype: int
        """
        return self._cycle_time

    @cycle_time.setter
    def cycle_time(self, cycle_time):
        """
        Sets the cycle_time of this GetUniverseSchematicsSchematicIdOk.
        Time in seconds to process a run

        :param cycle_time: The cycle_time of this GetUniverseSchematicsSchematicIdOk.
        :type: int
        """
        if cycle_time is None:
            raise ValueError("Invalid value for `cycle_time`, must not be `None`")

        self._cycle_time = cycle_time

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
        if not isinstance(other, GetUniverseSchematicsSchematicIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
