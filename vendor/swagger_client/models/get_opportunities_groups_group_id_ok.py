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


class GetOpportunitiesGroupsGroupIdOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, connected_groups=None, description=None, group_id=None, name=None, notification=None, required_tasks=None):
        """
        GetOpportunitiesGroupsGroupIdOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'connected_groups': 'list[int]',
            'description': 'str',
            'group_id': 'int',
            'name': 'str',
            'notification': 'str',
            'required_tasks': 'list[int]'
        }

        self.attribute_map = {
            'connected_groups': 'connected_groups',
            'description': 'description',
            'group_id': 'group_id',
            'name': 'name',
            'notification': 'notification',
            'required_tasks': 'required_tasks'
        }

        self._connected_groups = connected_groups
        self._description = description
        self._group_id = group_id
        self._name = name
        self._notification = notification
        self._required_tasks = required_tasks

    @property
    def connected_groups(self):
        """
        Gets the connected_groups of this GetOpportunitiesGroupsGroupIdOk.
        The groups that are connected to this group on the opportunities map

        :return: The connected_groups of this GetOpportunitiesGroupsGroupIdOk.
        :rtype: list[int]
        """
        return self._connected_groups

    @connected_groups.setter
    def connected_groups(self, connected_groups):
        """
        Sets the connected_groups of this GetOpportunitiesGroupsGroupIdOk.
        The groups that are connected to this group on the opportunities map

        :param connected_groups: The connected_groups of this GetOpportunitiesGroupsGroupIdOk.
        :type: list[int]
        """
        if connected_groups is None:
            raise ValueError("Invalid value for `connected_groups`, must not be `None`")

        self._connected_groups = connected_groups

    @property
    def description(self):
        """
        Gets the description of this GetOpportunitiesGroupsGroupIdOk.
        description string

        :return: The description of this GetOpportunitiesGroupsGroupIdOk.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GetOpportunitiesGroupsGroupIdOk.
        description string

        :param description: The description of this GetOpportunitiesGroupsGroupIdOk.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def group_id(self):
        """
        Gets the group_id of this GetOpportunitiesGroupsGroupIdOk.
        group_id integer

        :return: The group_id of this GetOpportunitiesGroupsGroupIdOk.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this GetOpportunitiesGroupsGroupIdOk.
        group_id integer

        :param group_id: The group_id of this GetOpportunitiesGroupsGroupIdOk.
        :type: int
        """
        if group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")

        self._group_id = group_id

    @property
    def name(self):
        """
        Gets the name of this GetOpportunitiesGroupsGroupIdOk.
        name string

        :return: The name of this GetOpportunitiesGroupsGroupIdOk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetOpportunitiesGroupsGroupIdOk.
        name string

        :param name: The name of this GetOpportunitiesGroupsGroupIdOk.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def notification(self):
        """
        Gets the notification of this GetOpportunitiesGroupsGroupIdOk.
        notification string

        :return: The notification of this GetOpportunitiesGroupsGroupIdOk.
        :rtype: str
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """
        Sets the notification of this GetOpportunitiesGroupsGroupIdOk.
        notification string

        :param notification: The notification of this GetOpportunitiesGroupsGroupIdOk.
        :type: str
        """
        if notification is None:
            raise ValueError("Invalid value for `notification`, must not be `None`")

        self._notification = notification

    @property
    def required_tasks(self):
        """
        Gets the required_tasks of this GetOpportunitiesGroupsGroupIdOk.
        Tasks need to complete for this group

        :return: The required_tasks of this GetOpportunitiesGroupsGroupIdOk.
        :rtype: list[int]
        """
        return self._required_tasks

    @required_tasks.setter
    def required_tasks(self, required_tasks):
        """
        Sets the required_tasks of this GetOpportunitiesGroupsGroupIdOk.
        Tasks need to complete for this group

        :param required_tasks: The required_tasks of this GetOpportunitiesGroupsGroupIdOk.
        :type: list[int]
        """
        if required_tasks is None:
            raise ValueError("Invalid value for `required_tasks`, must not be `None`")

        self._required_tasks = required_tasks

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
        if not isinstance(other, GetOpportunitiesGroupsGroupIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
