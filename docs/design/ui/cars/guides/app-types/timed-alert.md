---
title: https://developer.android.com/design/ui/cars/guides/app-types/timed-alert
url: https://developer.android.com/design/ui/cars/guides/app-types/timed-alert
source: md.txt
---

# See and respond to a timed alert

Use a timed alert to let users know how much time they have to respond before a default action is chosen.

To create a timed alert message, use the Pane view within the[navigation template](https://developer.android.com/design/ui/cars/guides/templates/navigation-template), with[timed buttons](https://developer.android.com/design/ui/cars/guides/components/button)for the default action.

## Sample flow

|                                                    User action                                                     |                                                                          Where action is performed                                                                           | Step count after action |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| The user is driving their vehicle.                                                                                 | Navigation template ![Navigation template during a user's journey](https://developer.android.com/static/images/design/ui/cars/app-cuj/respond_to_timed_alert_1.png)          | 1                       |
| An alert with a timed, default action opens. The user can dismiss the alert or open a map with an alternate route. | Navigation template ![Navigation template with prompt to resume navigation](https://developer.android.com/static/images/design/ui/cars/app-cuj/respond_to_timed_alert_2.png) | 2                       |