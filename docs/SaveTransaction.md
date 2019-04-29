# SaveTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**_date** | **date** |  | 
**amount** | **int** | The transaction amount in milliunits format | 
**payee_id** | **str** | The payee for the transaction | [optional] 
**payee_name** | **str** | The payee name.  If a payee_name value is provided and payee_id has a null value, the payee_name value will be used to resolve the payee by either (1) a matching payee rename rule (only if import_id is also specified) or (2) a payee with the same name or (3) creation of a new payee. | [optional] 
**category_id** | **str** | The category for the transaction.  Split and Credit Card Payment categories are not permitted and will be ignored if supplied.  If an existing transaction has a Split category it cannot be changed. | [optional] 
**memo** | **str** |  | [optional] 
**cleared** | **str** | The cleared status of the transaction | [optional] 
**approved** | **bool** | Whether or not the transaction is approved.  If not supplied, transaction will be unapproved by default. | [optional] 
**flag_color** | **str** | The transaction flag | [optional] 
**import_id** | **str** | If specified, the new transaction will be assigned this import_id and considered \&quot;imported\&quot;. *At the time of import* we will attempt to match \&quot;imported\&quot; transactions with non-imported (i.e. \&quot;user-entered\&quot;) transactions.&lt;br&gt;&lt;br&gt;Transactions imported through File Based Import or Direct Import (not through the API) are assigned an import_id in the format: &#x27;YNAB:[milliunit_amount]:[iso_date]:[occurrence]&#x27;. For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of &#x27;YNAB:-294230:2015-12-30:1&#x27;.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be &#x27;YNAB:-294230:2015-12-30:2&#x27;.  Using a consistent format will prevent duplicates through Direct Import and File Based Import.&lt;br&gt;&lt;br&gt;If import_id is omitted or specified as null, the transaction will be treated as a \&quot;user-entered\&quot; transaction. As such, it will be eligible to be matched against transactions later being imported (via DI, FBI, or API). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

