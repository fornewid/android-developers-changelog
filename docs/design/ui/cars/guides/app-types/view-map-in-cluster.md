---
title: View a map in the cluster  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/app-types/view-map-in-cluster
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# View a map in the cluster Stay organized with collections Save and categorize content based on your preferences.



Another helpful way to minimize distraction for drivers is to display a map in
the instrument cluster, behind the steering wheel. The
[cluster display option](/design/ui/cars/guides/templates/navigation-template#cluster) for the [navigation template](/design/ui/cars/guides/templates/navigation-template)
lets drivers navigate while looking straight ahead.

This map is noninteractive and can feature its own map view, independent of
any map view that might appear in the center screen. It displays in the cluster
only while the user is navigating with the navigation template.

[](/static/images/design/ui/cars/app-cuj/view_cluster.mp4)

## Sample flow

| User action | Where action is performed | Step count after action |
| --- | --- | --- |
| The user chooses a destination from the list on the center screen. | Place List template   Mock-up of the cluster view and head unit in a car, user taps a destination | 1 |
| When the navigation starts, a second map (created by the app developer) appears in the cluster. | Navigation template   Updated mock-up; the Navigation template guides the user | 2 |