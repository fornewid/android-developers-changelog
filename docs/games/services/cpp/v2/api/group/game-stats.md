---
title: https://developer.android.com/games/services/cpp/v2/api/group/game-stats
url: https://developer.android.com/games/services/cpp/v2/api/group/game-stats
source: md.txt
---

# Play Games Services Game Stats

Native API for Play Games Services Game Stats.

## Summary

| ### Typedefs ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1ga0b05a4e6b1203559d27e56ad7b1ca905)(PgsStatusCode status_code, void *user_data)` | typedef `void(*` Callback for PgsGameStatsClient_recordEventImmediate. |
| `https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gae35fb896fd8a1c4144c77ac0bc6200dc)(PgsStatusCode status_code, void *user_data)` | typedef `void(*` Callback for PgsGameStatsClient_recordEventsImmediate. |

| ### Functions ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gab0b4cd91ff01afffb822a459fd7aeb26(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga7a0f58b5967954ea578f2c9523949067 *client, https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145 *event)` | `void` Records a single player game event. |
| `https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gaa11f7cee9353cbd8822ad5b36f33da44(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga7a0f58b5967954ea578f2c9523949067 *client, https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145 *event, https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1ga0b05a4e6b1203559d27e56ad7b1ca905 callback, void *user_data)` | `void` Records a single player game event immediately. |
| `https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gadb437808ae33d20d96f0664af4618206(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga7a0f58b5967954ea578f2c9523949067 *client, const https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145 *events, int32_t events_count)` | `void` Records a list of player game events. |
| `https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1ga7a499cdbb0a17156521dd482b3c14c5c(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga7a0f58b5967954ea578f2c9523949067 *client, const https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145 *events, int32_t events_count, https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gae35fb896fd8a1c4144c77ac0bc6200dc callback, void *user_data)` | `void` Records a list of player game events immediately. |
| `https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gafb1a243a893f31f79c1634c6f746ac57(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga7a0f58b5967954ea578f2c9523949067 *client)` | `void` Requests an upload of player game events. |

## Typedefs

### PgsGameStatsClient_RecordEventImmediateCallback

```c++
void(* PgsGameStatsClient_RecordEventImmediateCallback)(PgsStatusCode status_code, void *user_data)
```
Callback for PgsGameStatsClient_recordEventImmediate.

This is invoked after the asynchronous operation to record the event completes or fails.

<br />

Details Parameters `status_code` Result of the operation. PGS_STATUS_SUCCESS on success. `user_data` Pointer to the user-provided data passed in the original call.

### PgsGameStatsClient_RecordEventsImmediateCallback

```c++
void(* PgsGameStatsClient_RecordEventsImmediateCallback)(PgsStatusCode status_code, void *user_data)
```
Callback for PgsGameStatsClient_recordEventsImmediate.

This is invoked after the asynchronous operation to record the events completes or fails.

<br />

Details Parameters `status_code` Result of the operation. PGS_STATUS_SUCCESS on success. `user_data` Pointer to the user-provided data passed in the original call.

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

Details Parameters `client` The client handle. `event` The player game event to record.

### PgsGameStatsClient_recordEventImmediate

```c++
void PgsGameStatsClient_recordEventImmediate(
  PgsGameStatsClient *client,
  PgsPlayerGameEvent *event,
  PgsGameStatsClient_RecordEventImmediateCallback callback,
  void *user_data
)
```
Records a single player game event immediately.

This method attempts to record the event locally and invokes the callback when the local write is successful. Note that the event is still buffered locally for background upload. See [PgsGameStatsClient_requestEventsUpload()](https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gafb1a243a893f31f79c1634c6f746ac57) if you need to trigger an upload of buffered events.

<br />

Details Parameters `client` The client handle. `event` The player game event to record. `callback` Function to be called with the result of the asynchronous operation. See PgsGameStatsClient_RecordEventImmediateCallback. `user_data` Arbitrary data pointer to be passed back to the callback.

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

Details Parameters `client` The client handle. `events` An array of player game events to record. `events_count` The number of events in the array.

### PgsGameStatsClient_recordEventsImmediate

```c++
void PgsGameStatsClient_recordEventsImmediate(
  PgsGameStatsClient *client,
  const PgsPlayerGameEvent *events,
  int32_t events_count,
  PgsGameStatsClient_RecordEventsImmediateCallback callback,
  void *user_data
)
```
Records a list of player game events immediately.

This method attempts to record the events locally and invokes the callback when the local write is successful. Note that the events are still buffered locally for background upload. See [PgsGameStatsClient_requestEventsUpload()](https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gafb1a243a893f31f79c1634c6f746ac57) if you need to trigger an upload of buffered events.

Batching events into a list is more efficient than calling [PgsGameStatsClient_recordEventImmediate()](https://developer.android.com/games/services/cpp/v2/api/group/game-stats#group__game__stats_1gaa11f7cee9353cbd8822ad5b36f33da44) multiple times in rapid succession.

<br />

Details Parameters `client` The client handle. `events` An array of player game events to record. `events_count` The number of events in the array. `callback` Function to be called with the result of the asynchronous operation. See PgsGameStatsClient_RecordEventsImmediateCallback. `user_data` Arbitrary data pointer to be passed back to the callback.

### PgsGameStatsClient_requestEventsUpload

```c++
void PgsGameStatsClient_requestEventsUpload(
  PgsGameStatsClient *client
)
```
Requests an upload of player game events.

This method operates in a "fire-and-forget" manner. It requests an asynchronous background upload of all locally buffered events. Locally stored events are cleared upon successful upload.

<br />

Details Parameters `client` The client handle.