---
title: https://developer.android.com/games/pgs/unity/events
url: https://developer.android.com/games/pgs/unity/events
source: md.txt
---

This topics describes how to use Play Games Services events in Unity
games.

## Before you get started

Set up your Unity project and the Google Play Games plugin for Unity. For
details, see the [Get started guide](https://developer.android.com/games/pgs/unity/unity-start).

## Create events

You create events in Google Play Console. For details, see the
[events guide](https://developer.android.com/games/pgs/events#create-event) for Play Games Services. After
you create your events, add their Android resources to the plugin as described
in the [get started guide](https://developer.android.com/games/pgs/unity/unity-start).

## Record events

To increment an event, call the following method:

        using GooglePlayGames;
        ...
        // Increments the event with Id "YOUR_EVENT_ID" by 1
        PlayGamesPlatform.Instance.Events.IncrementEvent("YOUR_EVENT_ID", 1);

You only need to make this call once. It handles batching and execution in the
background.