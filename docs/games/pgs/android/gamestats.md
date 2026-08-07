---
title: https://developer.android.com/games/pgs/android/gamestats
url: https://developer.android.com/games/pgs/android/gamestats
source: md.txt
---

This guide shows you how to use the Game Stats APIs in an Android application to unlock and display Game Stats in your game. The APIs can be found in the [`com.google.android.gms.games`](https://developers.google.com/android/reference/com/google/android/gms/games/package-summary) and [`com.google.android.gms.games.playergameevent`](https://developers.google.com/android/reference/com/google/android/gms/games/playergameevent/package-summary) packages.

## Before you begin

If you haven't already done so, you might find it helpful to review the [Game Stats game concepts](https://developer.android.com/games/pgs/gamestats).

Before you start to code using the Game Stats API:

- Follow the instructions for installing and setting up your app to use Google Play Games Services in the [Set Up Google Play services SDK](https://developers.google.com/android/guides/setup) guide.

- Define the Game Stats that you want your game to unlock or display, by following the instructions in the [Google Play Console guide](https://developer.android.com/games/pgs/integrate-gamestats).

## Get a Game Stats client

To start using the Game Stats API, your game must first obtain an [`GameStatsClient`](https://developers.google.com/android/reference/com/google/android/gms/games/GameStatsClient) object. You can do this by calling the [`Games.getGameStatsClient()`](https://developers.google.com/android/reference/com/google/android/gms/games/GameStatsClient) method and passing in the activity.

## Client side integration

The client side integration for [`PlayerGameEvent`](https://developer.android.com/android/reference/com/google/android/gms/games/playergameevent/PlayerGameEvent) would involve you building the event object in Java SDK, at the trigger points and sending them using the upload functions provided by the SDK.

Similarly, for the `progressUpdate` event, record updated progress using the `currentProgress` property with additional defined properties and send them using upload functions provided by the SDK.

### Events

The client side integration for `PlayerGameEvent` are:

#### Build Player Game Event

### Java


    // Build the PlayerGameEvent
    PlayerGameEvent event = new PlayerGameEvent.Builder("matchCompleted")
      .addProperty("matchId", "Match_A")
      .addProperty("gameMode", "Battle_B")
      .addProperty("mapId", "Location_XYZ")
      .addProperty("isWinner", true)
      .addProperty("playerElimination", 2)
      .build();

    List
           
             
            events
             
            =
             
            new
             
            ArrayList
            <>
            ();

            // ... populate list ...

           
#### Build `progressUpdate` Player Game Event

### Java


    // Build the PlayerGameEvent
    PlayerGameEvent event = new PlayerGameEvent.Builder("progressUpdate")
      .addProperty("currentProgress", 52)
      // Add other properties if needed
      .build();

    List
           
             
            events
             
            =
             
            new
             
            ArrayList
            <>
            ();

            // ... populate list ...

           
#### Record Event And Upload

### Java


    // Buffers the event locally.
    client.recordEvent(event);

    // Buffers the events locally, (List version)
    client.recordEvents(events);

    // This submits the events to PGS
    client.requestEventsUpload();

> [!NOTE]
> **Note:** Each uploaded event will be validated against the declared schema in the console. If the uploaded event contains properties or corresponding datatypes different from those declared in the console, the event won't be submitted and a relevant response will be sent in the API call response. In case of batch upload, each uploaded event will be validated against the declared schema and events failing the schema won't be submitted and will be shown in the response with the failure reason.