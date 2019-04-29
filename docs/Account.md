# Account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** | The type of account. Note: payPal, merchantAccount, investmentAccount, and mortgage types have been deprecated and will be removed in the future. | 
**on_budget** | **bool** | Whether this account is on budget or not | 
**closed** | **bool** | Whether this account is closed or not | 
**note** | **str** |  | 
**balance** | **int** | The current balance of the account in milliunits format | 
**cleared_balance** | **int** | The current cleared balance of the account in milliunits format | 
**uncleared_balance** | **int** | The current uncleared balance of the account in milliunits format | 
**transfer_payee_id** | **str** | The payee id which should be used when transferring to this account | 
**deleted** | **bool** | Whether or not the account has been deleted.  Deleted accounts will only be included in delta requests. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

