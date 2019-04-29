# ynab.TransactionsApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction**](TransactionsApi.md#create_transaction) | **POST** /budgets/{budget_id}/transactions | Create a single transaction or multiple transactions
[**get_transaction_by_id**](TransactionsApi.md#get_transaction_by_id) | **GET** /budgets/{budget_id}/transactions/{transaction_id} | Single transaction
[**get_transactions**](TransactionsApi.md#get_transactions) | **GET** /budgets/{budget_id}/transactions | List transactions
[**get_transactions_by_account**](TransactionsApi.md#get_transactions_by_account) | **GET** /budgets/{budget_id}/accounts/{account_id}/transactions | List account transactions
[**get_transactions_by_category**](TransactionsApi.md#get_transactions_by_category) | **GET** /budgets/{budget_id}/categories/{category_id}/transactions | List category transactions
[**get_transactions_by_payee**](TransactionsApi.md#get_transactions_by_payee) | **GET** /budgets/{budget_id}/payees/{payee_id}/transactions | List payee transactions
[**update_transaction**](TransactionsApi.md#update_transaction) | **PUT** /budgets/{budget_id}/transactions/{transaction_id} | Updates an existing transaction
[**update_transactions**](TransactionsApi.md#update_transactions) | **PATCH** /budgets/{budget_id}/transactions | Update multiple transactions

# **create_transaction**
> SaveTransactionsResponse create_transaction(body, budget_id)

Create a single transaction or multiple transactions

Creates a single transaction or multiple transactions.  If you provide a body containing a 'transaction' object, a single transaction will be created and if you provide a body containing a 'transactions' array, multiple transactions will be created.

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
api_instance = ynab.TransactionsApi(ynab.ApiClient(configuration))
body = ynab.SaveTransactionsWrapper() # SaveTransactionsWrapper | The transaction or transactions to create.  To create a single transaction you can specify a value for the 'transaction' object and to create multiple transactions you can specify an array of 'transactions'.  It is expected that you will only provide a value for one of these objects.
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can also be used to specify the last used budget)

try:
    # Create a single transaction or multiple transactions
    api_response = api_instance.create_transaction(body, budget_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaveTransactionsWrapper**](SaveTransactionsWrapper.md)| The transaction or transactions to create.  To create a single transaction you can specify a value for the &#x27;transaction&#x27; object and to create multiple transactions you can specify an array of &#x27;transactions&#x27;.  It is expected that you will only provide a value for one of these objects. | 
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 

### Return type

[**SaveTransactionsResponse**](SaveTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_by_id**
> TransactionResponse get_transaction_by_id(budget_id, transaction_id)

Single transaction

Returns a single transaction

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
api_instance = ynab.TransactionsApi(ynab.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can also be used to specify the last used budget)
transaction_id = 'transaction_id_example' # str | The id of the transaction

try:
    # Single transaction
    api_response = api_instance.get_transaction_by_id(budget_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transaction_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **transaction_id** | **str**| The id of the transaction | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> TransactionsResponse get_transactions(budget_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)

List transactions

Returns budget transactions

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
api_instance = ynab.TransactionsApi(ynab.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can also be used to specify the last used budget)
since_date = '2013-10-20' # date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). (optional)
type = 'type_example' # str | If specified, only transactions of the specified type will be included. 'uncategorized' and 'unapproved' are currently supported. (optional)
last_knowledge_of_server = 789 # int | The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. (optional)

try:
    # List transactions
    api_response = api_instance.get_transactions(budget_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **since_date** | **date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional] 
 **type** | **str**| If specified, only transactions of the specified type will be included. &#x27;uncategorized&#x27; and &#x27;unapproved&#x27; are currently supported. | [optional] 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_account**
> TransactionsResponse get_transactions_by_account(budget_id, account_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)

List account transactions

Returns all transactions for a specified account

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
api_instance = ynab.TransactionsApi(ynab.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can also be used to specify the last used budget)
account_id = 'account_id_example' # str | The id of the account
since_date = '2013-10-20' # date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). (optional)
type = 'type_example' # str | If specified, only transactions of the specified type will be included. 'uncategorized' and 'unapproved' are currently supported. (optional)
last_knowledge_of_server = 789 # int | The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. (optional)

try:
    # List account transactions
    api_response = api_instance.get_transactions_by_account(budget_id, account_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions_by_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **account_id** | **str**| The id of the account | 
 **since_date** | **date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional] 
 **type** | **str**| If specified, only transactions of the specified type will be included. &#x27;uncategorized&#x27; and &#x27;unapproved&#x27; are currently supported. | [optional] 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_category**
> HybridTransactionsResponse get_transactions_by_category(budget_id, category_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)

List category transactions

Returns all transactions for a specified category

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
api_instance = ynab.TransactionsApi(ynab.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can also be used to specify the last used budget)
category_id = 'category_id_example' # str | The id of the category
since_date = '2013-10-20' # date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). (optional)
type = 'type_example' # str | If specified, only transactions of the specified type will be included. 'uncategorized' and 'unapproved' are currently supported. (optional)
last_knowledge_of_server = 789 # int | The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. (optional)

try:
    # List category transactions
    api_response = api_instance.get_transactions_by_category(budget_id, category_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions_by_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **category_id** | **str**| The id of the category | 
 **since_date** | **date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional] 
 **type** | **str**| If specified, only transactions of the specified type will be included. &#x27;uncategorized&#x27; and &#x27;unapproved&#x27; are currently supported. | [optional] 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. | [optional] 

### Return type

[**HybridTransactionsResponse**](HybridTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_payee**
> HybridTransactionsResponse get_transactions_by_payee(budget_id, payee_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)

List payee transactions

Returns all transactions for a specified payee

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
api_instance = ynab.TransactionsApi(ynab.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can also be used to specify the last used budget)
payee_id = 'payee_id_example' # str | The id of the payee
since_date = '2013-10-20' # date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). (optional)
type = 'type_example' # str | If specified, only transactions of the specified type will be included. 'uncategorized' and 'unapproved' are currently supported. (optional)
last_knowledge_of_server = 789 # int | The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. (optional)

try:
    # List payee transactions
    api_response = api_instance.get_transactions_by_payee(budget_id, payee_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions_by_payee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **payee_id** | **str**| The id of the payee | 
 **since_date** | **date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional] 
 **type** | **str**| If specified, only transactions of the specified type will be included. &#x27;uncategorized&#x27; and &#x27;unapproved&#x27; are currently supported. | [optional] 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. | [optional] 

### Return type

[**HybridTransactionsResponse**](HybridTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction**
> TransactionResponse update_transaction(body, budget_id, transaction_id)

Updates an existing transaction

Updates a transaction

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
api_instance = ynab.TransactionsApi(ynab.ApiClient(configuration))
body = ynab.SaveTransactionWrapper() # SaveTransactionWrapper | The transaction to update
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can also be used to specify the last used budget)
transaction_id = 'transaction_id_example' # str | The id of the transaction

try:
    # Updates an existing transaction
    api_response = api_instance.update_transaction(body, budget_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaveTransactionWrapper**](SaveTransactionWrapper.md)| The transaction to update | 
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **transaction_id** | **str**| The id of the transaction | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transactions**
> SaveTransactionsResponse update_transactions(body, budget_id)

Update multiple transactions

Updates multiple transactions, by 'id' or 'import_id'.

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
api_instance = ynab.TransactionsApi(ynab.ApiClient(configuration))
body = ynab.SaveTransactionsWrapper() # SaveTransactionsWrapper | The transactions to update.  Optionally, transaction 'id' value(s) can be specified as null and an 'import_id' value can be provided which will allow transaction(s) to updated by their import_id.
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can also be used to specify the last used budget)

try:
    # Update multiple transactions
    api_response = api_instance.update_transactions(body, budget_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->update_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaveTransactionsWrapper**](SaveTransactionsWrapper.md)| The transactions to update.  Optionally, transaction &#x27;id&#x27; value(s) can be specified as null and an &#x27;import_id&#x27; value can be provided which will allow transaction(s) to updated by their import_id. | 
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 

### Return type

[**SaveTransactionsResponse**](SaveTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

