# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import ynab
from ynab.api.payee_locations_api import PayeeLocationsApi  # noqa: E501
from ynab.rest import ApiException


class TestPayeeLocationsApi(unittest.TestCase):
    """PayeeLocationsApi unit test stubs"""

    def setUp(self):
        self.api = PayeeLocationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_payee_location_by_id(self):
        """Test case for get_payee_location_by_id

        Single payee location  # noqa: E501
        """
        pass

    def test_get_payee_locations(self):
        """Test case for get_payee_locations

        List payee locations  # noqa: E501
        """
        pass

    def test_get_payee_locations_by_payee(self):
        """Test case for get_payee_locations_by_payee

        List locations for a payee  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
