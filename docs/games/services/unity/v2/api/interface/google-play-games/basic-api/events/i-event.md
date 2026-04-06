---
title: GooglePlayGames.BasicApi.Events.IEvent Interface Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-event
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.Events.IEvent

Data object representing an Event.

## Summary

Native.PInvoke.EventManager for more.

### Inheritance

Direct Known Subclasses:[GooglePlayGames.BasicApi.Events.Event](/games/services/unity/v2/api/class/google-play-games/basic-api/events/event)

| Properties | |
| --- | --- |
| `CurrentCount` | `ulong`  The current count for this event. |
| `Description` | `string`  The description of the event. |
| `Id` | `string`  The ID of the event. |
| `ImageUrl` | `string`  The URL of the image for the event. |
| `Name` | `string`  The name of the event. |
| `Visibility` | `EventVisibility`  The visibility of the event. |

## Properties

### CurrentCount

```
ulong CurrentCount
```

The current count for this event.

### Description

```
string Description
```

The description of the event.

### Id

```
string Id
```

The ID of the event.

### ImageUrl

```
string ImageUrl
```

The URL of the image for the event.

Empty if there is no image for this event.

The image URL.

### Name

```
string Name
```

The name of the event.

### Visibility

```
EventVisibility Visibility
```

The visibility of the event.