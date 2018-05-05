# ScheduledTransactionDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**date_first** | **date** | The first date for which the Scheduled Transaction was scheduled. | 
**date_next** | **date** | The next date for which the Scheduled Transaction is scheduled. | 
**frequency** | **str** |  | 
**amount** | **float** | The scheduled transaction amount in milliunits format | 
**memo** | **str** |  | 
**flag_color** | **str** | The scheduled transaction flag | 
**account_id** | **str** |  | 
**payee_id** | **str** |  | 
**category_id** | **str** |  | 
**transfer_account_id** | **str** | If a transfer, the account_id which the scheduled transaction transfers to | 
**account_name** | **str** |  | 
**payee_name** | **str** |  | 
**category_name** | **str** |  | 
**subtransactions** | [**list[ScheduledSubTransaction]**](ScheduledSubTransaction.md) | If a split scheduled transaction, the subtransactions. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


