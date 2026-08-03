---
title: https://developer.android.com/games/pgs/cpp/gamestats
url: https://developer.android.com/games/pgs/cpp/gamestats
source: md.txt
---

This document describes how to use Google Play Games Services Game Stats in C++ games. This
document assumes you have set up your project as described in [Set Up
Google Play Games Services](https://developer.android.com/games/pgs/console/setup). You can find the Game Stats API in the
[`PgsGameStatsClient`](https://developer.android.com/games/services/cpp/v2/api/group/game-stats).

## Before you begin

If you haven't already done so, you might find it helpful to review the
[Game Stats game concepts](https://developer.android.com/games/pgs/gamestats).

Before you start to code using the Game Stats API:

- Follow the instructions for installing and setting up your app to use
  Play Games Services in the
  [Set Up Google Play Games Services](https://developer.android.com/games/pgs/console/setup) guide.

- Define the Game Stats that you want your game, by
  following the instructions in the [Google Play Console guide](https://developer.android.com/games/pgs/integrate-gamestats).

## Get Game Stats client

To start using the achievements API, your game must first obtain an
[`PgsGameStatsClient`](https://developer.android.com/games/services/cpp/v2/api/group/play-games#pgsgamestatsclient)
object. You can do this by calling the
[`PgsPlayerGameEvent_create`](https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#pgsplayergameevent_create)
method and passing in the activity.

## Client side integration

The client side integration for [`PlayerGameEvent`](https://developer.android.com/games/services/cpp/v2/api/group/player-game-event) would involve you building the
event object in C++ SDK, at the trigger points and
sending them using the upload functions provided by the SDK.

Similarly, for the `progressUpdate` event, record updated progress using the
`currentProgress` property with additional defined properties and send them
using upload functions provided by the SDK.

##### Events

The client side integration for `PlayerGameEvent` are:

##### Build Player Game Event

### C++


    // Build the PlayerGameEvent
    PgsPlayerGameEvent* player_event = PgsPlayerGameEvent_create("matchCompleted");
    if (player_event != nullptr) {
       PgsPlayerGameEvent_putString(player_event, "matchId", "Match_A");
       PgsPlayerGameEvent_putString(player_event, "gameMode", "Battle_B");
       PgsPlayerGameEvent_putString(player_event, "mapId", "Location_XYZ");
       PgsPlayerGameEvent_putBoolean(player_event, "isWinner", true);
       PgsPlayerGameEvent_putLong(player_event, "playerElimination", 2);
    }

##### Build `progressUpdate` Player Game Event

### C++


    PgsPlayerGameEvent* progress_event = PgsPlayerGameEvent_create("progressUpdate");
    if (progress_event != nullptr) {
       PgsPlayerGameEvent_putLong(progress_event, "currentProgress", 52);
    }

##### Record Event And Upload

### C++


    // Record the event
    PgsGameStatsClient_recordEvent(client, player_event);

    // This submits the events to PGS
    PgsGameStatsClient_requestEventsUpload(client);

    // Clean up handle to avoid leaks
    PgsPlayerGameEvent_destroy(player_event);

    // Clean up client handle when PGS operations are finished
    PgsGameStatsClient_destroy(client);

> [!NOTE]
> **Note:** Each uploaded event will be validated against the declared schema in the console. If the uploaded event contains properties or corresponding datatypes different from those declared in the console, the event won't be submitted and a relevant response will be sent in the API call response. In case of batch upload, each uploaded event will be validated against the declared schema and events failing the schema won't be submitted and will be shown in the response with the failure reason.