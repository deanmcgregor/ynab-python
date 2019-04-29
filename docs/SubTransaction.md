# SubTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transaction_id** | **str** |  | 
**amount** | **int** | The subtransaction amount in milliunits format | 
**memo** | **str** |  | 
**payee_id** | **str** |  | 
**category_id** | **str** |  | 
**transfer_account_id** | **str** | If a transfer, the account_id which the subtransaction transfers to | 
**deleted** | **bool** | Whether or not the subtransaction has been deleted.  Deleted subtransactions will only be included in delta requests. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

