# SubTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transaction_id** | **str** |  | 
**amount** | **int** | The subtransaction amount in milliunits format | 
**memo** | **str** |  | [optional] 
**payee_id** | **str** |  | [optional] 
**payee_name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**transfer_account_id** | **str** | If a transfer, the account_id which the subtransaction transfers to | [optional] 
**transfer_transaction_id** | **str** | If a transfer, the id of transaction on the other side of the transfer | [optional] 
**deleted** | **bool** | Whether or not the subtransaction has been deleted.  Deleted subtransactions will only be included in delta requests. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

