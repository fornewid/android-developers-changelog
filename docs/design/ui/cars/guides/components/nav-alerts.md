---
title: https://developer.android.com/design/ui/cars/guides/components/nav-alerts
url: https://developer.android.com/design/ui/cars/guides/components/nav-alerts
source: md.txt
---

# Respond to navigation alerts

You can inform users about incidents like traffic events by using[navigation alerts](https://developer.android.com/design/ui/cars/guides/templates/navigation-template#alerts)in the[Navigation template](https://developer.android.com/design/ui/cars/guides/templates/navigation-template).

Navigation alerts appear in the spot normally used for the estimated time of arrival (ETA), so they don't block the navigation route. Users can then select how to respond to the alert, for example, deciding to reroute to avoid heavy traffic.

## Sample flow

This sample flow shows how the templates might look in Android Auto.

|                                                                                       User action                                                                                       |                                                                             Where action is performed                                                                              | Step count after action |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| While the user is navigating, the app learns about a traffic event ahead on the route.                                                                                                  | Navigation template ![Navigation template during a user's journey](https://developer.android.com/static/images/design/ui/cars/components/respond-to-nav-alert-1.png)               | 1                       |
| Instead of the ETA, a navigation alert now appears to warn the user and offer an option to reroute, while a progress indicator tracks the time until the alert automatically dismisses. | Navigation template (refresh) ![Navigation template with alert](https://developer.android.com/static/images/design/ui/cars/components/respond-to-nav-alert-2.png)                  | 1                       |
| The alert is dismissed after it times out.                                                                                                                                              | Navigation template (second refresh) ![Navigation template with alert dismissed](https://developer.android.com/static/images/design/ui/cars/components/respond-to-nav-alert-1.png) | 1                       |