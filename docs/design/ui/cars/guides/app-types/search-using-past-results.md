---
title: https://developer.android.com/design/ui/cars/guides/app-types/search-using-past-results
url: https://developer.android.com/design/ui/cars/guides/app-types/search-using-past-results
source: md.txt
---

# Search using past data while driving

Users might be restricted from using the keyboard while driving. Presenting past search results (places) or keywords (such as*coffee*) using the Search template can help them find the right destination without typing. Users can then select a result and begin navigation.  

<br />

## Sample flow

This sample flow shows how the templates might look in Android Auto.

|                               User action                                |                                                                                                                              Where action is performed                                                                                                                               | Step count after action |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| The user taps the**Search**button from the action strip.                 | List template included in the Map + Content template (landing template) ![List template included in the Map + Content template with Work charger, Nearby stations, and Saved sublists](https://developer.android.com/static/images/design/ui/cars/app-cuj/search_past_results_1.png) | 1                       |
| The user selects the option to show the map with a list of past results. | Search template (disabled state) ![Search template with list of past locations and Show Map button](https://developer.android.com/static/images/design/ui/cars/app-cuj/search_past_results_2.png)                                                                                    | 2                       |
| The user selects an item from the list.                                  | List template included in the Map + Content template ![Selecting a location from previous search results](https://developer.android.com/static/images/design/ui/cars/app-cuj/search_past_results_3.png)                                                                              | 3                       |
| The user selects an action from the pane that opens.                     | Pane template included in the Map + Content template ![Pane template included in the Map + Content template with primary and secondary action buttons](https://developer.android.com/static/images/design/ui/cars/app-cuj/search_past_results_4.png)                                 | 4                       |
| Navigation begins.                                                       | Navigation template![Navigation template at the beginning of the user's journey](https://developer.android.com/static/images/design/ui/cars/app-cuj/search_past_results_5.png)                                                                                                       | 1 (new task)            |