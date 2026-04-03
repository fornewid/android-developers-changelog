---
title: Search using past data while driving  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/app-types/search-using-past-results
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Search using past data while driving Stay organized with collections Save and categorize content based on your preferences.




Users might be restricted from using the keyboard while driving.
Presenting past search results (places) or keywords (such as *coffee*) using
the Search template can help them find the right destination without typing.
Users can then select a result and begin navigation.

[](/static/images/design/ui/cars/app-cuj/search.mp4)

## Sample flow

This sample flow shows how the templates might look in Android Auto.

| User action | Where action is performed | Step count after action |
| --- | --- | --- |
| The user taps the **Search** button from the action strip. | List template included in the Map + Content template (landing template) List template included in the Map + Content template with Work           charger, Nearby stations, and Saved sublists | 1 |
| The user selects the option to show the map with a list of past results. | Search template (disabled state) Search template with list of past locations and Show Map button | 2 |
| The user selects an item from the list. | List template included in the Map + Content template Selecting a location from previous search results | 3 |
| The user selects an action from the pane that opens. | Pane template included in the Map + Content template Pane template included in the Map + Content template with primary and           secondary action buttons | 4 |
| Navigation begins. | Navigation template Navigation template at the beginning of the user's journey | 1 (new task) |