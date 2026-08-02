---
title: https://developer.android.com/games/services/cpp/v2/api/group/game-stats
url: https://developer.android.com/games/services/cpp/v2/api/group/game-stats
source: md.txt
---

# Play Games Services Game Stats

Native API for Play Games Services Game Stats.

## Summary

| ### Functions ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gab0b4cd91ff01afffb822a459fd7aeb26(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga7a0f58b5967954ea578f2c9523949067 *client, https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145 *event)` | `void` Records a single player game event. |
| `https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gadb437808ae33d20d96f0664af4618206(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga7a0f58b5967954ea578f2c9523949067 *client, const https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145 *events, int32_t events_count)` | `void` Records a list of player game events. |
| `https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gafb1a243a893f31f79c1634c6f746ac57(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga7a0f58b5967954ea578f2c9523949067 *client)` | `void` Requests an upload of player game events. |

## Functions

### PgsGameStatsClient_recordEvent

```c++
void PgsGameStatsClient_recordEvent(
  PgsGameStatsClient *client,
  PgsPlayerGameEvent *event
)
```
Records a single player game event.

This method operates in a "fire-and-forget" manner. The event is buffered locally for background upload. Note that the event may not be sent to the server until the next scheduled sync. See [PgsGameStatsClient_requestEventsUpload()](https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gafb1a243a893f31f79c1634c6f746ac57) if you need to trigger an upload of buffered events.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `client` | The client handle. | | `event` | The player game event to record. | |

### PgsGameStatsClient_recordEvents

```c++
void PgsGameStatsClient_recordEvents(
  PgsGameStatsClient *client,
  const PgsPlayerGameEvent *events,
  int32_t events_count
)
```
Records a list of player game events.

This method operates in a "fire-and-forget" manner. The events are buffered locally for background upload. Note that the events may not be sent to the server until the next scheduled sync. See [PgsGameStatsClient_requestEventsUpload()](https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gafb1a243a893f31f79c1634c6f746ac57) if you need to trigger an upload of buffered events.

Batching events into a list is more efficient than calling [PgsGameStatsClient_recordEvent()](https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gab0b4cd91ff01afffb822a459fd7aeb26) multiple times in rapid succession.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `client` | The client handle. | | `events` | An array of player game events to record. | | `events_count` | The number of events in the array. | |

### PgsGameStatsClient_requestEventsUpload

```c++
void PgsGameStatsClient_requestEventsUpload(
  PgsGameStatsClient *client
)
```
Requests an upload of player game events.

This method operates in a "fire-and-forget" manner. It requests an asynchronous background upload of all locally buffered events. Locally stored events are cleared upon successful upload.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `client` | The client handle. | |