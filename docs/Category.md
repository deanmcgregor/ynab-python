# Category

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**category_group_id** | **str** |  | 
**name** | **str** |  | 
**hidden** | **bool** | Whether or not the category is hidden | 
**original_category_group_id** | **str** | If category is hidden this is the id of the category group it originally belonged to before it was hidden. | [optional] 
**note** | **str** |  | 
**budgeted** | **int** | Budgeted amount in milliunits format | 
**activity** | **int** | Activity amount in milliunits format | 
**balance** | **int** | Balance in milliunits format | 
**goal_type** | **str** | The type of goal, if the cagegory has a goal (TB&#x3D;Target Category Balance, TBD&#x3D;Target Category Balance by Date, MF&#x3D;Monthly Funding) | 
**goal_creation_month** | **date** | The month a goal was created | 
**goal_target** | **int** | The goal target amount in milliunits | 
**goal_target_month** | **date** | If the goal type is &#x27;TBD&#x27; (Target Category Balance by Date), this is the target month for the goal to be completed | 
**goal_percentage_complete** | **int** | The percentage completion of the goal | 
**deleted** | **bool** | Whether or not the category has been deleted.  Deleted categories will only be included in delta requests. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

