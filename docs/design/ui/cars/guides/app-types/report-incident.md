---
title: Report an incident  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/app-types/report-incident
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Report an incident Stay organized with collections Save and categorize content based on your preferences.



Make it easy for drivers to report traffic incidents quickly.
The Grid template included in the Map + Content template
will help you reduce the number of steps
required to report incidents so drivers can focus on the road.

## Sample

This sample flow shows how the templates might look in Android Auto.

| User action | Where action is performed | Step count after action |
| --- | --- | --- |
| While driving, the user notices an incident that they decide to report, so they tap the Report FAB. | Navigation template Navigation template during navigation | 1 |
| A grid of possible actions opens, allowing the user to quickly tap the **Incident** icon. | Grid template included in the Map + Content template Grid template included in the Map + Content template with potential           actions the user can take | 2 |
| The grid is dismissed and a toast appears on the screen notifying the user that the incident was reported. | Navigation template Navigation template during navigation with toast thanking the user           for reporting an incident | 1 (new task) |