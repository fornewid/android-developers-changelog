---
title: https://developer.android.com/games/services/cpp/v2/api/group/player-game-event
url: https://developer.android.com/games/services/cpp/v2/api/group/player-game-event
source: md.txt
---

# Play Games Services Player Game Event

Data interface for constructing player game events.

## Summary

| ### Typedefs ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145` | typedef `struct https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145` An opaque handle to the PlayerGameEvent builder. |

| ### Functions ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1ga0a7831fade94e7c463471084dd2d7f11(const char *event_name)` | `https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145 *` Creates a new PlayerGameEvent builder. |
| `https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1ga34b829fbca5be8e23f6da6bc9e766dc9(https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145 *event)` | `void` Destroys a PlayerGameEvent handle. |
| `https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1ga9d9b62711f46ec07fee9d58a8fd790a4(https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145 *event, const char *key, bool value)` | `void` Adds a boolean property to the event. |
| `https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1ga0cd76a9bb10bdfd334f10619b6ac5e4b(https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145 *event, const char *key, double value)` | `void` Adds a double property to the event. |
| `https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae6f7a29a80ee53c350efa0c56f0bfd80(https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145 *event, const char *key, int64_t value)` | `void` Adds a long property to the event. |
| `https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1ga99b037f5b0f97f2030fd70e659460123(https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1gae36a74b9855223a6b27b8a0667337145 *event, const char *key, const char *value)` | `void` Adds a string property to the event. |

## Typedefs

### PgsPlayerGameEvent

```c++
struct PgsPlayerGameEvent PgsPlayerGameEvent
```
An opaque handle to the PlayerGameEvent builder.

## Functions

### PgsPlayerGameEvent_create

```c++
PgsPlayerGameEvent * PgsPlayerGameEvent_create(
  const char *event_name
)
```
Creates a new PlayerGameEvent builder.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `event_name` | The name of the event. | |
| **Returns** | A new PgsPlayerGameEvent handle, or NULL on failure. This handle must be released with [PgsPlayerGameEvent_destroy()](https://developer.android.com/games/services/cpp/v2/api/group/player-game-event#group__player__game__event_1ga34b829fbca5be8e23f6da6bc9e766dc9). |

### PgsPlayerGameEvent_destroy

```c++
void PgsPlayerGameEvent_destroy(
  PgsPlayerGameEvent *event
)
```
Destroys a PlayerGameEvent handle.

This function releases all resources associated with the handle.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `event` | The event handle to destroy. | |

### PgsPlayerGameEvent_putBoolean

```c++
void PgsPlayerGameEvent_putBoolean(
  PgsPlayerGameEvent *event,
  const char *key,
  bool value
)
```
Adds a boolean property to the event.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `event` | The event handle. | | `key` | The property key. | | `value` | The property value. | |

### PgsPlayerGameEvent_putDouble

```c++
void PgsPlayerGameEvent_putDouble(
  PgsPlayerGameEvent *event,
  const char *key,
  double value
)
```
Adds a double property to the event.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `event` | The event handle. | | `key` | The property key. | | `value` | The property value. | |

### PgsPlayerGameEvent_putLong

```c++
void PgsPlayerGameEvent_putLong(
  PgsPlayerGameEvent *event,
  const char *key,
  int64_t value
)
```
Adds a long property to the event.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `event` | The event handle. | | `key` | The property key. | | `value` | The property value. | |

### PgsPlayerGameEvent_putString

```c++
void PgsPlayerGameEvent_putString(
  PgsPlayerGameEvent *event,
  const char *key,
  const char *value
)
```
Adds a string property to the event.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `event` | The event handle. | | `key` | The property key. | | `value` | The property value. | |