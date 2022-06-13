# HybridTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Whether the hybrid transaction represents a regular transaction or a subtransaction | 
**parent_transaction_id** | **str** | For subtransaction types, this is the id of the parent transaction.  For transaction types, this id will be always be null. | [optional] 
**account_name** | **str** |  | 
**payee_name** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

