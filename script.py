import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv') # Given
# Task 1: To examine the first few rows.
#print(ad_clicks.head()) 

# Task 2: To find the amount of views that came from each utm_source. 
views = ad_clicks.groupby('utm_source').count().reset_index()
#print(views)

# Task 3: Create a new column called "is_click", which is True if 'ad_click_timestamp' is not null and 'False' otherwise. 
# To have all the 'False' rows filtered out.
ad_clicks["is_click"] = ad_clicks.ad_click_timestamp.apply(lambda row: True if row is not None else False)
# To have all rows displayed, both 'True' and 'False', from the 'is_click' column.
ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
#print(ad_clicks) 

# Task 4: Want to find the percent of ppl who clicked on ads from each 'utm_score'.
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().reset_index()
#print(clicks_by_source)

# Task 5: Pivot the data from Task 4.
clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id')
#print(clicks_pivot)

# Task 6: Create a new column and set the value equal to the percent of users who clicked on the ad from each utm_source.
clicks_pivot["percent_clicked"] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
#print(clicks_pivot)

# Task 7: Display the amount of times each ad was displayed to people.
adCount = ad_clicks.groupby("experimental_group").count()
#print(adCount)

# Task 8: Check to see if greater percentage of users clicked on Ad A or Ad B.
checks = ad_clicks.groupby(['is_click', 'experimental_group'])['user_id'].count().reset_index()
checks_pivot = checks.pivot(columns='experimental_group', index='is_click', values='user_id')
#print(checks_pivot) 
# The greater percentage of users clicked on Ad A.

# Task 9: Create dataframes that contain the results for the A & B groups.
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
#print(a_clicks)
#print(b_clicks)

# Task 10: Calculate the users who clucked on the ad by 'day'
a_clicks_grouping = a_clicks.groupby(['is_click', 'day'])['user_id'].count().reset_index()
#print(a_clicks_grouping) # Ad A
b_clicks_grouping = b_clicks.groupby(['is_click', 'day'])['user_id'].count().reset_index()
#print(b_clicks_grouping) # Ad B

# I can use the 'user_id' value(s) to get the percent of users who clicked on the ad by 'day'
# e.g. a_clicks_prct = a_clicks_grouping['is_click']
#print(a_clicks_grouping['is_click'])
a_pivot = a_clicks_grouping.pivot(columns='is_click', index='day')
b_pivot = b_clicks_grouping.pivot(columns='is_click', index='day')
print(a_pivot)
a_pivot["Percent", 'a'] = a_pivot[('user_id'), True] / (a_pivot[('user_id'), False] + a_pivot[('user_id'), True])
#print(a_pivot)
b_pivot["Percent", 'b'] = b_pivot[('user_id'), True] / (b_pivot[('user_id'), False] + b_pivot[('user_id'), True])
print(b_pivot)
# The addition of both columns to divide for the percentage of Task 10
#print(a_pivot[('user_id'), False] + a_pivot[('user_id'), True])