---
title: https://developer.android.com/design/ui/cars/guides/app-types/browse-locations
url: https://developer.android.com/design/ui/cars/guides/app-types/browse-locations
source: md.txt
---

# Browse locations and start Navigation

You can help users quickly find places and start navigation by organizing multiple saved locations under submenus, such as*Recents*.  

In this example, the task flow remains under the maximum of 5 steps --- even with the additional step of selecting a route.

## Sample flow

|         User action          |                                                                                                                                                         Where action is performed                                                                                                                                                         | Step count after action |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| The user selects a submenu.  | Landing template (List template included in the Map + Content template) ![List template included in the Map + Content template containing Recents, Favorites, and Saved sublists](https://developer.android.com/static/images/design/ui/cars/app-cuj/browse_and_start_nav_1.png)                                                          | 1                       |
| The user selects a location. | List template included in the Map + Content template (not a refresh) ![List template included in the Map + Content template with new content](https://developer.android.com/static/images/design/ui/cars/app-cuj/browse_and_start_nav_2.png)**Note:**Because new content is presented, this step is considered a new step, not a refresh. | 2                       |
| The user selects a route.    | List template included in the Map + Content template ![List template included in the Map + Content template](https://developer.android.com/static/images/design/ui/cars/app-cuj/browse_and_start_nav_3.png)                                                                                                                               | 3                       |
| Navigation begins.           | Navigation template ![Example of navigation template](https://developer.android.com/static/images/design/ui/cars/app-cuj/browse_and_start_nav_4.png)                                                                                                                                                                                      | 1 (new task)            |