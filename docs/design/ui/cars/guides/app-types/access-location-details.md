---
title: Access place details and start navigation  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/app-types/access-location-details
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Access place details and start navigation Stay organized with collections Save and categorize content based on your preferences.




In apps that include a map feature, users may need detailed information about a
specific place. Use the Navigation template (only for navigation apps)
or the Map + Content template to help users find the details they need
within a couple of quick taps.

[](/static/images/design/ui/cars/app-cuj/access_location.mp4)

In this example from an electric vehicle charging app, the **Navigate** button
opens a separate navigation app, ending the task flow.

## Sample flow

| User action | Where action is performed | Step count after action |
| --- | --- | --- |
| The user opens your app, then selects a submenu. | List template included in the Map + Content template List template included in the Map + Content template with Work           charger, Nearby stations, and Saved submenus | 1 |
| The user selects a location from the submenu. | List template included in the Map + Content template Map + Content template with embedded List with list of charging           locations **Note:** Because new content is presented to the user, this step is considered a new step, not a refresh. | 2 |
| The user reviews details about the location and decides to navigate there. | Pane template included in the Map + Content template Map + Content template with embedded Pane template with details about           the location and primary and secondary buttons | 3 || A separate navigation app opens and routing begins. | Navigation template in new app New navigation app with routing instructions | 1 |