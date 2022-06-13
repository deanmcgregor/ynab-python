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
from ynab.models.transaction_summary import TransactionSummary  # noqa: F401,E501

class HybridTransaction(TransactionSummary):
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
        'type': 'str',
        'parent_transaction_id': 'str',
        'account_name': 'str',
        'payee_name': 'str',
        'category_name': 'str'
    }
    if hasattr(TransactionSummary, "swagger_types"):
        swagger_types.update(TransactionSummary.swagger_types)

    attribute_map = {
        'type': 'type',
        'parent_transaction_id': 'parent_transaction_id',
        'account_name': 'account_name',
        'payee_name': 'payee_name',
        'category_name': 'category_name'
    }
    if hasattr(TransactionSummary, "attribute_map"):
        attribute_map.update(TransactionSummary.attribute_map)

    def __init__(self, type=None, parent_transaction_id=None, account_name=None, payee_name=None, category_name=None, *args, **kwargs):  # noqa: E501
        """HybridTransaction - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._parent_transaction_id = None
        self._account_name = None
        self._payee_name = None
        self._category_name = None
        self.discriminator = None
        self.type = type
        if parent_transaction_id is not None:
            self.parent_transaction_id = parent_transaction_id
        self.account_name = account_name
        if payee_name is not None:
            self.payee_name = payee_name
        if category_name is not None:
            self.category_name = category_name
        TransactionSummary.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this HybridTransaction.  # noqa: E501

        Whether the hybrid transaction represents a regular transaction or a subtransaction  # noqa: E501

        :return: The type of this HybridTransaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HybridTransaction.

        Whether the hybrid transaction represents a regular transaction or a subtransaction  # noqa: E501

        :param type: The type of this HybridTransaction.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["transaction", "subtransaction"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def parent_transaction_id(self):
        """Gets the parent_transaction_id of this HybridTransaction.  # noqa: E501

        For subtransaction types, this is the id of the parent transaction.  For transaction types, this id will be always be null.  # noqa: E501

        :return: The parent_transaction_id of this HybridTransaction.  # noqa: E501
        :rtype: str
        """
        return self._parent_transaction_id

    @parent_transaction_id.setter
    def parent_transaction_id(self, parent_transaction_id):
        """Sets the parent_transaction_id of this HybridTransaction.

        For subtransaction types, this is the id of the parent transaction.  For transaction types, this id will be always be null.  # noqa: E501

        :param parent_transaction_id: The parent_transaction_id of this HybridTransaction.  # noqa: E501
        :type: str
        """

        self._parent_transaction_id = parent_transaction_id

    @property
    def account_name(self):
        """Gets the account_name of this HybridTransaction.  # noqa: E501


        :return: The account_name of this HybridTransaction.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this HybridTransaction.


        :param account_name: The account_name of this HybridTransaction.  # noqa: E501
        :type: str
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def payee_name(self):
        """Gets the payee_name of this HybridTransaction.  # noqa: E501


        :return: The payee_name of this HybridTransaction.  # noqa: E501
        :rtype: str
        """
        return self._payee_name

    @payee_name.setter
    def payee_name(self, payee_name):
        """Sets the payee_name of this HybridTransaction.


        :param payee_name: The payee_name of this HybridTransaction.  # noqa: E501
        :type: str
        """

        self._payee_name = payee_name

    @property
    def category_name(self):
        """Gets the category_name of this HybridTransaction.  # noqa: E501


        :return: The category_name of this HybridTransaction.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this HybridTransaction.


        :param category_name: The category_name of this HybridTransaction.  # noqa: E501
        :type: str
        """

        self._category_name = category_name

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
        if issubclass(HybridTransaction, dict):
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
        if not isinstance(other, HybridTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
