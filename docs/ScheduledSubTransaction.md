# ScheduledSubTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**scheduled_transaction_id** | **str** |  | 
**amount** | **int** | The scheduled subtransaction amount in milliunits format | 
**memo** | **str** |  | [optional] 
**payee_id** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**transfer_account_id** | **str** | If a transfer, the account_id which the scheduled subtransaction transfers to | [optional] 
**deleted** | **bool** | Whether or not the scheduled subtransaction has been deleted.  Deleted scheduled subtransactions will only be included in delta requests. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

