# ynab.DeprecatedApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_transactions**](DeprecatedApi.md#bulk_create_transactions) | **POST** /budgets/{budget_id}/transactions/bulk | Bulk create transactions

# **bulk_create_transactions**
> BulkResponse bulk_create_transactions(body, budget_id)

Bulk create transactions

Creates multiple transactions.  Although this endpoint is still supported, it is recommended to use 'POST /budgets/{budget_id}/transactions' to create multiple transactions.

### Example
```python
from __future__ import print_function
import time
import ynab
from ynab.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = ynab.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ynab.DeprecatedApi(ynab.ApiClient(configuration))
body = ynab.BulkTransactions() # BulkTransactions | The list of transactions to create
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can also be used to specify the last used budget)

try:
    # Bulk create transactions
    api_response = api_instance.bulk_create_transactions(body, budget_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeprecatedApi->bulk_create_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkTransactions**](BulkTransactions.md)| The list of transactions to create | 
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

