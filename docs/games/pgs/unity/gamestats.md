---
title: https://developer.android.com/games/pgs/unity/gamestats
url: https://developer.android.com/games/pgs/unity/gamestats
source: md.txt
---

This topic describes how to use Play Games Services Game Stats in Unity
games. It assumes that you've set up your project and the
Google Play Games plugin for Unity, as discussed in the
[Get started guide](https://developer.android.com/games/pgs/unity/unity-start).

## Create Game Stats

When you set up your project and plugin, create the Game Stats in
Google Play Console and then update the plugin with the Android resources
for your Game Stats. For details about creating Game Stats in
Play Console, see the
[Game Stats guide](https://developer.android.com/games/pgs/integrate-gamestats).

## Client side integration

The client side integration for [`PlayerGameEvent`](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-game-event) would involve you
building the event object in Csharp, at the trigger points and sending them
using the upload functions provided by the SDK.

Similarly, for the `progressUpdate` event, record updated progress using the
`currentProgress` property with additional defined properties and send them
using upload functions provided by the SDK.

##### Events

The client side integration for `PlayerGameEvent` are:

##### Build Player Game Event

### Unity


    // Build the PlayerGameEvent
    var playerEvent = new PlayerGameEvent.Builder("matchCompleted")
       .AddProperty("matchId", "Match_A")
       .AddProperty("gameMode", "Battle_B")
       .AddProperty("mapId", "Location_XYZ")
       .AddProperty("isWinner", true)
       .AddProperty("playerElimination", 2)
       .Build();
    var events = new List();
    // ... populate list ...

##### Build `progressUpdate` Player Game Event

### Unity


    // Build the PlayerGameEvent
    var progressEvent = new PlayerGameEvent.Builder("progressUpdate")
       .AddProperty("currentProgress", 52)
       // Add other properties if needed
       .Build();
    var events = new List();
    // ... populate list ...

##### Record Event And Upload

### Unity


    // Buffers the event locally.
    PlayGamesPlatform.Instance.RecordEvent(playerEvent);

    // Buffers the events locally, (List version)
    PlayGamesPlatform.Instance.RecordEvents(events);

    // This submits the events to PGS
    PlayGamesPlatform.Instance.RequestEventsUpload();

> [!NOTE]
> **Note:** Each uploaded event will be validated against the declared schema in the console. If the uploaded event contains properties or corresponding datatypes different from those declared in the console, the event won't be submitted and a relevant response will be sent in the API call response. In case of batch upload, each uploaded event will be validated against the declared schema and events failing the schema won't be submitted and will be shown in the response with the failure reason.