---
title: Add a stop while driving  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/app-types/add-stop
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Add a stop while driving Stay organized with collections Save and categorize content based on your preferences.




You can let users add a stop while driving without losing the view of their
current route. Transition from the
[Navigation template](/design/ui/cars/guides/templates/navigation-template)
to the
[Map + Content template](/design/ui/cars/guides/templates/map-content-template)
to show a compact list of places while keeping the turn-by-turn
information visible.

The turn-by-turn information on the routing card will be condensed and moved
to the side of the screen.

## Sample flow

The user is using the app. They decide to add a stop to their journey.

| User action | Where action is performed | Step count after action |
| --- | --- | --- |
| The user taps an action to add a stop during an active route. | Navigation template Navigation template during the user's journey | 1 |
| A compact list appears, showing the available options to add a stop, while the turn information shrinks into a floating navigation bar and moves to the side. | List template included in the Map + Content template Map template with list of locations to add a stop | 2 |
| The user taps the chosen stop. | List template included in the Map + Content template Map template with list of locations to add a stop **Note:** Because the content of the map template does not change, this is considered a refresh and does not add to the step count. | 2 |
| The user clicks the **Navigate** button to start navigation. | Pane template included in the Map + Content template Included Pane template with location details and Navigate button | 3 |
| The stop is added to the route and the app informs the user with a [navigation alert](/design/ui/cars/guides/templates/navigation-template#alerts). | Navigation template Navigation template during navigation | 1 |