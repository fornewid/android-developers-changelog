---
title: Events  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/management/api/events
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# Events Stay organized with collections Save and categorize content based on your preferences.




For a list of [methods](#methods) for this resource, see the end of this page.

## Resource representations

There is no persistent data associated with this resource.

## Methods

[reset](/games/services/management/api/events/reset)
:   Resets all player progress on the event with the given ID for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application.

[resetAll](/games/services/management/api/events/resetAll)
:   Resets all player progress on all events for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application.

[resetForAllPlayers](/games/services/management/api/events/resetForAllPlayers)
:   Resets the event with the given ID for all players. This method is only available to user accounts for your developer console. Only draft events can be reset.

[resetAllForAllPlayers](/games/services/management/api/events/resetAllForAllPlayers)
:   Resets all draft events for all players. This method is only available to user accounts for your developer console.

[resetMultipleForAllPlayers](/games/services/management/api/events/resetMultipleForAllPlayers)
:   Resets events with the given IDs for all players. This method is only available to user accounts for your developer console. Only draft events may be reset.