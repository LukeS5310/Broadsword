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


class GetCorporationsCorporationIdWalletsDivisionTransactions200Ok(object):
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
        'transaction_id': 'int',
        'date': 'datetime',
        'type_id': 'int',
        'location_id': 'int',
        'unit_price': 'float',
        'quantity': 'int',
        'client_id': 'int',
        'is_buy': 'bool',
        'journal_ref_id': 'int'
    }

    attribute_map = {
        'transaction_id': 'transaction_id',
        'date': 'date',
        'type_id': 'type_id',
        'location_id': 'location_id',
        'unit_price': 'unit_price',
        'quantity': 'quantity',
        'client_id': 'client_id',
        'is_buy': 'is_buy',
        'journal_ref_id': 'journal_ref_id'
    }

    def __init__(self, transaction_id=None, date=None, type_id=None, location_id=None, unit_price=None, quantity=None, client_id=None, is_buy=None, journal_ref_id=None):
        """
        GetCorporationsCorporationIdWalletsDivisionTransactions200Ok - a model defined in Swagger
        """

        self._transaction_id = None
        self._date = None
        self._type_id = None
        self._location_id = None
        self._unit_price = None
        self._quantity = None
        self._client_id = None
        self._is_buy = None
        self._journal_ref_id = None
        self.discriminator = None

        self.transaction_id = transaction_id
        self.date = date
        self.type_id = type_id
        self.location_id = location_id
        self.unit_price = unit_price
        self.quantity = quantity
        self.client_id = client_id
        self.is_buy = is_buy
        self.journal_ref_id = journal_ref_id

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        Unique transaction ID

        :return: The transaction_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        Unique transaction ID

        :param transaction_id: The transaction_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :type: int
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")

        self._transaction_id = transaction_id

    @property
    def date(self):
        """
        Gets the date of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        Date and time of transaction

        :return: The date of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        Date and time of transaction

        :param date: The date of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :type: datetime
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")

        self._date = date

    @property
    def type_id(self):
        """
        Gets the type_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        type_id integer

        :return: The type_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        type_id integer

        :param type_id: The type_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")

        self._type_id = type_id

    @property
    def location_id(self):
        """
        Gets the location_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        location_id integer

        :return: The location_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        location_id integer

        :param location_id: The location_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")

        self._location_id = location_id

    @property
    def unit_price(self):
        """
        Gets the unit_price of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        Amount paid per unit

        :return: The unit_price of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """
        Sets the unit_price of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        Amount paid per unit

        :param unit_price: The unit_price of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :type: float
        """
        if unit_price is None:
            raise ValueError("Invalid value for `unit_price`, must not be `None`")

        self._unit_price = unit_price

    @property
    def quantity(self):
        """
        Gets the quantity of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        quantity integer

        :return: The quantity of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        quantity integer

        :param quantity: The quantity of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity

    @property
    def client_id(self):
        """
        Gets the client_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        client_id integer

        :return: The client_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        client_id integer

        :param client_id: The client_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :type: int
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")

        self._client_id = client_id

    @property
    def is_buy(self):
        """
        Gets the is_buy of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        is_buy boolean

        :return: The is_buy of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :rtype: bool
        """
        return self._is_buy

    @is_buy.setter
    def is_buy(self, is_buy):
        """
        Sets the is_buy of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        is_buy boolean

        :param is_buy: The is_buy of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :type: bool
        """
        if is_buy is None:
            raise ValueError("Invalid value for `is_buy`, must not be `None`")

        self._is_buy = is_buy

    @property
    def journal_ref_id(self):
        """
        Gets the journal_ref_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        journal_ref_id integer

        :return: The journal_ref_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :rtype: int
        """
        return self._journal_ref_id

    @journal_ref_id.setter
    def journal_ref_id(self, journal_ref_id):
        """
        Sets the journal_ref_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        journal_ref_id integer

        :param journal_ref_id: The journal_ref_id of this GetCorporationsCorporationIdWalletsDivisionTransactions200Ok.
        :type: int
        """
        if journal_ref_id is None:
            raise ValueError("Invalid value for `journal_ref_id`, must not be `None`")

        self._journal_ref_id = journal_ref_id

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
        if not isinstance(other, GetCorporationsCorporationIdWalletsDivisionTransactions200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
