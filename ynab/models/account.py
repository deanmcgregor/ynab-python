# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Account(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'on_budget': 'bool',
        'closed': 'bool',
        'note': 'str',
        'balance': 'int',
        'cleared_balance': 'int',
        'uncleared_balance': 'int',
        'transfer_payee_id': 'str',
        'direct_import_linked': 'bool',
        'direct_import_in_error': 'bool',
        'deleted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'on_budget': 'on_budget',
        'closed': 'closed',
        'note': 'note',
        'balance': 'balance',
        'cleared_balance': 'cleared_balance',
        'uncleared_balance': 'uncleared_balance',
        'transfer_payee_id': 'transfer_payee_id',
        'direct_import_linked': 'direct_import_linked',
        'direct_import_in_error': 'direct_import_in_error',
        'deleted': 'deleted'
    }

    def __init__(self, id=None, name=None, type=None, on_budget=None, closed=None, note=None, balance=None, cleared_balance=None, uncleared_balance=None, transfer_payee_id=None, direct_import_linked=None, direct_import_in_error=None, deleted=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._type = None
        self._on_budget = None
        self._closed = None
        self._note = None
        self._balance = None
        self._cleared_balance = None
        self._uncleared_balance = None
        self._transfer_payee_id = None
        self._direct_import_linked = None
        self._direct_import_in_error = None
        self._deleted = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.type = type
        self.on_budget = on_budget
        self.closed = closed
        if note is not None:
            self.note = note
        self.balance = balance
        self.cleared_balance = cleared_balance
        self.uncleared_balance = uncleared_balance
        self.transfer_payee_id = transfer_payee_id
        if direct_import_linked is not None:
            self.direct_import_linked = direct_import_linked
        if direct_import_in_error is not None:
            self.direct_import_in_error = direct_import_in_error
        self.deleted = deleted

    @property
    def id(self):
        """Gets the id of this Account.  # noqa: E501


        :return: The id of this Account.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Account.


        :param id: The id of this Account.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Account.  # noqa: E501


        :return: The name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Account.


        :param name: The name of this Account.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Account.  # noqa: E501

        The type of account. Note: payPal, merchantAccount, investmentAccount, and mortgage types have been deprecated and will be removed in the future.  # noqa: E501

        :return: The type of this Account.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Account.

        The type of account. Note: payPal, merchantAccount, investmentAccount, and mortgage types have been deprecated and will be removed in the future.  # noqa: E501

        :param type: The type of this Account.  # noqa: E501
        :type: str
        """
        allowed_values = ["checking", "savings", "cash", "creditCard", "lineOfCredit", "otherAsset", "otherLiability", "payPal", "merchantAccount", "investmentAccount", "mortgage"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def on_budget(self):
        """Gets the on_budget of this Account.  # noqa: E501

        Whether this account is on budget or not  # noqa: E501

        :return: The on_budget of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._on_budget

    @on_budget.setter
    def on_budget(self, on_budget):
        """Sets the on_budget of this Account.

        Whether this account is on budget or not  # noqa: E501

        :param on_budget: The on_budget of this Account.  # noqa: E501
        :type: bool
        """

        self._on_budget = on_budget

    @property
    def closed(self):
        """Gets the closed of this Account.  # noqa: E501

        Whether this account is closed or not  # noqa: E501

        :return: The closed of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this Account.

        Whether this account is closed or not  # noqa: E501

        :param closed: The closed of this Account.  # noqa: E501
        :type: bool
        """

        self._closed = closed

    @property
    def note(self):
        """Gets the note of this Account.  # noqa: E501


        :return: The note of this Account.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Account.


        :param note: The note of this Account.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def balance(self):
        """Gets the balance of this Account.  # noqa: E501

        The current balance of the account in milliunits format  # noqa: E501

        :return: The balance of this Account.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Account.

        The current balance of the account in milliunits format  # noqa: E501

        :param balance: The balance of this Account.  # noqa: E501
        :type: int
        """

        self._balance = balance

    @property
    def cleared_balance(self):
        """Gets the cleared_balance of this Account.  # noqa: E501

        The current cleared balance of the account in milliunits format  # noqa: E501

        :return: The cleared_balance of this Account.  # noqa: E501
        :rtype: int
        """
        return self._cleared_balance

    @cleared_balance.setter
    def cleared_balance(self, cleared_balance):
        """Sets the cleared_balance of this Account.

        The current cleared balance of the account in milliunits format  # noqa: E501

        :param cleared_balance: The cleared_balance of this Account.  # noqa: E501
        :type: int
        """

        self._cleared_balance = cleared_balance

    @property
    def uncleared_balance(self):
        """Gets the uncleared_balance of this Account.  # noqa: E501

        The current uncleared balance of the account in milliunits format  # noqa: E501

        :return: The uncleared_balance of this Account.  # noqa: E501
        :rtype: int
        """
        return self._uncleared_balance

    @uncleared_balance.setter
    def uncleared_balance(self, uncleared_balance):
        """Sets the uncleared_balance of this Account.

        The current uncleared balance of the account in milliunits format  # noqa: E501

        :param uncleared_balance: The uncleared_balance of this Account.  # noqa: E501
        :type: int
        """

        self._uncleared_balance = uncleared_balance

    @property
    def transfer_payee_id(self):
        """Gets the transfer_payee_id of this Account.  # noqa: E501

        The payee id which should be used when transferring to this account  # noqa: E501

        :return: The transfer_payee_id of this Account.  # noqa: E501
        :rtype: str
        """
        return self._transfer_payee_id

    @transfer_payee_id.setter
    def transfer_payee_id(self, transfer_payee_id):
        """Sets the transfer_payee_id of this Account.

        The payee id which should be used when transferring to this account  # noqa: E501

        :param transfer_payee_id: The transfer_payee_id of this Account.  # noqa: E501
        :type: str
        """

        self._transfer_payee_id = transfer_payee_id

    @property
    def direct_import_linked(self):
        """Gets the direct_import_linked of this Account.  # noqa: E501

        Whether or not the account is linked to a financial institution for automatic transaction import.  # noqa: E501

        :return: The direct_import_linked of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._direct_import_linked

    @direct_import_linked.setter
    def direct_import_linked(self, direct_import_linked):
        """Sets the direct_import_linked of this Account.

        Whether or not the account is linked to a financial institution for automatic transaction import.  # noqa: E501

        :param direct_import_linked: The direct_import_linked of this Account.  # noqa: E501
        :type: bool
        """

        self._direct_import_linked = direct_import_linked

    @property
    def direct_import_in_error(self):
        """Gets the direct_import_in_error of this Account.  # noqa: E501

        If an account linked to a financial institution (direct_import_linked=true) and the linked connection is not in a healthy state, this will be true.  # noqa: E501

        :return: The direct_import_in_error of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._direct_import_in_error

    @direct_import_in_error.setter
    def direct_import_in_error(self, direct_import_in_error):
        """Sets the direct_import_in_error of this Account.

        If an account linked to a financial institution (direct_import_linked=true) and the linked connection is not in a healthy state, this will be true.  # noqa: E501

        :param direct_import_in_error: The direct_import_in_error of this Account.  # noqa: E501
        :type: bool
        """

        self._direct_import_in_error = direct_import_in_error

    @property
    def deleted(self):
        """Gets the deleted of this Account.  # noqa: E501

        Whether or not the account has been deleted.  Deleted accounts will only be included in delta requests.  # noqa: E501

        :return: The deleted of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Account.

        Whether or not the account has been deleted.  Deleted accounts will only be included in delta requests.  # noqa: E501

        :param deleted: The deleted of this Account.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Account, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
