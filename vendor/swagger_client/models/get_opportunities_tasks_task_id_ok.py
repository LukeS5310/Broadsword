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


class GetOpportunitiesTasksTaskIdOk(object):
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
        'task_id': 'int',
        'name': 'str',
        'description': 'str',
        'notification': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'name': 'name',
        'description': 'description',
        'notification': 'notification'
    }

    def __init__(self, task_id=None, name=None, description=None, notification=None):
        """
        GetOpportunitiesTasksTaskIdOk - a model defined in Swagger
        """

        self._task_id = None
        self._name = None
        self._description = None
        self._notification = None
        self.discriminator = None

        self.task_id = task_id
        self.name = name
        self.description = description
        self.notification = notification

    @property
    def task_id(self):
        """
        Gets the task_id of this GetOpportunitiesTasksTaskIdOk.
        task_id integer

        :return: The task_id of this GetOpportunitiesTasksTaskIdOk.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """
        Sets the task_id of this GetOpportunitiesTasksTaskIdOk.
        task_id integer

        :param task_id: The task_id of this GetOpportunitiesTasksTaskIdOk.
        :type: int
        """
        if task_id is None:
            raise ValueError("Invalid value for `task_id`, must not be `None`")

        self._task_id = task_id

    @property
    def name(self):
        """
        Gets the name of this GetOpportunitiesTasksTaskIdOk.
        name string

        :return: The name of this GetOpportunitiesTasksTaskIdOk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetOpportunitiesTasksTaskIdOk.
        name string

        :param name: The name of this GetOpportunitiesTasksTaskIdOk.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this GetOpportunitiesTasksTaskIdOk.
        description string

        :return: The description of this GetOpportunitiesTasksTaskIdOk.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GetOpportunitiesTasksTaskIdOk.
        description string

        :param description: The description of this GetOpportunitiesTasksTaskIdOk.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def notification(self):
        """
        Gets the notification of this GetOpportunitiesTasksTaskIdOk.
        notification string

        :return: The notification of this GetOpportunitiesTasksTaskIdOk.
        :rtype: str
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """
        Sets the notification of this GetOpportunitiesTasksTaskIdOk.
        notification string

        :param notification: The notification of this GetOpportunitiesTasksTaskIdOk.
        :type: str
        """
        if notification is None:
            raise ValueError("Invalid value for `notification`, must not be `None`")

        self._notification = notification

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
        if not isinstance(other, GetOpportunitiesTasksTaskIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
