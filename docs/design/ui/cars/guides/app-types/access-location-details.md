---
title: https://developer.android.com/design/ui/cars/guides/app-types/access-location-details
url: https://developer.android.com/design/ui/cars/guides/app-types/access-location-details
source: md.txt
---

# Access place details and start navigation

In apps that include a map feature, users may need detailed information about a specific place. Use the Navigation template (only for navigation apps) or the Map + Content template to help users find the details they need within a couple of quick taps.  

<br />

In this example from an electric vehicle charging app, the**Navigate**button opens a separate navigation app, ending the task flow.

## Sample flow

|                                User action                                 |                                                                                                                                                           Where action is performed                                                                                                                                                            | Step count after action |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| The user opens your app, then selects a submenu.                           | List template included in the Map + Content template ![List template included in the Map + Content template with Work charger, Nearby stations, and Saved submenus](https://developer.android.com/static/images/design/ui/cars/app-cuj/location_details_navigate_1.png)                                                                        | 1                       |
| The user selects a location from the submenu.                              | List template included in the Map + Content template ![Map + Content template with embedded List with list of charging locations](https://developer.android.com/static/images/design/ui/cars/app-cuj/location_details_navigate_2.png)**Note:**Because new content is presented to the user, this step is considered a new step, not a refresh. | 2                       |
| The user reviews details about the location and decides to navigate there. | Pane template included in the Map + Content template ![Map + Content template with embedded Pane template with details about the location and primary and secondary buttons](https://developer.android.com/static/images/design/ui/cars/app-cuj/location_details_navigate_3.png)                                                               | 3                       |
| A separate navigation app opens and routing begins.                        | Navigation template in new app ![New navigation app with routing instructions](https://developer.android.com/static/images/design/ui/cars/app-cuj/location_details_navigate_4.png)                                                                                                                                                             | 1                       |