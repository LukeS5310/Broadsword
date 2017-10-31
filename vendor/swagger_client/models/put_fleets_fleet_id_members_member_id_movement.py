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


class PutFleetsFleetIdMembersMemberIdMovement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, role=None, squad_id=None, wing_id=None):
        """
        PutFleetsFleetIdMembersMemberIdMovement - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'role': 'str',
            'squad_id': 'int',
            'wing_id': 'int'
        }

        self.attribute_map = {
            'role': 'role',
            'squad_id': 'squad_id',
            'wing_id': 'wing_id'
        }

        self._role = role
        self._squad_id = squad_id
        self._wing_id = wing_id

    @property
    def role(self):
        """
        Gets the role of this PutFleetsFleetIdMembersMemberIdMovement.
        If a character is moved to the `fleet_commander` role, neither `wing_id` or `squad_id` should be specified. If a character is moved to the `wing_commander` role, only `wing_id` should be specified. If a character is moved to the `squad_commander` role, both `wing_id` and `squad_id` should be specified. If a character is moved to the `squad_member` role, both `wing_id` and `squad_id` should be specified.

        :return: The role of this PutFleetsFleetIdMembersMemberIdMovement.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this PutFleetsFleetIdMembersMemberIdMovement.
        If a character is moved to the `fleet_commander` role, neither `wing_id` or `squad_id` should be specified. If a character is moved to the `wing_commander` role, only `wing_id` should be specified. If a character is moved to the `squad_commander` role, both `wing_id` and `squad_id` should be specified. If a character is moved to the `squad_member` role, both `wing_id` and `squad_id` should be specified.

        :param role: The role of this PutFleetsFleetIdMembersMemberIdMovement.
        :type: str
        """
        allowed_values = ["fleet_commander", "wing_commander", "squad_commander", "squad_member"]
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def squad_id(self):
        """
        Gets the squad_id of this PutFleetsFleetIdMembersMemberIdMovement.
        squad_id integer

        :return: The squad_id of this PutFleetsFleetIdMembersMemberIdMovement.
        :rtype: int
        """
        return self._squad_id

    @squad_id.setter
    def squad_id(self, squad_id):
        """
        Sets the squad_id of this PutFleetsFleetIdMembersMemberIdMovement.
        squad_id integer

        :param squad_id: The squad_id of this PutFleetsFleetIdMembersMemberIdMovement.
        :type: int
        """
        if squad_id is not None and squad_id < 0:
            raise ValueError("Invalid value for `squad_id`, must be a value greater than or equal to `0`")

        self._squad_id = squad_id

    @property
    def wing_id(self):
        """
        Gets the wing_id of this PutFleetsFleetIdMembersMemberIdMovement.
        wing_id integer

        :return: The wing_id of this PutFleetsFleetIdMembersMemberIdMovement.
        :rtype: int
        """
        return self._wing_id

    @wing_id.setter
    def wing_id(self, wing_id):
        """
        Sets the wing_id of this PutFleetsFleetIdMembersMemberIdMovement.
        wing_id integer

        :param wing_id: The wing_id of this PutFleetsFleetIdMembersMemberIdMovement.
        :type: int
        """
        if wing_id is not None and wing_id < 0:
            raise ValueError("Invalid value for `wing_id`, must be a value greater than or equal to `0`")

        self._wing_id = wing_id

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
        if not isinstance(other, PutFleetsFleetIdMembersMemberIdMovement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
