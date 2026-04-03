---
title: https://developer.android.com/games/services/management/api/achievements
url: https://developer.android.com/games/services/management/api/achievements
source: md.txt
---

# Achievements

Represents player awards for in-game accomplishments.

For a list of[methods](https://developer.android.com/games/services/management/api/achievements#methods)for this resource, see the end of this page.

## Resource representations

There is no persistent data associated with this resource.

## Methods

[reset](https://developer.android.com/games/services/management/api/achievements/reset)
:   Resets the achievement with the given ID for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application.

[resetAll](https://developer.android.com/games/services/management/api/achievements/resetAll)
:   Resets all achievements for the currently authenticated player for your application. This method is only accessible to whitelisted tester accounts for your application.

[resetForAllPlayers](https://developer.android.com/games/services/management/api/achievements/resetForAllPlayers)
:   Resets the achievement with the given ID for all players. This method is only available to user accounts for your developer console. Only draft achievements can be reset.

[resetAllForAllPlayers](https://developer.android.com/games/services/management/api/achievements/resetAllForAllPlayers)
:   Resets all draft achievements for all players. This method is only available to user accounts for your developer console.

[resetMultipleForAllPlayers](https://developer.android.com/games/services/management/api/achievements/resetMultipleForAllPlayers)
:   Resets achievements with the given IDs for all players. This method is only available to user accounts for your developer console. Only draft achievements may be reset.