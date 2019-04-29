# ynab.BudgetsApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_budget_by_id**](BudgetsApi.md#get_budget_by_id) | **GET** /budgets/{budget_id} | Single budget
[**get_budget_settings_by_id**](BudgetsApi.md#get_budget_settings_by_id) | **GET** /budgets/{budget_id}/settings | Budget Settings
[**get_budgets**](BudgetsApi.md#get_budgets) | **GET** /budgets | List budgets

# **get_budget_by_id**
> BudgetDetailResponse get_budget_by_id(budget_id, last_knowledge_of_server=last_knowledge_of_server)

Single budget

Returns a single budget with all related entities.  This resource is effectively a full budget export.

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
api_instance = ynab.BudgetsApi(ynab.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can also be used to specify the last used budget)
last_knowledge_of_server = 789 # int | The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. (optional)

try:
    # Single budget
    api_response = api_instance.get_budget_by_id(budget_id, last_knowledge_of_server=last_knowledge_of_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->get_budget_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. | [optional] 

### Return type

[**BudgetDetailResponse**](BudgetDetailResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_settings_by_id**
> BudgetSettingsResponse get_budget_settings_by_id(budget_id)

Budget Settings

Returns settings for a budget

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
api_instance = ynab.BudgetsApi(ynab.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can also be used to specify the last used budget)

try:
    # Budget Settings
    api_response = api_instance.get_budget_settings_by_id(budget_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->get_budget_settings_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 

### Return type

[**BudgetSettingsResponse**](BudgetSettingsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budgets**
> BudgetSummaryResponse get_budgets()

List budgets

Returns budgets list with summary information

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
api_instance = ynab.BudgetsApi(ynab.ApiClient(configuration))

try:
    # List budgets
    api_response = api_instance.get_budgets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->get_budgets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BudgetSummaryResponse**](BudgetSummaryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

