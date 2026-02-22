---
title: https://developer.android.com/design/ui/cars/guides/app-types/report-incident
url: https://developer.android.com/design/ui/cars/guides/app-types/report-incident
source: md.txt
---

# Report an incident

Make it easy for drivers to report traffic incidents quickly. The Grid template included in the Map + Content template will help you reduce the number of steps required to report incidents so drivers can focus on the road.

## Sample

This sample flow shows how the templates might look in Android Auto.

|                                                User action                                                 |                                                                                                            Where action is performed                                                                                                            | Step count after action |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| While driving, the user notices an incident that they decide to report, so they tap the Report FAB.        | Navigation template ![Navigation template during navigation](https://developer.android.com/static/images/design/ui/cars/app-cuj/report_incident_1.png)                                                                                          | 1                       |
| A grid of possible actions opens, allowing the user to quickly tap the**Incident**icon.                    | Grid template included in the Map + Content template ![Grid template included in the Map + Content template with potential actions the user can take](https://developer.android.com/static/images/design/ui/cars/app-cuj/report_incident_2.png) | 2                       |
| The grid is dismissed and a toast appears on the screen notifying the user that the incident was reported. | Navigation template ![Navigation template during navigation with toast thanking the user for reporting an incident](https://developer.android.com/static/images/design/ui/cars/app-cuj/report_incident_3.png)                                   | 1 (new task)            |