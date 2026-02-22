---
title: https://developer.android.com/design/ui/cars/guides/app-types/navigation-alerts
url: https://developer.android.com/design/ui/cars/guides/app-types/navigation-alerts
source: md.txt
---

# See and respond to navigation alerts

You can inform users about incidents like traffic events by using[navigation alerts](https://developer.android.com/design/ui/cars/guides/templates/navigation-template#alerts)in the[Navigation template](https://developer.android.com/design/ui/cars/guides/templates/navigation-template).

Navigation alerts appear in the spot normally used for the estimated time of arrival (ETA), so they don't block the navigation route. Users can then select how to respond to the alert, for example, deciding to reroute to avoid heavy traffic.

## Sample flow

This sample flow shows how the templates might look in Android Auto.

|                                                                                    User action                                                                                    |                                                                             Where action is performed                                                                              | Step count after action |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| While the user is navigating, the app learns about a traffic event ahead on the route.                                                                                            | Navigation template ![Navigation template during a user's journey](https://developer.android.com/static/images/design/ui/cars/app-cuj/respond_to_nav_alert_1.png)                  | 1                       |
| A navigation alert appears instead of the ETA to warn the user and offer an option to reroute, while a progress indicator tracks the time until automatic dismissal of the alert. | Navigation template (refresh) ![Navigation template with alert](https://developer.android.com/static/images/design/ui/cars/app-cuj/respond_to_nav_alert_2.png)                     | 1                       |
| The alert is dismissed after it times out.                                                                                                                                        | Navigation template (second refresh) ![Navigation template during a user's journey](https://developer.android.com/static/images/design/ui/cars/app-cuj/respond_to_nav_alert_1.png) | 1                       |