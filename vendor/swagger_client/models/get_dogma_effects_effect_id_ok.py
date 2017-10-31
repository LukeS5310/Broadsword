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


class GetDogmaEffectsEffectIdOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, description=None, disallow_auto_repeat=None, discharge_attribute_id=None, display_name=None, duration_attribute_id=None, effect_category=None, effect_id=None, electronic_chance=None, falloff_attribute_id=None, icon_id=None, is_assistance=None, is_offensive=None, is_warp_safe=None, modifiers=None, name=None, post_expression=None, pre_expression=None, published=None, range_attribute_id=None, range_chance=None, tracking_speed_attribute_id=None):
        """
        GetDogmaEffectsEffectIdOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'disallow_auto_repeat': 'bool',
            'discharge_attribute_id': 'int',
            'display_name': 'str',
            'duration_attribute_id': 'int',
            'effect_category': 'int',
            'effect_id': 'int',
            'electronic_chance': 'bool',
            'falloff_attribute_id': 'int',
            'icon_id': 'int',
            'is_assistance': 'bool',
            'is_offensive': 'bool',
            'is_warp_safe': 'bool',
            'modifiers': 'list[GetDogmaEffectsEffectIdModifier]',
            'name': 'str',
            'post_expression': 'int',
            'pre_expression': 'int',
            'published': 'bool',
            'range_attribute_id': 'int',
            'range_chance': 'bool',
            'tracking_speed_attribute_id': 'int'
        }

        self.attribute_map = {
            'description': 'description',
            'disallow_auto_repeat': 'disallow_auto_repeat',
            'discharge_attribute_id': 'discharge_attribute_id',
            'display_name': 'display_name',
            'duration_attribute_id': 'duration_attribute_id',
            'effect_category': 'effect_category',
            'effect_id': 'effect_id',
            'electronic_chance': 'electronic_chance',
            'falloff_attribute_id': 'falloff_attribute_id',
            'icon_id': 'icon_id',
            'is_assistance': 'is_assistance',
            'is_offensive': 'is_offensive',
            'is_warp_safe': 'is_warp_safe',
            'modifiers': 'modifiers',
            'name': 'name',
            'post_expression': 'post_expression',
            'pre_expression': 'pre_expression',
            'published': 'published',
            'range_attribute_id': 'range_attribute_id',
            'range_chance': 'range_chance',
            'tracking_speed_attribute_id': 'tracking_speed_attribute_id'
        }

        self._description = description
        self._disallow_auto_repeat = disallow_auto_repeat
        self._discharge_attribute_id = discharge_attribute_id
        self._display_name = display_name
        self._duration_attribute_id = duration_attribute_id
        self._effect_category = effect_category
        self._effect_id = effect_id
        self._electronic_chance = electronic_chance
        self._falloff_attribute_id = falloff_attribute_id
        self._icon_id = icon_id
        self._is_assistance = is_assistance
        self._is_offensive = is_offensive
        self._is_warp_safe = is_warp_safe
        self._modifiers = modifiers
        self._name = name
        self._post_expression = post_expression
        self._pre_expression = pre_expression
        self._published = published
        self._range_attribute_id = range_attribute_id
        self._range_chance = range_chance
        self._tracking_speed_attribute_id = tracking_speed_attribute_id

    @property
    def description(self):
        """
        Gets the description of this GetDogmaEffectsEffectIdOk.
        description string

        :return: The description of this GetDogmaEffectsEffectIdOk.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GetDogmaEffectsEffectIdOk.
        description string

        :param description: The description of this GetDogmaEffectsEffectIdOk.
        :type: str
        """

        self._description = description

    @property
    def disallow_auto_repeat(self):
        """
        Gets the disallow_auto_repeat of this GetDogmaEffectsEffectIdOk.
        disallow_auto_repeat boolean

        :return: The disallow_auto_repeat of this GetDogmaEffectsEffectIdOk.
        :rtype: bool
        """
        return self._disallow_auto_repeat

    @disallow_auto_repeat.setter
    def disallow_auto_repeat(self, disallow_auto_repeat):
        """
        Sets the disallow_auto_repeat of this GetDogmaEffectsEffectIdOk.
        disallow_auto_repeat boolean

        :param disallow_auto_repeat: The disallow_auto_repeat of this GetDogmaEffectsEffectIdOk.
        :type: bool
        """

        self._disallow_auto_repeat = disallow_auto_repeat

    @property
    def discharge_attribute_id(self):
        """
        Gets the discharge_attribute_id of this GetDogmaEffectsEffectIdOk.
        discharge_attribute_id integer

        :return: The discharge_attribute_id of this GetDogmaEffectsEffectIdOk.
        :rtype: int
        """
        return self._discharge_attribute_id

    @discharge_attribute_id.setter
    def discharge_attribute_id(self, discharge_attribute_id):
        """
        Sets the discharge_attribute_id of this GetDogmaEffectsEffectIdOk.
        discharge_attribute_id integer

        :param discharge_attribute_id: The discharge_attribute_id of this GetDogmaEffectsEffectIdOk.
        :type: int
        """

        self._discharge_attribute_id = discharge_attribute_id

    @property
    def display_name(self):
        """
        Gets the display_name of this GetDogmaEffectsEffectIdOk.
        display_name string

        :return: The display_name of this GetDogmaEffectsEffectIdOk.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this GetDogmaEffectsEffectIdOk.
        display_name string

        :param display_name: The display_name of this GetDogmaEffectsEffectIdOk.
        :type: str
        """

        self._display_name = display_name

    @property
    def duration_attribute_id(self):
        """
        Gets the duration_attribute_id of this GetDogmaEffectsEffectIdOk.
        duration_attribute_id integer

        :return: The duration_attribute_id of this GetDogmaEffectsEffectIdOk.
        :rtype: int
        """
        return self._duration_attribute_id

    @duration_attribute_id.setter
    def duration_attribute_id(self, duration_attribute_id):
        """
        Sets the duration_attribute_id of this GetDogmaEffectsEffectIdOk.
        duration_attribute_id integer

        :param duration_attribute_id: The duration_attribute_id of this GetDogmaEffectsEffectIdOk.
        :type: int
        """

        self._duration_attribute_id = duration_attribute_id

    @property
    def effect_category(self):
        """
        Gets the effect_category of this GetDogmaEffectsEffectIdOk.
        effect_category integer

        :return: The effect_category of this GetDogmaEffectsEffectIdOk.
        :rtype: int
        """
        return self._effect_category

    @effect_category.setter
    def effect_category(self, effect_category):
        """
        Sets the effect_category of this GetDogmaEffectsEffectIdOk.
        effect_category integer

        :param effect_category: The effect_category of this GetDogmaEffectsEffectIdOk.
        :type: int
        """

        self._effect_category = effect_category

    @property
    def effect_id(self):
        """
        Gets the effect_id of this GetDogmaEffectsEffectIdOk.
        effect_id integer

        :return: The effect_id of this GetDogmaEffectsEffectIdOk.
        :rtype: int
        """
        return self._effect_id

    @effect_id.setter
    def effect_id(self, effect_id):
        """
        Sets the effect_id of this GetDogmaEffectsEffectIdOk.
        effect_id integer

        :param effect_id: The effect_id of this GetDogmaEffectsEffectIdOk.
        :type: int
        """
        if effect_id is None:
            raise ValueError("Invalid value for `effect_id`, must not be `None`")

        self._effect_id = effect_id

    @property
    def electronic_chance(self):
        """
        Gets the electronic_chance of this GetDogmaEffectsEffectIdOk.
        electronic_chance boolean

        :return: The electronic_chance of this GetDogmaEffectsEffectIdOk.
        :rtype: bool
        """
        return self._electronic_chance

    @electronic_chance.setter
    def electronic_chance(self, electronic_chance):
        """
        Sets the electronic_chance of this GetDogmaEffectsEffectIdOk.
        electronic_chance boolean

        :param electronic_chance: The electronic_chance of this GetDogmaEffectsEffectIdOk.
        :type: bool
        """

        self._electronic_chance = electronic_chance

    @property
    def falloff_attribute_id(self):
        """
        Gets the falloff_attribute_id of this GetDogmaEffectsEffectIdOk.
        falloff_attribute_id integer

        :return: The falloff_attribute_id of this GetDogmaEffectsEffectIdOk.
        :rtype: int
        """
        return self._falloff_attribute_id

    @falloff_attribute_id.setter
    def falloff_attribute_id(self, falloff_attribute_id):
        """
        Sets the falloff_attribute_id of this GetDogmaEffectsEffectIdOk.
        falloff_attribute_id integer

        :param falloff_attribute_id: The falloff_attribute_id of this GetDogmaEffectsEffectIdOk.
        :type: int
        """

        self._falloff_attribute_id = falloff_attribute_id

    @property
    def icon_id(self):
        """
        Gets the icon_id of this GetDogmaEffectsEffectIdOk.
        icon_id integer

        :return: The icon_id of this GetDogmaEffectsEffectIdOk.
        :rtype: int
        """
        return self._icon_id

    @icon_id.setter
    def icon_id(self, icon_id):
        """
        Sets the icon_id of this GetDogmaEffectsEffectIdOk.
        icon_id integer

        :param icon_id: The icon_id of this GetDogmaEffectsEffectIdOk.
        :type: int
        """

        self._icon_id = icon_id

    @property
    def is_assistance(self):
        """
        Gets the is_assistance of this GetDogmaEffectsEffectIdOk.
        is_assistance boolean

        :return: The is_assistance of this GetDogmaEffectsEffectIdOk.
        :rtype: bool
        """
        return self._is_assistance

    @is_assistance.setter
    def is_assistance(self, is_assistance):
        """
        Sets the is_assistance of this GetDogmaEffectsEffectIdOk.
        is_assistance boolean

        :param is_assistance: The is_assistance of this GetDogmaEffectsEffectIdOk.
        :type: bool
        """

        self._is_assistance = is_assistance

    @property
    def is_offensive(self):
        """
        Gets the is_offensive of this GetDogmaEffectsEffectIdOk.
        is_offensive boolean

        :return: The is_offensive of this GetDogmaEffectsEffectIdOk.
        :rtype: bool
        """
        return self._is_offensive

    @is_offensive.setter
    def is_offensive(self, is_offensive):
        """
        Sets the is_offensive of this GetDogmaEffectsEffectIdOk.
        is_offensive boolean

        :param is_offensive: The is_offensive of this GetDogmaEffectsEffectIdOk.
        :type: bool
        """

        self._is_offensive = is_offensive

    @property
    def is_warp_safe(self):
        """
        Gets the is_warp_safe of this GetDogmaEffectsEffectIdOk.
        is_warp_safe boolean

        :return: The is_warp_safe of this GetDogmaEffectsEffectIdOk.
        :rtype: bool
        """
        return self._is_warp_safe

    @is_warp_safe.setter
    def is_warp_safe(self, is_warp_safe):
        """
        Sets the is_warp_safe of this GetDogmaEffectsEffectIdOk.
        is_warp_safe boolean

        :param is_warp_safe: The is_warp_safe of this GetDogmaEffectsEffectIdOk.
        :type: bool
        """

        self._is_warp_safe = is_warp_safe

    @property
    def modifiers(self):
        """
        Gets the modifiers of this GetDogmaEffectsEffectIdOk.
        modifiers array

        :return: The modifiers of this GetDogmaEffectsEffectIdOk.
        :rtype: list[GetDogmaEffectsEffectIdModifier]
        """
        return self._modifiers

    @modifiers.setter
    def modifiers(self, modifiers):
        """
        Sets the modifiers of this GetDogmaEffectsEffectIdOk.
        modifiers array

        :param modifiers: The modifiers of this GetDogmaEffectsEffectIdOk.
        :type: list[GetDogmaEffectsEffectIdModifier]
        """

        self._modifiers = modifiers

    @property
    def name(self):
        """
        Gets the name of this GetDogmaEffectsEffectIdOk.
        name string

        :return: The name of this GetDogmaEffectsEffectIdOk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetDogmaEffectsEffectIdOk.
        name string

        :param name: The name of this GetDogmaEffectsEffectIdOk.
        :type: str
        """

        self._name = name

    @property
    def post_expression(self):
        """
        Gets the post_expression of this GetDogmaEffectsEffectIdOk.
        post_expression integer

        :return: The post_expression of this GetDogmaEffectsEffectIdOk.
        :rtype: int
        """
        return self._post_expression

    @post_expression.setter
    def post_expression(self, post_expression):
        """
        Sets the post_expression of this GetDogmaEffectsEffectIdOk.
        post_expression integer

        :param post_expression: The post_expression of this GetDogmaEffectsEffectIdOk.
        :type: int
        """

        self._post_expression = post_expression

    @property
    def pre_expression(self):
        """
        Gets the pre_expression of this GetDogmaEffectsEffectIdOk.
        pre_expression integer

        :return: The pre_expression of this GetDogmaEffectsEffectIdOk.
        :rtype: int
        """
        return self._pre_expression

    @pre_expression.setter
    def pre_expression(self, pre_expression):
        """
        Sets the pre_expression of this GetDogmaEffectsEffectIdOk.
        pre_expression integer

        :param pre_expression: The pre_expression of this GetDogmaEffectsEffectIdOk.
        :type: int
        """

        self._pre_expression = pre_expression

    @property
    def published(self):
        """
        Gets the published of this GetDogmaEffectsEffectIdOk.
        published boolean

        :return: The published of this GetDogmaEffectsEffectIdOk.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """
        Sets the published of this GetDogmaEffectsEffectIdOk.
        published boolean

        :param published: The published of this GetDogmaEffectsEffectIdOk.
        :type: bool
        """

        self._published = published

    @property
    def range_attribute_id(self):
        """
        Gets the range_attribute_id of this GetDogmaEffectsEffectIdOk.
        range_attribute_id integer

        :return: The range_attribute_id of this GetDogmaEffectsEffectIdOk.
        :rtype: int
        """
        return self._range_attribute_id

    @range_attribute_id.setter
    def range_attribute_id(self, range_attribute_id):
        """
        Sets the range_attribute_id of this GetDogmaEffectsEffectIdOk.
        range_attribute_id integer

        :param range_attribute_id: The range_attribute_id of this GetDogmaEffectsEffectIdOk.
        :type: int
        """

        self._range_attribute_id = range_attribute_id

    @property
    def range_chance(self):
        """
        Gets the range_chance of this GetDogmaEffectsEffectIdOk.
        range_chance boolean

        :return: The range_chance of this GetDogmaEffectsEffectIdOk.
        :rtype: bool
        """
        return self._range_chance

    @range_chance.setter
    def range_chance(self, range_chance):
        """
        Sets the range_chance of this GetDogmaEffectsEffectIdOk.
        range_chance boolean

        :param range_chance: The range_chance of this GetDogmaEffectsEffectIdOk.
        :type: bool
        """

        self._range_chance = range_chance

    @property
    def tracking_speed_attribute_id(self):
        """
        Gets the tracking_speed_attribute_id of this GetDogmaEffectsEffectIdOk.
        tracking_speed_attribute_id integer

        :return: The tracking_speed_attribute_id of this GetDogmaEffectsEffectIdOk.
        :rtype: int
        """
        return self._tracking_speed_attribute_id

    @tracking_speed_attribute_id.setter
    def tracking_speed_attribute_id(self, tracking_speed_attribute_id):
        """
        Sets the tracking_speed_attribute_id of this GetDogmaEffectsEffectIdOk.
        tracking_speed_attribute_id integer

        :param tracking_speed_attribute_id: The tracking_speed_attribute_id of this GetDogmaEffectsEffectIdOk.
        :type: int
        """

        self._tracking_speed_attribute_id = tracking_speed_attribute_id

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
        if not isinstance(other, GetDogmaEffectsEffectIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
