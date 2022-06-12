# Category

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**category_group_id** | **str** |  | 
**name** | **str** |  | 
**hidden** | **bool** | Whether or not the category is hidden | 
**original_category_group_id** | **str** | If category is hidden this is the id of the category group it originally belonged to before it was hidden. | [optional] 
**note** | **str** |  | [optional] 
**budgeted** | **int** | Budgeted amount in milliunits format | 
**activity** | **int** | Activity amount in milliunits format | 
**balance** | **int** | Balance in milliunits format | 
**goal_type** | **str** | The type of goal, if the category has a goal (TB&#x3D;&#x27;Target Category Balance&#x27;, TBD&#x3D;&#x27;Target Category Balance by Date&#x27;, MF&#x3D;&#x27;Monthly Funding&#x27;, NEED&#x3D;&#x27;Plan Your Spending&#x27;) | [optional] 
**goal_creation_month** | **date** | The month a goal was created | [optional] 
**goal_target** | **int** | The goal target amount in milliunits | [optional] 
**goal_target_month** | **date** | The original target month for the goal to be completed.  Only some goal types specify this date. | [optional] 
**goal_percentage_complete** | **int** | The percentage completion of the goal | [optional] 
**goal_months_to_budget** | **int** | The number of months, including the current month, left in the current goal period. | [optional] 
**goal_under_funded** | **int** | The amount of funding still needed in the current month to stay on track towards completing the goal within the current goal period.  This amount will generally correspond to the &#x27;Underfunded&#x27; amount in the web and mobile clients except when viewing a category with a Needed for Spending Goal in a future month.  The web and mobile clients will ignore any funding from a prior goal period when viewing category with a Needed for Spending Goal in a future month. | [optional] 
**goal_overall_funded** | **int** | The total amount funded towards the goal within the current goal period. | [optional] 
**goal_overall_left** | **int** | The amount of funding still needed to complete the goal within the current goal period. | [optional] 
**deleted** | **bool** | Whether or not the category has been deleted.  Deleted categories will only be included in delta requests. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

