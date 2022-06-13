# MonthSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **date** |  | 
**note** | **str** |  | [optional] 
**income** | **int** | The total amount of transactions categorized to &#x27;Inflow: Ready to Assign&#x27; in the month | 
**budgeted** | **int** | The total amount budgeted in the month | 
**activity** | **int** | The total amount of transactions in the month, excluding those categorized to &#x27;Inflow: Ready to Assign&#x27; | 
**to_be_budgeted** | **int** | The available amount for &#x27;Ready to Assign&#x27; | 
**age_of_money** | **int** | The Age of Money as of the month | [optional] 
**deleted** | **bool** | Whether or not the month has been deleted.  Deleted months will only be included in delta requests. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

