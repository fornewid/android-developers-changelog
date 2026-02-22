---
title: https://developer.android.com/games/services/management/api/events
url: https://developer.android.com/games/services/management/api/events
source: md.txt
---

# Events

<br />

For a list of[methods](https://developer.android.com/games/services/management/api/events#methods)for this resource, see the end of this page.

## Resource representations

There is no persistent data associated with this resource.

## Methods

[reset](https://developer.android.com/games/services/management/api/events/reset)
:   Resets all player progress on the event with the given ID for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application.

[resetAll](https://developer.android.com/games/services/management/api/events/resetAll)
:   Resets all player progress on all events for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application.

[resetForAllPlayers](https://developer.android.com/games/services/management/api/events/resetForAllPlayers)
:   Resets the event with the given ID for all players. This method is only available to user accounts for your developer console. Only draft events can be reset.

[resetAllForAllPlayers](https://developer.android.com/games/services/management/api/events/resetAllForAllPlayers)
:   Resets all draft events for all players. This method is only available to user accounts for your developer console.

[resetMultipleForAllPlayers](https://developer.android.com/games/services/management/api/events/resetMultipleForAllPlayers)
:   Resets events with the given IDs for all players. This method is only available to user accounts for your developer console. Only draft events may be reset.