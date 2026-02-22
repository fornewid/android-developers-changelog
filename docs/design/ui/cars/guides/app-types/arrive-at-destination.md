---
title: https://developer.android.com/design/ui/cars/guides/app-types/arrive-at-destination
url: https://developer.android.com/design/ui/cars/guides/app-types/arrive-at-destination
source: md.txt
---

# Arrive at destination

You can show a user that they've arrived at their destination using the[Navigation template](https://developer.android.com/design/ui/cars/guides/templates/navigation-template). Simply switch the routing card from[routing state](https://developer.android.com/design/ui/cars/guides/templates/navigation-template#routing-card)to[message state](https://developer.android.com/design/ui/cars/guides/templates/navigation-template#message-state)and display an arrival message (this is a refresh, as are all updates to the navigation template).

Once you've displayed the arrival message, you can refresh the screen to show the map view again.

## Sample flow

|                                                    User action                                                    |                                                                                                                                                 Where action is performed                                                                                                                                                  | Step count after action |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| The routing card directs the user toward the destination.                                                         | Navigation template in routing state ![Navigation template during the user's journey](https://developer.android.com/static/images/design/ui/cars/app-cuj/arrive-at-destination-1.png)                                                                                                                                      | 1                       |
| A message confirms the user's arrival at the destination.                                                         | Navigation template in message state ![Navigation template showing a message](https://developer.android.com/static/images/design/ui/cars/app-cuj/arrive-at-destination-2.png)**Note:**Because the content of the navigation template does not change, this is considered a refresh and does not add to the step count.     | 1                       |
| When the app decides it's time (after at least 8 seconds), the message disappears and the user sees just the map. | Navigation template with map only ![Navigation template; message has disappeared](https://developer.android.com/static/images/design/ui/cars/app-cuj/arrive-at-destination-3.png)**Note:**Because the content of the navigation template does not change, this is considered a refresh and does not add to the step count. | 1                       |