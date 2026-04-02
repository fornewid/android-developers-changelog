---
title: GooglePlayGames.BasicApi.Events.IEventsClient Interface Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-events-client
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.Events.IEventsClient

An interface for interacting with events.

## Summary

See online [documentation for Events](https://developers.google.com/games/services/common/concepts/events) for more information.

All callbacks in this interface must be invoked on the game thread.

| Public functions | |
| --- | --- |
| `FetchAllEvents(DataSource source, Action< ResponseStatus, List< IEvent >> callback)` | `void`  Fetches all events defined for this game. |
| `FetchEvent(DataSource source, string eventId, Action< ResponseStatus, IEvent > callback)` | `void`  Fetches the event with the specified ID. |
| `IncrementEvent(string eventId, uint stepsToIncrement)` | `void`  Increments the indicated event. |

## Public functions

### FetchAllEvents

```
void FetchAllEvents(
  DataSource source,
  Action< ResponseStatus, List< IEvent >> callback
)
```

Fetches all events defined for this game.

Details | || Parameters | |  |  | | --- | --- | | `source` | The source of the event (i.e. whether we can return stale cached values). | | `callback` | A callback for the results of the request. The passed list will only be non-empty if the request succeeded. This callback will be invoked on the game thread. | |

### FetchEvent

```
void FetchEvent(
  DataSource source,
  string eventId,
  Action< ResponseStatus, IEvent > callback
)
```

Fetches the event with the specified ID.

Details | || Parameters | |  |  | | --- | --- | | `source` | The source of the event (i.e. whether we can return stale cached values). | | `eventId` | The ID of the event. | | `callback` | A callback for the result of the event. If the request failed, the passed event will be null. This callback will be invoked on the game thread. | |

### IncrementEvent

```
void IncrementEvent(
  string eventId,
  uint stepsToIncrement
)
```

Increments the indicated event.

Details | || Parameters | |  |  | | --- | --- | | `eventId` | The ID of the event to increment. | | `stepsToIncrement` | The number of steps to increment by. | |