---
title: Arrive at destination  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/app-types/arrive-at-destination
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Arrive at destination Stay organized with collections Save and categorize content based on your preferences.



You can show a user that they've arrived at their destination using the
[Navigation template](/design/ui/cars/guides/templates/navigation-template).
Simply switch the routing card from
[routing state](/design/ui/cars/guides/templates/navigation-template#routing-card) to
[message state](/design/ui/cars/guides/templates/navigation-template#message-state)
and display an arrival message (this is a refresh, as are all updates to the
navigation template).

Once you've displayed the arrival message, you can refresh the screen to show
the map view again.

## Sample flow

| User action | Where action is performed | Step count after action |
| --- | --- | --- |
| The routing card directs the user toward the destination. | Navigation template in routing state Navigation template during the user's journey | 1 |
| A message confirms the user's arrival at the destination. | Navigation template in message state Navigation template showing a message **Note:** Because the content of the navigation template does not change, this is considered a refresh and does not add to the step count. | 1 |
| When the app decides it's time (after at least 8 seconds), the message disappears and the user sees just the map. | Navigation template with map only Navigation template; message has disappeared **Note:** Because the content of the navigation template does not change, this is considered a refresh and does not add to the step count. | 1 |