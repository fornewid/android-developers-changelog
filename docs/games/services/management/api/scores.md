---
title: https://developer.android.com/games/services/management/api/scores
url: https://developer.android.com/games/services/management/api/scores
source: md.txt
---

# Scores

A player leaderboard score. Represents the score (and optionally, the ranks) of a given player in a leaderboard.

For a list of[methods](https://developer.android.com/games/services/management/api/scores#methods)for this resource, see the end of this page.

## Resource representations

There is no persistent data associated with this resource.

## Methods

[reset](https://developer.android.com/games/services/management/api/scores/reset)
:   Resets scores for the leaderboard with the given ID for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application.

[resetForAllPlayers](https://developer.android.com/games/services/management/api/scores/resetForAllPlayers)
:   Resets scores for the leaderboard with the given ID for all players. This method is only available to user accounts for your developer console. Only draft leaderboards can be reset.

[resetAll](https://developer.android.com/games/services/management/api/scores/resetAll)
:   Resets all scores for all leaderboards for the currently authenticated players. This method is only accessible to whitelisted tester accounts for your application.

[resetAllForAllPlayers](https://developer.android.com/games/services/management/api/scores/resetAllForAllPlayers)
:   Resets scores for all draft leaderboards for all players. This method is only available to user accounts for your developer console.

[resetMultipleForAllPlayers](https://developer.android.com/games/services/management/api/scores/resetMultipleForAllPlayers)
:   Resets scores for the leaderboards with the given IDs for all players. This method is only available to user accounts for your developer console. Only draft leaderboards may be reset.