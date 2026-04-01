---
title: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-events-client
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-events-client
source: md.txt
---

# GooglePlayGames.BasicApi.Events.IEventsClient Interface Reference

# GooglePlayGames.BasicApi.Events.IEventsClient

An interface for interacting with events.

## Summary

See online[documentation for Events](https://developers.google.com/games/services/common/concepts/events)for more information.

All callbacks in this interface must be invoked on the game thread.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                            ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                             ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [FetchAllEvents](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-events-client#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_events_client_1a3a23d38f619261e9284f76fa0ebaa7dc)`(`[DataSource](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a7b061047c3edf97247d4d1ccd52e2aec)` source, Action< `[ResponseStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1afc173c0f78ea77552386c8f699526dea)`, List< `[IEvent](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-event#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_event)` >> callback)`      | `void` Fetches all events defined for this game. |
| [FetchEvent](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-events-client#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_events_client_1a755e6c50c65ec923ff2b7e0189eb62d8)`(`[DataSource](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a7b061047c3edf97247d4d1ccd52e2aec)` source, string eventId, Action< `[ResponseStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1afc173c0f78ea77552386c8f699526dea)`, `[IEvent](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-event#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_event)` > callback)` | `void` Fetches the event with the specified ID.  |
| [IncrementEvent](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-events-client#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_events_client_1a7933bfc76b28da069d7b1b2d1f4e7fd3)`(string eventId, uint stepsToIncrement)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `void` Increments the indicated event.           |

## Public functions

### FetchAllEvents

```c#
void FetchAllEvents(
  DataSource source,
  Action< ResponseStatus, List< IEvent >> callback
)
```  
Fetches all events defined for this game.

<br />

|                                                                                                                                                                                                                                                                         Details                                                                                                                                                                                                                                                                          ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------| | `source`   | The source of the event (i.e. whether we can return stale cached values).                                                                                     | | `callback` | A callback for the results of the request. The passed list will only be non-empty if the request succeeded. This callback will be invoked on the game thread. | |

### FetchEvent

```c#
void FetchEvent(
  DataSource source,
  string eventId,
  Action< ResponseStatus, IEvent > callback
)
```  
Fetches the event with the specified ID.

<br />

|                                                                                                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                                                                                                     ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-------------------------------------------------------------------------------------------------------------------------------------------------| | `source`   | The source of the event (i.e. whether we can return stale cached values).                                                                       | | `eventId`  | The ID of the event.                                                                                                                            | | `callback` | A callback for the result of the event. If the request failed, the passed event will be null. This callback will be invoked on the game thread. | |

### IncrementEvent

```c#
void IncrementEvent(
  string eventId,
  uint stepsToIncrement
)
```  
Increments the indicated event.

<br />

|                                                                                                Details                                                                                                ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------------|--------------------------------------| | `eventId`          | The ID of the event to increment.    | | `stepsToIncrement` | The number of steps to increment by. | |