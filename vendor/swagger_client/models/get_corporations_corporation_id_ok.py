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


class GetCorporationsCorporationIdOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, alliance_id=None, ceo_id=None, corporation_description=None, corporation_name=None, creation_date=None, creator_id=None, faction=None, member_count=None, tax_rate=None, ticker=None, url=None):
        """
        GetCorporationsCorporationIdOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alliance_id': 'int',
            'ceo_id': 'int',
            'corporation_description': 'str',
            'corporation_name': 'str',
            'creation_date': 'datetime',
            'creator_id': 'int',
            'faction': 'str',
            'member_count': 'int',
            'tax_rate': 'float',
            'ticker': 'str',
            'url': 'str'
        }

        self.attribute_map = {
            'alliance_id': 'alliance_id',
            'ceo_id': 'ceo_id',
            'corporation_description': 'corporation_description',
            'corporation_name': 'corporation_name',
            'creation_date': 'creation_date',
            'creator_id': 'creator_id',
            'faction': 'faction',
            'member_count': 'member_count',
            'tax_rate': 'tax_rate',
            'ticker': 'ticker',
            'url': 'url'
        }

        self._alliance_id = alliance_id
        self._ceo_id = ceo_id
        self._corporation_description = corporation_description
        self._corporation_name = corporation_name
        self._creation_date = creation_date
        self._creator_id = creator_id
        self._faction = faction
        self._member_count = member_count
        self._tax_rate = tax_rate
        self._ticker = ticker
        self._url = url

    @property
    def alliance_id(self):
        """
        Gets the alliance_id of this GetCorporationsCorporationIdOk.
        id of alliance that corporation is a member of, if any

        :return: The alliance_id of this GetCorporationsCorporationIdOk.
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """
        Sets the alliance_id of this GetCorporationsCorporationIdOk.
        id of alliance that corporation is a member of, if any

        :param alliance_id: The alliance_id of this GetCorporationsCorporationIdOk.
        :type: int
        """

        self._alliance_id = alliance_id

    @property
    def ceo_id(self):
        """
        Gets the ceo_id of this GetCorporationsCorporationIdOk.
        ceo_id integer

        :return: The ceo_id of this GetCorporationsCorporationIdOk.
        :rtype: int
        """
        return self._ceo_id

    @ceo_id.setter
    def ceo_id(self, ceo_id):
        """
        Sets the ceo_id of this GetCorporationsCorporationIdOk.
        ceo_id integer

        :param ceo_id: The ceo_id of this GetCorporationsCorporationIdOk.
        :type: int
        """
        if ceo_id is None:
            raise ValueError("Invalid value for `ceo_id`, must not be `None`")

        self._ceo_id = ceo_id

    @property
    def corporation_description(self):
        """
        Gets the corporation_description of this GetCorporationsCorporationIdOk.
        corporation_description string

        :return: The corporation_description of this GetCorporationsCorporationIdOk.
        :rtype: str
        """
        return self._corporation_description

    @corporation_description.setter
    def corporation_description(self, corporation_description):
        """
        Sets the corporation_description of this GetCorporationsCorporationIdOk.
        corporation_description string

        :param corporation_description: The corporation_description of this GetCorporationsCorporationIdOk.
        :type: str
        """
        if corporation_description is None:
            raise ValueError("Invalid value for `corporation_description`, must not be `None`")

        self._corporation_description = corporation_description

    @property
    def corporation_name(self):
        """
        Gets the corporation_name of this GetCorporationsCorporationIdOk.
        the full name of the corporation

        :return: The corporation_name of this GetCorporationsCorporationIdOk.
        :rtype: str
        """
        return self._corporation_name

    @corporation_name.setter
    def corporation_name(self, corporation_name):
        """
        Sets the corporation_name of this GetCorporationsCorporationIdOk.
        the full name of the corporation

        :param corporation_name: The corporation_name of this GetCorporationsCorporationIdOk.
        :type: str
        """
        if corporation_name is None:
            raise ValueError("Invalid value for `corporation_name`, must not be `None`")

        self._corporation_name = corporation_name

    @property
    def creation_date(self):
        """
        Gets the creation_date of this GetCorporationsCorporationIdOk.
        creation_date string

        :return: The creation_date of this GetCorporationsCorporationIdOk.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this GetCorporationsCorporationIdOk.
        creation_date string

        :param creation_date: The creation_date of this GetCorporationsCorporationIdOk.
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def creator_id(self):
        """
        Gets the creator_id of this GetCorporationsCorporationIdOk.
        creator_id integer

        :return: The creator_id of this GetCorporationsCorporationIdOk.
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """
        Sets the creator_id of this GetCorporationsCorporationIdOk.
        creator_id integer

        :param creator_id: The creator_id of this GetCorporationsCorporationIdOk.
        :type: int
        """
        if creator_id is None:
            raise ValueError("Invalid value for `creator_id`, must not be `None`")

        self._creator_id = creator_id

    @property
    def faction(self):
        """
        Gets the faction of this GetCorporationsCorporationIdOk.
        faction string

        :return: The faction of this GetCorporationsCorporationIdOk.
        :rtype: str
        """
        return self._faction

    @faction.setter
    def faction(self, faction):
        """
        Sets the faction of this GetCorporationsCorporationIdOk.
        faction string

        :param faction: The faction of this GetCorporationsCorporationIdOk.
        :type: str
        """
        allowed_values = ["Minmatar", "Gallente", "Caldari", "Amarr"]
        if faction not in allowed_values:
            raise ValueError(
                "Invalid value for `faction` ({0}), must be one of {1}"
                .format(faction, allowed_values)
            )

        self._faction = faction

    @property
    def member_count(self):
        """
        Gets the member_count of this GetCorporationsCorporationIdOk.
        member_count integer

        :return: The member_count of this GetCorporationsCorporationIdOk.
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """
        Sets the member_count of this GetCorporationsCorporationIdOk.
        member_count integer

        :param member_count: The member_count of this GetCorporationsCorporationIdOk.
        :type: int
        """
        if member_count is None:
            raise ValueError("Invalid value for `member_count`, must not be `None`")

        self._member_count = member_count

    @property
    def tax_rate(self):
        """
        Gets the tax_rate of this GetCorporationsCorporationIdOk.
        tax_rate number

        :return: The tax_rate of this GetCorporationsCorporationIdOk.
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """
        Sets the tax_rate of this GetCorporationsCorporationIdOk.
        tax_rate number

        :param tax_rate: The tax_rate of this GetCorporationsCorporationIdOk.
        :type: float
        """
        if tax_rate is None:
            raise ValueError("Invalid value for `tax_rate`, must not be `None`")
        if tax_rate is not None and tax_rate > 1:
            raise ValueError("Invalid value for `tax_rate`, must be a value less than or equal to `1`")
        if tax_rate is not None and tax_rate < 0:
            raise ValueError("Invalid value for `tax_rate`, must be a value greater than or equal to `0`")

        self._tax_rate = tax_rate

    @property
    def ticker(self):
        """
        Gets the ticker of this GetCorporationsCorporationIdOk.
        the short name of the corporation

        :return: The ticker of this GetCorporationsCorporationIdOk.
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """
        Sets the ticker of this GetCorporationsCorporationIdOk.
        the short name of the corporation

        :param ticker: The ticker of this GetCorporationsCorporationIdOk.
        :type: str
        """
        if ticker is None:
            raise ValueError("Invalid value for `ticker`, must not be `None`")

        self._ticker = ticker

    @property
    def url(self):
        """
        Gets the url of this GetCorporationsCorporationIdOk.
        url string

        :return: The url of this GetCorporationsCorporationIdOk.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this GetCorporationsCorporationIdOk.
        url string

        :param url: The url of this GetCorporationsCorporationIdOk.
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url

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
        if not isinstance(other, GetCorporationsCorporationIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
