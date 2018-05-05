# HybridTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**date** | **date** |  | 
**amount** | **float** | The transaction amount in milliunits format | 
**memo** | **str** |  | 
**cleared** | **str** | The cleared status of the transaction | 
**approved** | **bool** | Whether or not the transaction is approved | 
**flag_color** | **str** | The transaction flag | 
**account_id** | **str** |  | 
**payee_id** | **str** |  | 
**category_id** | **str** |  | 
**transfer_account_id** | **str** |  | 
**import_id** | **str** | If the Transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: &#39;YNAB:[milliunit_amount]:[iso_date]:[occurrence]&#39;.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of &#39;YNAB:-294230:2015-12-30:1&#39;.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be &#39;YNAB:-294230:2015-12-30:2&#39;. | 
**type** | **str** | Whether the hybrid transaction represents a regular transaction or a subtransaction | 
**parent_transaction_id** | **str** | For subtransaction types, this is the id of the pararent transaction.  For transaction types, this id will be always be null. | 
**account_name** | **str** |  | 
**payee_name** | **str** |  | 
**category_name** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


