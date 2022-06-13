# SaveTransactionsResponseData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **list[str]** | The transaction ids that were saved | 
**transaction** | [**TransactionDetail**](TransactionDetail.md) |  | [optional] 
**transactions** | [**list[TransactionDetail]**](TransactionDetail.md) | If multiple transactions were specified, the transactions that were saved | [optional] 
**duplicate_import_ids** | **list[str]** | If multiple transactions were specified, a list of import_ids that were not created because of an existing &#x60;import_id&#x60; found on the same account | [optional] 
**server_knowledge** | **int** | The knowledge of the server | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

